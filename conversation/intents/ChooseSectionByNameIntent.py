from conversation.intents.Intent import Intent


class ChooseSectionByName(Intent):

    def __init__(self, chosen_section_name):
        self.name = self.__class__.__name__
        self.chosen_section_name = chosen_section_name

    def update_session(self, session):

        # gets the chosen selection from the choice
        session.chosen_selection = [choice[2] for choice in session.choices if choice[4] == self.chosen_section_name][0]

        # gets the selection description from the choice, for the prompt
        chosen_selection_description = [choice[4] for choice in session.choices if choice[4] == self.chosen_section_name]
        session.chosen_selection_description = ''.join(chosen_selection_description)
        return session


def unmarshall(intent):
    chosen_section_name = intent['sessionState']['intent']['slots']['SectionDescription']['value']['interpretedValue']
    return ChooseSectionByName(chosen_section_name)
