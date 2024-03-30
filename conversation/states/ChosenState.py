from conversation.states.State import State


def _transition(next_session, intent_name, qualifiers, stage):
    match intent_name:
        case 'FallbackIntent':
            next_session.error = True
            return ChosenState(next_session, qualifiers, stage)
        case _:
            next_session.error = True
            return ChosenState(next_session, qualifiers, stage)


class ChosenState(State):

    def __init__(self, session, qualifiers, stage):
        self.name = self.__class__.__name__
        self.session = session
        self.context_tags = []
        self.is_terminal = True
        self.qualifiers = qualifiers
        self.stage = stage

    def get_next_prompt(self, availability):
        section_description = self.session.chosen_selection_description
        first_seat = self.session.chosen_selection.seats[0]

        if len(self.session.chosen_selection.seats) == 1:
            seat = first_seat
            return f"You have booked seat {seat.row}{seat.number} in the {section_description} section. Thank you for booking with us today!"

        elif len(self.session.chosen_selection.seats) == 2:
            second_seat = self.session.chosen_selection.seats[-1]
            return f"You have booked tickets {first_seat.row}{first_seat.number} and {second_seat.row}{second_seat.number} in the {section_description} section. Thank you for booking with us today!"

        else:
            last_seat = self.session.chosen_selection.seats[-1]
            return f"You have booked tickets {first_seat.row}{first_seat.number} to {last_seat.row}{last_seat.number} in the {section_description} section. Thank you for booking with us today!"

    def transition(self, intent):
        next_session = intent.update_session(self.session)
        return _transition(next_session, intent.name, self.qualifiers, self.stage)

    def is_terminal(self):
        return self.is_terminal
