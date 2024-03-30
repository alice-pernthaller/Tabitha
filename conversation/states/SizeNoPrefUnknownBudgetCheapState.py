from conversation.states.SizeYesPrefUnknownBudgetCheapState import SizeYesPrefUnknownBudgetCheapState
from conversation.states.State import State


def _transition(next_session, intent_name, qualifiers, stage):
    match intent_name:
        case 'SizeIntent': return SizeYesPrefUnknownBudgetCheapState(next_session, qualifiers, stage)
        case 'FallbackIntent':
            next_session.error = True
            return SizeNoPrefUnknownBudgetCheapState(next_session, qualifiers, stage)
        case _:
            next_session.error = True
            return SizeNoPrefUnknownBudgetCheapState(next_session, qualifiers, stage)


class SizeNoPrefUnknownBudgetCheapState(State):
    def __init__(self, session, qualifiers, stage):
        self.name = self.__class__.__name__
        self.session = session
        self.qualifiers = qualifiers
        self.stage = stage
        self.context_tags = ['NoPartySize', 'NoPreference']
        self.is_terminal = False

    def _get_party_size(self):
        return self.session.party_size

    def get_next_prompt(self, availability):

        # checks availability in the cheaper sections
        cheap_sections = self.qualifiers['cheap_sections']
        max_chain_length = availability.max_available_in_sections(cheap_sections)

        if max_chain_length == 0:
            self.is_terminal = True
            return "There is no availability in the cheaper sections."

        if max_chain_length < 3:
            return "There is limited availability in the cheaper sections. How many seats are you looking for?"

        else:
            return "There is availability in the cheaper sections. How many seats are you looking for?"

    def transition(self, intent):
        next_session = intent.update_session(self.session)
        return _transition(next_session, intent.name, self.qualifiers, self.stage)

    def is_terminal(self):
        return self.is_terminal
