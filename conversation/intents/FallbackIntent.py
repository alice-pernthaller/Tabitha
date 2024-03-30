from conversation.intents.Intent import Intent


class FallbackIntent(Intent):

    def __init__(self):
        self.name = self.__class__.__name__

    def update_session(self, session):
        return session


def unmarshall(intent):
    return FallbackIntent()
