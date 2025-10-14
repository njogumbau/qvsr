# qvsr/__init__.py (oTree app)
from otree.api import *
import json
from typing import Callable, Dict

doc = """
oTree-QVSR: Quadratic Voting Survey Research app
"""

# ---- Cost functions ---------------------------------------------------------

def quadratic_cost(v: int) -> float:
    # Standard QV cost: v^2 (sign doesn't reduce cost)
    return float(v * v)

def concave_pilot(v: int) -> float:
    # Example alternative
    return float((abs(v) ** 1.6))

COST_FUNCTIONS: Dict[str, Callable[[int], float]] = {
    "quadratic": quadratic_cost,
    "concave_pilot": concave_pilot,
}

def _get_cost_fn(session):
    """Resolve the cost function from session.config."""
    fn = session.config.get("qvsr_cost_fn", "quadratic")
    if isinstance(fn, str):
        return COST_FUNCTIONS.get(fn, quadratic_cost)
    if callable(fn):
        return fn
    return quadratic_cost


# ---- oTree models -----------------------------------------------------------

class C(BaseConstants):
    NAME_IN_URL = "qvsr"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Raw votes by option as JSON string: {"Option A": 2, "Option B": -1, ...}
    votes = models.StringField()
    # Per-option costs as JSON string: {"Option A": 4.0, "Option B": 1.0, ...}
    costs = models.StringField()
    # Budget accounting
    total_cost = models.FloatField(initial=0.0)
    remaining_credits = models.FloatField(initial=0.0)


# ---- Pages ------------------------------------------------------------------

class Vote(Page):
    form_model = "player"
    form_fields = ["votes"]

    @staticmethod
    def vars_for_template(player: Player):
        cfg = player.session.config
        return {
            "options": cfg["qvsr_options"],
            "credits": cfg["qvsr_credits"],
            "allow_negative": cfg.get("qvsr_allow_negative", False),
            "feedback": cfg.get("qvsr_feedback", True),
            "cost_fn_name": cfg.get("qvsr_cost_fn", "quadratic")
                if isinstance(cfg.get("qvsr_cost_fn"), str)
                else "custom",
        }

    @staticmethod
    def error_message(player: Player, values):
        cfg = player.session.config
        options = cfg["qvsr_options"]
        credits = cfg["qvsr_credits"]
        allow_negative = cfg.get("qvsr_allow_negative", False)
        cost_fn = _get_cost_fn(player.session)

        # Parse and validate payload
        try:
            votes = json.loads(values["votes"])
        except Exception:
            return "Invalid data format."

        if not isinstance(votes, dict):
            return "Invalid data format."

        # Validate each option vote
        total_cost = 0.0
        for opt in options:
            v = votes.get(opt, 0)
            if not isinstance(v, int):
                return f"Votes for '{opt}' must be integers."
            if not allow_negative and v < 0:
                return f"Negative votes are not allowed (check '{opt}')."
            # Cost is based on magnitude; sign does not discount cost
            total_cost += float(cost_fn(v))

        if total_cost > float(credits):
            return f"You exceeded your {credits} credit budget (total cost = {total_cost:.2f})."

        # Also block unknown keys if provided
        extra = set(votes.keys()) - set(options)
        if extra:
            return f"Unknown option(s) in submission: {', '.join(sorted(extra))}"

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        cfg = player.session.config
        options = cfg["qvsr_options"]
        credits = float(cfg["qvsr_credits"])
        cost_fn = _get_cost_fn(player.session)

        votes = json.loads(player.votes)
        costs = {opt: float(cost_fn(int(votes.get(opt, 0)))) for opt in options}

        total_cost = sum(costs.values())
        remaining = max(0.0, credits - total_cost)

        player.costs = json.dumps(costs)
        player.total_cost = total_cost
        player.remaining_credits = remaining


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        cfg = player.session.config
        options = cfg["qvsr_options"]

        votes = json.loads(player.votes)
        costs = json.loads(player.costs)

        rows = []
        for opt in options:
            rows.append({
                "option": opt,
                "votes": int(votes.get(opt, 0)),
                "cost": float(costs.get(opt, 0.0)),
            })

        return {
            "rows": rows,
            "total_cost": player.total_cost,
            "remaining_credits": player.remaining_credits,
        }


page_sequence = [Vote, Results]
