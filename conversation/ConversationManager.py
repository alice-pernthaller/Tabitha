import random

from botocore.exceptions import BotoCoreError

import conversation.intents.CentralCheapIntent as CentralCheapIntent
import conversation.intents.CentralIntent as CentralIntent
import conversation.intents.CheapIntent as CheapIntent
import conversation.intents.ChooseSectionByNameIntent as ChooseSectionByNameIntent
import conversation.intents.ChooseSectionByPriceIntent as ChooseSectionByPriceIntent
import conversation.intents.FallbackIntent as FallbackIntent
import conversation.intents.FrontCheapIntent as FrontCheapIntent
import conversation.intents.FrontIntent as FrontIntent
import conversation.intents.GoodViewCheapIntent as GoodViewCheapIntent
import conversation.intents.GoodViewIntent as GoodViewIntent
import conversation.intents.SizeCentralCheapIntent as SizeCentralCheapIntent
import conversation.intents.SizeCentralIntent as SizeCentralIntent
import conversation.intents.SizeCheapIntent as SizeCheapIntent
import conversation.intents.SizeFrontCheapIntent as SizeFrontCheapIntent
import conversation.intents.SizeFrontIntent as SizeFrontIntent
import conversation.intents.SizeGoodViewCheapIntent as SizeGoodViewCheapIntent
import conversation.intents.SizeGoodViewIntent as SizeGoodViewIntent
import conversation.intents.SizeIntent as SizeIntent
from conversation.Session import Session
from conversation.states.GreetingState import GreetingState
from theatre import my_constants

intent_builders = {"SizeFrontCheap": SizeFrontCheapIntent,
                   "FrontCheap": FrontCheapIntent,
                   "CommunicatePartySize": SizeIntent,
                   "ChooseSectionByPrice": ChooseSectionByPriceIntent,
                   "ChooseSectionByName": ChooseSectionByNameIntent,
                   "Front": FrontIntent,
                   "Central": CentralIntent,
                   "GoodView": GoodViewIntent,
                   "SizeCentralCheap": SizeCentralCheapIntent,
                   "SizeGoodViewCheap": SizeGoodViewCheapIntent,
                   "GoodViewCheap": GoodViewCheapIntent,
                   "CentralCheap": CentralCheapIntent,
                   "SizeGoodView": SizeGoodViewIntent,
                   "SizeCentral": SizeCentralIntent,
                   "SizeFront": SizeFrontIntent,
                   "SizeCheap": SizeCheapIntent,
                   "Size": SizeIntent,
                   "Cheap": CheapIntent,
                   "FallbackIntent": FallbackIntent}


def _resolve_intent_name(response):
    intent = response['sessionState']['intent']
    name = intent['name']
    return name


# the conversation manager integrates the Lex bot with the conversation model
class ConversationManager:
    def __init__(self, availability, client, qualifiers, stage):
        self.availability = availability
        self.session = Session()
        self.qualifiers = qualifiers
        self.stage = stage

        self.current_state = GreetingState(self.session, self.qualifiers, self.stage)

        self.sessionId = str(random.randint(1, 10000000))
        self.client = client

        self.lex_error = False

    # gets the next prompt from the current state and returns it to the GUI
    def get_next_prompt(self):
        if self.lex_error:  # error handling when connection to Lex is broken
            next_prompt = "Unexpected error when talking to lex."

        else:
            error_part = ""
            if self.current_state.session.check_and_clear_error():
                error_part = "I'm sorry, I don't understand. Please try again.\n"

            if self.availability.calculate_remaining_seats() == 0:
                return "The theatre is full."

            # asks the current state for what to say next
            next_prompt = error_part + self.current_state.get_next_prompt(self.availability)

        print(f"Tabitha: {next_prompt}")
        return next_prompt

    def _get_active_contexts(self):
        active_contexts = []
        for flag in self.current_state.context_tags:
            active_contexts.append(
                {'name': flag, 'timeToLive': {'timeToLiveInSeconds': 3600, 'turnsToLive': 1}, 'contextAttributes': {}})
        return active_contexts

    def _process_response(self, response):
        intent_name = _resolve_intent_name(response)

        builder = intent_builders[intent_name]
        intent = builder.unmarshall(response)

        self.current_state = self.current_state.transition(intent)
        if self.current_state.is_terminal:
            self.availability.remove_selection_from_availability(self.session.chosen_selection)

    def update_with_input(self, input):
        active_contexts = self._get_active_contexts()

        try:
            # sends the user input to Lex, which matches it to an intent.
            response = self.client.recognize_text(botId=my_constants.botId,
                                                  botAliasId=my_constants.botAliasId,
                                                  localeId=my_constants.localeId,
                                                  sessionId=self.sessionId,
                                                  text=input,
                                                  sessionState={'activeContexts': active_contexts})
            # then unmarshalls the response into an Intent
            self._process_response(response)

        except BotoCoreError:  # error handling when there is a Lex-related error
            self.lex_error = True
