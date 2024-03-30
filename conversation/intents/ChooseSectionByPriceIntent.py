from conversation.intents.Intent import Intent


class ChooseSectionByPrice(Intent):

    def __init__(self, chosen_section_price):
        self.name = self.__class__.__name__
        self.chosen_section_price = chosen_section_price

    def update_session(self, session):

        # gets the chosen selection from the choice
        session.chosen_selection = [choice[2] for choice in session.choices if choice[0] == self.chosen_section_price][0]

        # gets the selection description from the choice, for the prompt
        chosen_selection_description = [choice[4] for choice in session.choices if choice[0] == self.chosen_section_price]
        session.chosen_selection_description = ''.join(chosen_selection_description)
        return session


def unmarshall(intent):
    chosen_section_price = int(intent['sessionState']['intent']['slots']['Price']['value']['interpretedValue'])
    return ChooseSectionByPrice(chosen_section_price)
