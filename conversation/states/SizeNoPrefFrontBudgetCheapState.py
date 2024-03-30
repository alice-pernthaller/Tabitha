from conversation.states.SizeYesPrefFrontBudgetCheapState import SizeYesPrefFrontBudgetCheapState
from conversation.states.State import State


def _transition(next_session, intent_name, qualifiers, stage):
    match intent_name:
        case 'SizeIntent':
            return SizeYesPrefFrontBudgetCheapState(next_session, qualifiers, stage)
        case 'FallbackIntent':
            next_session.error = True
            return SizeNoPrefFrontBudgetCheapState(next_session, qualifiers, stage)
        case _:
            next_session.error = True
            return SizeNoPrefFrontBudgetCheapState(next_session, qualifiers, stage)


class SizeNoPrefFrontBudgetCheapState(State):
    def __init__(self, session, qualifiers, stage):
        self.name = self.__class__.__name__
        self.session = session
        self.qualifiers = qualifiers
        self.stage = stage
        self.context_tags = ['NoPartySize']
        self.is_terminal = False

    def get_next_prompt(self, availability):

        # no point in asking for party size if there are only expensive tickets.
        # prequery availability for cheap tickets

        cheap_sections = self.qualifiers['cheap_sections']
        max_chain_length = availability.max_available_in_sections(cheap_sections)
        self.context_tags.append('AskedForPartySize')

        if max_chain_length == 0:
            self.is_terminal = True
            return 'There are no cheap seats left.'
        elif max_chain_length < 3:
            return 'There is limited availability in the cheaper sections. How many tickets do you want?'
        else:
            return 'There is availability in the cheaper sections. How many tickets do you want?'

    def transition(self, intent):
        next_session = intent.update_session(self.session)
        return _transition(next_session, intent.name, self.qualifiers, self.stage)

    def is_terminal(self):
        return self.is_terminal
