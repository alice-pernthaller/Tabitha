from conversation.states.SizeNoPrefCentralBudgetCheapState import SizeNoPrefCentralBudgetCheapState
from conversation.states.SizeNoPrefCentralBudgetUnknownState import SizeNoPrefCentralBudgetUnknownState
from conversation.states.SizeNoPrefFrontBudgetCheapState import SizeNoPrefFrontBudgetCheapState
from conversation.states.SizeNoPrefFrontBudgetUnknownState import SizeNoPrefFrontBudgetUnknownState
from conversation.states.SizeNoPrefGoodViewBudgetCheapState import SizeNoPrefGoodViewBudgetCheapState
from conversation.states.SizeNoPrefGoodViewBudgetUnknownState import SizeNoPrefGoodViewBudgetUnknownState
from conversation.states.SizeNoPrefUnknownBudgetCheapState import SizeNoPrefUnknownBudgetCheapState
from conversation.states.SizeYesPrefCentralBudgetCheapState import SizeYesPrefCentralBudgetCheapState
from conversation.states.SizeYesPrefCentralBudgetUnknownState import SizeYesPrefCentralBudgetUnknownState
from conversation.states.SizeYesPrefFrontBudgetCheapState import SizeYesPrefFrontBudgetCheapState
from conversation.states.SizeYesPrefFrontBudgetUnknownState import SizeYesPrefFrontBudgetUnknownState
from conversation.states.SizeYesPrefGoodViewBudgetCheapState import SizeYesPrefGoodViewBudgetCheapState
from conversation.states.SizeYesPrefGoodViewBudgetUnknownState import SizeYesPrefGoodViewBudgetUnknownState
from conversation.states.SizeYesPrefUnknownBudgetCheapState import SizeYesPrefUnknownBudgetCheapState
from conversation.states.SizeYesPrefUnknownBudgetUnknownState import SizeYesPrefUnknownBudgetUnknownState
from conversation.states.State import State


def _transition(next_session, intent_name, qualifiers, stage):
    match intent_name:
        case 'SizeFrontCheapIntent': return SizeYesPrefFrontBudgetCheapState(next_session, qualifiers, stage)
        case 'FrontCheapIntent': return SizeNoPrefFrontBudgetCheapState(next_session, qualifiers, stage)
        case 'FrontIntent': return SizeNoPrefFrontBudgetUnknownState(next_session, qualifiers, stage)
        case 'CentralIntent': return SizeNoPrefCentralBudgetUnknownState(next_session, qualifiers, stage)
        case 'GoodViewIntent': return SizeNoPrefGoodViewBudgetUnknownState(next_session, qualifiers, stage)
        case 'SizeGoodViewCheapIntent': return SizeYesPrefGoodViewBudgetCheapState(next_session, qualifiers, stage)
        case 'SizeCentralCheapIntent': return SizeYesPrefCentralBudgetCheapState(next_session, qualifiers, stage)
        case 'GoodViewCheapIntent': return SizeNoPrefGoodViewBudgetCheapState(next_session, qualifiers, stage)
        case 'CentralCheapIntent': return SizeNoPrefCentralBudgetCheapState(next_session, qualifiers, stage)
        case 'SizeGoodViewIntent': return SizeYesPrefGoodViewBudgetUnknownState(next_session, qualifiers, stage)
        case 'SizeCentralIntent': return SizeYesPrefCentralBudgetUnknownState(next_session, qualifiers, stage)
        case 'SizeFrontIntent': return SizeYesPrefFrontBudgetUnknownState(next_session, qualifiers, stage)
        case 'SizeCheapIntent': return SizeYesPrefUnknownBudgetCheapState(next_session, qualifiers, stage)
        case 'SizeIntent': return SizeYesPrefUnknownBudgetUnknownState(next_session, qualifiers, stage)
        case 'CheapIntent': return SizeNoPrefUnknownBudgetCheapState(next_session, qualifiers, stage)
        case 'FallbackIntent':
            next_session.error = True
            return GreetingState(next_session, qualifiers, stage)
        case _:
            # Deal with any unexpected intents
            next_session.error = True  # set error - defensive
            return GreetingState(next_session, qualifiers, stage)


class GreetingState(State):

    def __init__(self, session, qualifiers, stage):
        self.name = self.__class__.__name__
        self.session = session
        self.qualifiers = qualifiers
        self.stage = stage
        self.context_tags = ['NoPartySize', 'NoPreference', 'NoBudget']
        self.is_terminal = False

    def get_next_prompt(self, availability):
        return "Hi! I'm Tabitha the TicketBot. How can I help you today?"

    def transition(self, intent):
        next_session = intent.update_session(self.session)
        return _transition(next_session, intent.name, self.qualifiers, self.stage)

    def is_terminal(self):
        return self.is_terminal
