from otree.api import *
import math
import json

doc = """
Quadratic Voting App
"""


class C(BaseConstants):
    NAME_IN_URL = 'oq'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    votes = models.StringField()
    quadratic_votes = models.StringField()
    total_votes = models.FloatField()


# PAGES
class Vote(Page):
    form_model = 'player'
    form_fields = ['votes']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "options": player.session.config['qvsr_options'],
            "total_votes": player.session.config['qvsr_total_votes'],
        }

    @staticmethod
    def error_message(player, values):
        try:
            votes = json.loads(values['votes'])
        except json.JSONDecodeError:
            return "Invalid data format."

        if not isinstance(votes, dict):
            return "Invalid data format."

        total_cost = 0
        for option in player.session.config['qvsr_options']:
            num_votes = votes.get(option, 0)
            if not isinstance(num_votes, int) or num_votes < 0:
                return f"Invalid vote count for {option}."
            total_cost += num_votes * num_votes

        if total_cost > player.session.config['qvsr_total_votes']:
            return f"You have exceeded your {player.session.config['qvsr_total_votes']} vote-credit budget!"

    @staticmethod
    def before_next_page(player, timeout_happened):
        votes = json.loads(player.votes)
        quadratic_votes = {option: num_votes * num_votes for option, num_votes in votes.items()}
        player.quadratic_votes = json.dumps(quadratic_votes)
        player.total_votes = sum(votes.values())


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        votes = json.loads(player.votes)
        quadratic_votes = json.loads(player.quadratic_votes)
        options = player.session.config['qvsr_options']
        vote_data = []
        for option in options:
            vote_data.append({
                'option': option,
                'votes': votes.get(option, 0),
                'quadratic_votes': quadratic_votes.get(option, 0)
            })

        return {
            "vote_data": vote_data
        }


page_sequence = [Vote, Results]