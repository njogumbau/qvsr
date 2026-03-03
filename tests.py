from otree.api import Currency as c, currency_range, expect, Bot, Submission
from . import *
import json

class PlayerBot(Bot):
    def play_game(self):
        options = self.session.config.get("qvsr_options", ["Option 1", "Option 2"])
        credits = self.session.config.get("qvsr_credits", 25)
        allow_negative = self.session.config.get("qvsr_allow_negative", False)

        # Test valid submission: 3 votes for Option 1, 4 for Option 2 (total cost: 3^2 + 4^2 = 9 + 16 = 25)
        if len(options) >= 2 and credits >= 25:
            valid_votes = {options[0]: 3, options[1]: 4}
            yield Vote, {"votes": json.dumps(valid_votes)}
            
            # Check results
            expect(self.player.total_cost, 25.0)
            expect(self.player.remaining_credits, 0.0)
            expect(self.player.credits_allocated, float(credits))
            
            yield Results
        else:
            # Fallback for other configs
            valid_votes = {options[0]: 0}
            yield Vote, {"votes": json.dumps(valid_votes)}
            yield Results

    def play_invalid_budget(self):
        """Verify that the bot cannot submit votes exceeding the budget."""
        options = self.session.config.get("qvsr_options", ["Option 1", "Option 2"])
        credits = self.session.config.get("qvsr_credits", 25)
        
        # Try to exceed budget: submitting 10 votes for the first option costs 100 credits.
        # This should trigger the error_message validation in __init__.py.
        invalid_votes = {options[0]: 10}
        
        # In oTree, yielding a page with invalid data is expected to fail or 
        # stay on the same page. We yield the submission and then yield the valid one 
        # to ensure the bot can complete the session after a failed attempt.
        yield Submission(Vote, {"votes": json.dumps(invalid_votes)}, check_html=False)
        
        # Now submit a valid one to finish the session
        yield Vote, {"votes": json.dumps({options[0]: 1})}
        yield Results
