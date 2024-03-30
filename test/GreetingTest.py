import unittest

import boto3

from conversation.ConversationManager import ConversationManager
from conversation.states.SizeNoPrefCentralBudgetCheapState import SizeNoPrefCentralBudgetCheapState
from conversation.states.SizeYesPrefCentralBudgetCheapState import SizeYesPrefCentralBudgetCheapState
from conversation.states.SizeYesPrefFrontBudgetUnknownState import SizeYesPrefFrontBudgetUnknownState
from conversation.states.SizeYesPrefUnknownBudgetUnknownState import SizeYesPrefUnknownBudgetUnknownState
from resources import config


from theatre.bookings import Chain
from theatre.bookings.Availability import Availability
from theatre.layout.TheatreLoader import load_theatre

client = boto3.client('lexv2-runtime',
                      aws_access_key_id=config.aws_access_key_id,
                      aws_secret_access_key=config.aws_secret_access_key,
                      region_name=config.region)


# availability, client, qualifiers, stage):
stage, seats = load_theatre("../resources/TestStage.csv", "../resources/TestSeats.csv")
chains = Chain.calculate_chains(seats)
availability = Availability(chains, stage)


class Testing(unittest.TestCase):

    def setUp(self):
        self.conversation_manager = ConversationManager(availability, client, None, None)

    def test_greetStatePrompt(self):
        self.assertEqual("Hi! I'm Tabitha the TicketBot. How can I help you today?",
                         self.conversation_manager.get_next_prompt())

    def test_transitiontoSizeNoPrefCentralBudgetCheapState(self):
        self.conversation_manager.update_with_input("I want some cheap seats in the centre")
        self.assertEqual(SizeNoPrefCentralBudgetCheapState.__name__, self.conversation_manager.current_state.__class__.__name__)

    def test_transitiontoSizeYesPrefFrontBudgetUnknownState(self):
        self.conversation_manager.update_with_input("Can I have seats at the front for 2")
        self.assertEqual(SizeYesPrefFrontBudgetUnknownState.__name__, self.conversation_manager.current_state.__class__.__name__)

    def test_transitiontoSizeYesPrefUnknownBudgetUnknownState(self):
        self.conversation_manager.update_with_input("Can I buy three tickets?")
        self.assertEqual(SizeYesPrefUnknownBudgetUnknownState.__name__, self.conversation_manager.current_state.__class__.__name__)

    def test_transitiontoSizeYesPrefCentralBudgetCheapState(self):
        self.conversation_manager.update_with_input("I want cheap central tickets for five")
        self.assertEqual(SizeYesPrefCentralBudgetCheapState.__name__, self.conversation_manager.current_state.__class__.__name__)


if __name__ == '__main__':
    unittest.main()
