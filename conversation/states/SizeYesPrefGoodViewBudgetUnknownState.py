from conversation.states.ChosenState import ChosenState
from conversation.states.State import State
from theatre import my_constants
from theatre.consumer.Query import Query
from theatre.consumer.metrics.ViewOfStage import ViewOfStage


def _transition(next_session, intent_name, qualifiers, stage):
    match intent_name:
        case 'ChooseSectionByPrice': return ChosenState(next_session, qualifiers, stage)
        case 'ChooseSectionByName': return ChosenState(next_session, qualifiers, stage)
        case 'FallbackIntent':
            next_session.error = True
            return SizeYesPrefGoodViewBudgetUnknownState(next_session, qualifiers, stage)
        case _:
            next_session.error = True
            return SizeYesPrefGoodViewBudgetUnknownState(next_session, qualifiers, stage)


class SizeYesPrefGoodViewBudgetUnknownState(State):
    def __init__(self, session, qualifiers, stage):
        self.name = self.__class__.__name__
        self.session = session
        self.qualifiers = qualifiers
        self.stage = stage
        self.context_tags = []
        self.is_terminal = False

    def _get_party_size(self):
        return self.session.party_size

    def get_next_prompt(self, availability):

        query = Query(self._get_party_size(), float('inf'), ViewOfStage(self.stage), my_constants.price_list)
        choices = availability.find_best_selection(query)
        self.session.choices = choices

        return_string = "Tickets are available in the following sections:"
        for choice in choices:
            return_string += f'\n £{choice[0]} in the {choice[4]}'

        self.context_tags.append('SelectionsOffered')
        return return_string

    def transition(self, intent):
        next_session = intent.update_session(self.session)
        return _transition(next_session, intent.name, self.qualifiers, self.stage)

    def is_terminal(self):
        return self.is_terminal
