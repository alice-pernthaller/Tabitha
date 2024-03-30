from conversation.intents.Intent import Intent


class SizeFrontIntent(Intent):

    def __init__(self, party_size):
        self.name = self.__class__.__name__
        self.party_size = party_size

    def update_session(self, session):
        session.party_size = self.party_size
        return session


def unmarshall(intent):
    party_size = int(intent['sessionState']['intent']['slots']['PartySize']['value']['interpretedValue'])
    return SizeFrontIntent(party_size)
