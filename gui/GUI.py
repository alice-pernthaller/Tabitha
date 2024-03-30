import tkinter as tk

from conversation.ConversationManager import ConversationManager
from gui import Render


class GUI:

    # gets the new prompt from the conversation manager and updates the GUI with it
    def _show_prompt(self):
        newtext = self.conversation_manager.get_next_prompt()
        self.line1.config(text=newtext)
        self.line1.update()

    # resets for the next customer
    def _next_conversation(self):
        self.finish_button['state'] = 'disabled'
        self.conversation_manager = ConversationManager(self.availability, self.client, self.qualifiers, self.stage)

        self._show_prompt()

    def _get_response(self, event):
        text = self.enterbox.get()  # gets user input
        self.enterbox.delete(0, 'end')
        print(f"User: {text}")  # prints user input to log

        if text.strip() != '':  # checks for empty string
            self.conversation_manager.update_with_input(text)  # gives the input to the conversation manager to process
            self._show_prompt()

            # at the end of the conversation, the GUI greys out the booked seats and starts a new conversation
            if self.conversation_manager.current_state.is_terminal:
                self.finish_button['state'] = 'normal'
                if self.conversation_manager.session.chosen_selection is not None:
                    self._grey_out_chosen_selection(self.conversation_manager.session.chosen_selection)

    def __init__(self, stage, seats, availability, client, qualifiers):
        self.stage = stage
        self.seats = seats
        self.availability = availability
        self.client = client
        self.qualifiers = qualifiers
        self.conversation_manager = ConversationManager(self.availability, self.client, self.qualifiers, self.stage)

        self.window = tk.Tk()
        self.window.title('Tabitha')
        self.window.geometry('1120x740')

        self.c = tk.Canvas(self.window)

        # the GUI has a line of text which displays the response to the user's input
        self.line1 = tk.Label(self.window, text=self.conversation_manager.get_next_prompt(), font=("Arial", 25), wraplength=1120)
        self.line1.pack()

        # the 'next customer' button is only enabled at the end of a conversation, to start a new one
        self.finish_button = tk.Button(self.window, text='Next Customer', command=self._next_conversation, state='disabled', font=("Arial", 25))
        self.finish_button.pack()

        # when the user hits the 'enter' key, the GUI takes the input and processes the response
        self.enterbox = tk.Entry(self.window, width=80)
        self.enterbox.bind('<Return>', self._get_response)
        self.enterbox.pack()

    # when run, the GUI draws all of the seats, with the booked ones in grey
    def run(self):
        self.c.pack(fill="both", expand=True)
        Render.draw_stage(self.stage, self.c)
        for seat in self.seats.values():
            Render.draw_seat(seat, self.c, False)
        for chain in self.availability.get_all_chains():
            for seat in chain.seats:
                Render.draw_seat(seat, self.c, True)
        self.window.mainloop()

    # when seats are booked, they turn grey in the GUI
    def _grey_out_chosen_selection(self, selection):
        for seat in selection.seats:
            Render.draw_seat(seat, self.c, False)

        first_seat = selection.seats[0]
        last_seat = selection.seats[-1]

        first_seat_x = Render.translate_x(first_seat.x)
        first_seat_y = Render.translate_y(first_seat.y)

        last_seat_x = Render.translate_x(last_seat.x)
        last_seat_y = Render.translate_y(last_seat.y)

        x1 = first_seat_x - 7
        y1 = first_seat_y - 7
        x2 = last_seat_x + 7
        y2 = last_seat_y + 7

        self.c.create_rectangle(x1, y1, x2, y2)
