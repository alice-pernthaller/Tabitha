from conversation.states.SizeYesPrefCentralBudgetUnknownState import SizeYesPrefCentralBudgetUnknownState
from conversation.states.SizeYesPrefFrontBudgetUnknownState import SizeYesPrefFrontBudgetUnknownState
from conversation.states.SizeYesPrefGoodViewBudgetUnknownState import SizeYesPrefGoodViewBudgetUnknownState
from conversation.states.State import State


def _transition(next_session, intent_name, qualifiers, stage):
    match intent_name:
        case 'FrontIntent':
            return SizeYesPrefFrontBudgetUnknownState(next_session, qualifiers, stage)
        case 'CentralIntent':
            return SizeYesPrefCentralBudgetUnknownState(next_session, qualifiers, stage)
        case 'GoodViewIntent':
            return SizeYesPrefGoodViewBudgetUnknownState(next_session, qualifiers, stage)
        case 'FallbackIntent':
            next_session.error = True
            return SizeYesPrefUnknownBudgetUnknownState(next_session, qualifiers, stage)
        case _:
            next_session.error = True
            return SizeYesPrefUnknownBudgetUnknownState(next_session, qualifiers, stage)


class SizeYesPrefUnknownBudgetUnknownState(State):
    def __init__(self, session, qualifiers, stage):
        self.name = self.__class__.__name__
        self.session = session
        self.qualifiers = qualifiers
        self.stage = stage
        self.context_tags = ['NoPreference', 'NoBudget']
        self.is_terminal = False

    def _get_party_size(self):
        return self.session.party_size

    def get_next_prompt(self, availability):

        # checks that there is a chain large enough in the theatre to fit the party
        all_sections = self.qualifiers['all_sections']
        max_chain_length = availability.max_available_in_sections(all_sections)
        if self._get_party_size() > max_chain_length:
            self.is_terminal = True
            return "Sorry, we cannot accommodate a party of that size. Goodbye."

        front_sections = self.qualifiers['front_sections']
        max_chain_length = availability.max_available_in_sections(front_sections)
        if self._get_party_size() <= max_chain_length:
            front = True
        else:
            front = False

        good_view_sections = self.qualifiers['good_view_sections']
        max_chain_length = availability.max_available_in_sections(good_view_sections)
        if self._get_party_size() <= max_chain_length:
            good_view = True
        else:
            good_view = False

        central_sections = self.qualifiers['central_sections']
        max_chain_length = availability.max_available_in_sections(central_sections)
        if self._get_party_size() <= max_chain_length:
            central = True
        else:
            central = False

        # the state wants to elicit a preference from the user
        if front and good_view and central:
            return "Are you looking for seats that are near the front, near the centre, or which offer the best view?"

        if front and central:
            return "Are you looking for seats that are near the front or near the centre?"

        if front and good_view:
            return "Are you looking for seats that are near the front or that offer the best view of the stage?"

        else:
            return "There is limited availability left. Would you prioritise sitting near the front, near the centre, or with the best view of the stage?"

    def transition(self, intent):
        next_session = intent.update_session(self.session)
        return _transition(next_session, intent.name, self.qualifiers, self.stage)

    def is_terminal(self):
        return self.is_terminal
