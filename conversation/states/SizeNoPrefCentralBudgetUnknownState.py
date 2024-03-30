
from conversation.states.SizeYesPrefCentralBudgetUnknownState import SizeYesPrefCentralBudgetUnknownState
from conversation.states.State import State


def _transition(next_session, intent_name, qualifiers, stage):
    match intent_name:
        case 'SizeIntent':
            return SizeYesPrefCentralBudgetUnknownState(next_session, qualifiers, stage)
        case 'FallbackIntent':
            next_session.error = True
            return SizeNoPrefCentralBudgetUnknownState(next_session, qualifiers, stage)
        case _:
            next_session.error = True
            return SizeNoPrefCentralBudgetUnknownState(next_session, qualifiers, stage)


class SizeNoPrefCentralBudgetUnknownState(State):
    def __init__(self, session, qualifiers, stage):
        self.name = self.__class__.__name__
        self.session = session
        self.qualifiers = qualifiers
        self.stage = stage
        self.context_tags = ['NoPartySize', 'NoBudget']
        self.is_terminal = False

    def get_next_prompt(self, availability):

        central_sections = self.qualifiers['central_sections']
        max_chain_length = availability.max_available_in_sections(central_sections)
        self.context_tags.append('AskedForPartySize')

        if max_chain_length == 0:
            self.is_terminal = True
            return 'There are no seats left in the most central sections'
        elif max_chain_length < 3:
            return 'There is limited availability in the most central sections. How many tickets do you want?'
        else:
            return 'There is availability in the central sections. How many tickets do you want?'

    def transition(self, intent):
        next_session = intent.update_session(self.session)
        return _transition(next_session, intent.name, self.qualifiers, self.stage)

    def is_terminal(self):
        return self.is_terminal
