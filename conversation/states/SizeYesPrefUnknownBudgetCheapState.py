from conversation.states.SizeYesPrefCentralBudgetCheapState import SizeYesPrefCentralBudgetCheapState
from conversation.states.SizeYesPrefFrontBudgetCheapState import SizeYesPrefFrontBudgetCheapState
from conversation.states.SizeYesPrefGoodViewBudgetCheapState import SizeYesPrefGoodViewBudgetCheapState
from conversation.states.State import State


def _transition(next_session, intent_name, qualifiers, stage):
    match intent_name:
        case 'FrontIntent':
            return SizeYesPrefFrontBudgetCheapState(next_session, qualifiers, stage)
        case 'CentralIntent':
            return SizeYesPrefCentralBudgetCheapState(next_session, qualifiers, stage)
        case 'GoodViewIntent':
            return SizeYesPrefGoodViewBudgetCheapState(next_session, qualifiers, stage)
        case 'FallbackIntent':
            next_session.error = True
            return SizeYesPrefUnknownBudgetCheapState(next_session, qualifiers, stage)
        case _:
            next_session.error = True
            return SizeYesPrefUnknownBudgetCheapState(next_session, qualifiers, stage)


class SizeYesPrefUnknownBudgetCheapState(State):
    def __init__(self, session, qualifiers, stage):
        self.name = self.__class__.__name__
        self.session = session
        self.qualifiers = qualifiers
        self.stage = stage
        self.context_tags = ['NoPreference']
        self.is_terminal = False

    def _get_party_size(self):
        return self.session.party_size

    def get_next_prompt(self, availability):

        # checks the availability for cheap seats
        party_size = self._get_party_size()

        cheap_sections = self.qualifiers['cheap_sections']
        max_chain_length = availability.max_available_in_sections(cheap_sections)

        if party_size <= max_chain_length:
            return f"There is availability in the cheaper sections for {party_size} tickets. Would you like to look for seats that are front, central, or offer a good view of the stage?"

        else:
            return "There is limited availability in the cheaper sections. Would you like to look for seats that are front, central, or offer a good view of the stage?"

    def transition(self, intent):
        next_session = intent.update_session(self.session)
        return _transition(next_session, intent.name, self.qualifiers, self.stage)

    def is_terminal(self):
        return self.is_terminal
