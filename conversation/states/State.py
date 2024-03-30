class State:

    # a state returns a prompt to elicit the next necessary piece of information from the user
    def get_next_prompt(self, availability):
        pass

    # given an intent, a state transitions to another state
    def transition(self, intent):
        pass

    # a state knows if it is the final state of the conversation
    def is_terminal(self):
        pass