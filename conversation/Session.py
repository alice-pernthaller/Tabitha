# contains information about the current conversation
class Session:
    def __init__(self):
        self.party_size = None
        self.chosen_selection = None
        self.error = False

    # error handling - when Lex does not understand the input
    def check_and_clear_error(self):
        result = self.error
        self.error = False
        return result
