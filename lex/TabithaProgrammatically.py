# the following code is run ONCE to create the bot and its intents


import time

import boto3

from resources import config


# functions to create the bot
def create_bot(client):
    response = client.create_bot(
        botName='TabithaTheTicketBot',
        roleArn='arn:aws:iam::214384484131:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots_ALICE',
        dataPrivacy={'childDirected': False},
        idleSessionTTLInSeconds=3600)
    return response


def create_bot_locale(client, bot_id, bot_version, locale_id):
    response = client.create_bot_locale(
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id,
        nluIntentConfidenceThreshold=0.4)
    return response


# intents are created and then updated with slots (required variables) and sample utterances
def create_GoodView_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='GoodView',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_GoodView_intent(client, intent_id, intent_name, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        # the user can say any of the following utterances to trigger the intent:
        sampleUtterances=[{'utterance': 'I want the best seats'}, {'utterance': 'Can I buy the best tickets'},
                          {'utterance': 'good view'}, {'utterance': 'I want a good view'}],
        inputContexts=[{'name': 'NoPreference'}],  # an intent can only be matched to if all context tags are met
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_Central_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='Central',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_Central_intent(client, intent_id, intent_name, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': 'I want to sit in the middle'},
                          {'utterance': 'Can I buy tickets near the middle'},
                          {'utterance': 'centre'}, {'utterance': 'middle'}, {'utterance': 'middle please'}],
        inputContexts=[{'name': 'NoPreference'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_Front_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='Front',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_Front_intent(client, intent_id, intent_name, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': 'I want to sit at the front'}, {'utterance': 'Can I buy seats at the front'},
                          {'utterance': 'front'}],
        inputContexts=[{'name': 'NoPreference'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_CentralCheap_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='CentralCheap',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_CentralCheap_intent(client, intent_id, intent_name, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': 'I want some cheap seats in the centre'},
                          {'utterance': 'Can I have cheap tickets near the middle'}],
        inputContexts=[{'name': 'NoPreference'}, {'name': 'NoBudget'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_Cheap_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='Cheap',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_Cheap_intent(client, intent_id, intent_name, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': 'I want cheap tickets'}, {'utterance': 'Can I buy inexpensive seats'},
                          {'utterance': "I don't have much to spend"}],
        inputContexts=[{'name': 'NoBudget'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_GoodViewCheap_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='GoodViewCheap',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_GoodViewCheap_intent(client, intent_id, intent_name, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': 'I want some cheap seats with a good view'},
                          {'utterance': 'Can I have the best cheap seats please'}],
        inputContexts=[{'name': 'NoPreference'}, {'name': 'NoBudget'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_FrontCheap_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='FrontCheap',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_FrontCheap_intent(client, intent_id, intent_name, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': 'I want some cheap seats at the front'},
                          {'utterance': 'Can I have some cheap tickets near the front'}],
        inputContexts=[{'name': 'NoPreference'}, {'name': 'NoBudget'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_SizeFrontCheap_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='SizeFrontCheap',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_SizeFrontCheap_intent(client, intent_id, intent_name, slot_id, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': 'I want {PartySize} cheap tickets at the front'},
                          {'utterance': 'I want cheap tickets at the front for {PartySize}'}],
        slotPriorities=[{'priority': 1, 'slotId': slot_id}],
        inputContexts=[{'name': 'NoParty'}, {'name': 'NoPreference'}, {'name': 'NoBudget'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_Size_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='Size',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_Size_intent(client, intent_id, intent_name, slot_id, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': '{PartySize}'}, {'utterance': 'Can I buy {PartySize} tickets?'},
                          {'utterance': 'I want {PartySize} seats'}, {'utterance': 'Can I have {PartySize} seats'},
                          {'utterance': 'I want {PartySize} tickets'}],
        slotPriorities=[{'priority': 1, 'slotId': slot_id}],
        inputContexts=[{'name': 'NoPartySize'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_SizeCheap_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='SizeCheap',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_SizeCheap_intent(client, intent_id, intent_name, slot_id, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': 'I want cheap seats for {PartySize}'},
                          {'utterance': 'Can I buy {PartySize} cheap tickets'}],
        slotPriorities=[{'priority': 1, 'slotId': slot_id}],
        inputContexts=[{'name': 'NoPartySize'}, {'name': 'NoPreference'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_SizeGoodView_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='SizeGoodView',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_SizeGoodView_intent(client, intent_id, intent_name, slot_id, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': 'I want the best {PartySize} tickets you have'},
                          {'utterance': 'Can I buy good seats for {PartySize}'}],
        slotPriorities=[{'priority': 1, 'slotId': slot_id}],
        inputContexts=[{'name': 'NoPartySize'}, {'name': 'NoPreference'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_SizeFront_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='SizeFront',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_SizeFront_intent(client, intent_id, intent_name, slot_id, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': 'I want {PartySize} tickets at the front'},
                          {'utterance': 'Can I have seats at the front for {PartySize}'}],
        slotPriorities=[{'priority': 1, 'slotId': slot_id}],
        inputContexts=[{'name': 'NoPartySize'}, {'name': 'NoPreference'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_SizeGoodViewCheap_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='SizeGoodViewCheap',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_SizeGoodViewCheap_intent(client, intent_id, intent_name, slot_id, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': 'I want {PartySize} cheap tickets with a good view'},
                          {'utterance': 'I want the best {PartySize} tickets that are cheap'}],
        slotPriorities=[{'priority': 1, 'slotId': slot_id}],
        inputContexts=[{'name': 'NoPartySize'}, {'name': 'NoBudget'}, {'name': 'NoPreference'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_SizeCentralCheap_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='SizeCentralCheap',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_SizeCentralCheap_intent(client, intent_id, intent_name, slot_id, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': 'I want {PartySize} cheap tickets near the centre'},
                          {'utterance': 'I want cheap central tickets for {PartySize}'}],
        slotPriorities=[{'priority': 1, 'slotId': slot_id}],
        inputContexts=[{'name': 'NoPartySize'}, {'name': 'NoBudget'}, {'name': 'NoPreference'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_SizeCentral_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='SizeCentral',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_SizeCentral_intent(client, intent_id, intent_name, slot_id, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': 'I want {PartySize} tickets in the centre'},
                          {'utterance': 'Can I have seats near the middle for {PartySize} ?'},
                          {'utterance': 'I want {PartySize} tickets in the middle'},
                          {'utterance': 'I want {PartySize} central tickets'}],
        slotPriorities=[{'priority': 1, 'slotId': slot_id}],
        inputContexts=[{'name': 'NoPartySize'}, {'name': 'NoPreference'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_CommunicatePartySize_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='CommunicatePartySize',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_CommunicatePartySize_intent(client, intent_id, intent_name, slot_id, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': '{PartySize}'}, {'utterance': 'I want {PartySize} tickets'},
                          {'utterance': "I'd like {PartySize} tickets thank you"},
                          {'utterance': 'I would like {PartySize} tickets'},
                          {'utterance': 'Can I have {PartySize} seats please'},
                          {'utterance': 'I want to buy {PartySize} tickets'}],
        slotPriorities=[{'priority': 1, 'slotId': slot_id}],
        inputContexts=[{'name': 'AskedForPartySize'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_ChooseSectionByPrice_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='ChooseSectionByPrice',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_ChooseSectionByPrice_intent(client, intent_id, intent_name, slot_id, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': "I'll take the £ {Price} seats"}, {'utterance': "{Price}"},
                          {'utterance': '£ {Price}'}, {'utterance': 'I want the £ {Price} tickets'}],
        slotPriorities=[{'priority': 1, 'slotId': slot_id}],
        inputContexts=[{'name': 'SelectionsOffered'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_ChooseSectionByName_intent(client, bot_id, bot_version, locale_id):
    response = client.create_intent(
        intentName='ChooseSectionByName',
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def update_ChooseSectionByName_intent(client, intent_id, intent_name, slot_id, bot_id, bot_version, locale_id):
    response = client.update_intent(
        intentId=intent_id,
        intentName=intent_name,
        sampleUtterances=[{'utterance': "{SectionDescription}"}, {'utterance': "{SectionDescription} section please"},
                          {'utterance': "I'll take the {SectionDescription} seats"}],
        slotPriorities=[{'priority': 1, 'slotId': slot_id}],
        inputContexts=[{'name': 'SelectionsOffered'}],
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id)
    return response


def create_party_size_slot(client, intent_id):
    response = client.create_slot(
        slotName='PartySize',
        slotTypeId='AMAZON.Number',
        valueElicitationSetting={
            'defaultValueSpecification': {'defaultValueList': [{'defaultValue': 'Two'}]},
            'slotConstraint': 'Required',
            'promptSpecification': {'messageGroups': [{'message': {'plainTextMessage': {'value': ' '}}}],
                                    'maxRetries': 1}},
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id,
        intentId=intent_id)
    return response


def create_price_slot(client, intent_id):
    response = client.create_slot(
        slotName='Price',
        slotTypeId='AMAZON.Number',
        valueElicitationSetting={
            'defaultValueSpecification': {'defaultValueList': [{'defaultValue': '30'}]},
            'slotConstraint': 'Required',
            'promptSpecification': {'messageGroups': [{'message': {'plainTextMessage': {'value': ' '}}}],
                                    'maxRetries': 1}},
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id,
        intentId=intent_id)
    return response


def create_section_description_slot(client, intent_id, slot_type_id):
    response = client.create_slot(
        slotName='SectionDescription',
        slotTypeId=slot_type_id,
        valueElicitationSetting={
            'defaultValueSpecification': {'defaultValueList': [{'defaultValue': 'front central'}]},
            'slotConstraint': 'Required',
            'promptSpecification': {'messageGroups': [{'message': {'plainTextMessage': {'value': ' '}}}],
                                    'maxRetries': 1}},
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id,
        intentId=intent_id)
    return response


client = boto3.client('lexv2-models', aws_access_key_id=config.aws_access_key_id,
                      aws_secret_access_key=config.aws_secret_access_key, region_name=config.region)

# Create bot from scratch:
response = create_bot(client)
print(response)
time.sleep(5)
bot_id = response['botId']
bot_version = 'DRAFT'
locale_id = 'en_US'

create_bot_locale(client, bot_id, bot_version, locale_id)
time.sleep(5)

# Create intents:
intent_response = create_GoodView_intent(client, bot_id, bot_version, locale_id)
update_GoodView_intent(client, intent_response['intentId'], intent_response['intentName'], bot_id, bot_version, locale_id)

intent_response = create_Central_intent(client, bot_id, bot_version, locale_id)
update_Central_intent(client, intent_response['intentId'], intent_response['intentName'], bot_id, bot_version, locale_id)

intent_response = create_Front_intent(client, bot_id, bot_version, locale_id)
update_Front_intent(client, intent_response['intentId'], intent_response['intentName'], bot_id, bot_version, locale_id)

intent_response = create_Cheap_intent(client, bot_id, bot_version, locale_id)
update_Cheap_intent(client, intent_response['intentId'], intent_response['intentName'], bot_id, bot_version, locale_id)

intent_response = create_CentralCheap_intent(client, bot_id, bot_version, locale_id)
update_CentralCheap_intent(client, intent_response['intentId'], intent_response['intentName'], bot_id, bot_version, locale_id)

intent_response = create_GoodViewCheap_intent(client, bot_id, bot_version, locale_id)
update_GoodViewCheap_intent(client, intent_response['intentId'], intent_response['intentName'], bot_id, bot_version, locale_id)

intent_response = create_FrontCheap_intent(client, bot_id, bot_version, locale_id)
update_FrontCheap_intent(client, intent_response['intentId'], intent_response['intentName'], bot_id, bot_version, locale_id)

# the following intents need a 'PartySize' slot, ie they need the user to express a number
intent_response = create_Size_intent(client, bot_id, bot_version, locale_id)
slot_response = create_party_size_slot(client, intent_response['intentId'])
slot_id = slot_response['slotId']
update_Size_intent(client, intent_response['intentId'], intent_response['intentName'], slot_id, bot_id, bot_version, locale_id)

intent_response = create_SizeCheap_intent(client, bot_id, bot_version, locale_id)
slot_response = create_party_size_slot(client, intent_response['intentId'])
slot_id = slot_response['slotId']
update_SizeCheap_intent(client, intent_response['intentId'], intent_response['intentName'], slot_id, bot_id, bot_version, locale_id)

intent_response = create_SizeGoodView_intent(client, bot_id, bot_version, locale_id)
slot_response = create_party_size_slot(client, intent_response['intentId'])
slot_id = slot_response['slotId']
update_SizeGoodView_intent(client, intent_response['intentId'], intent_response['intentName'], slot_id, bot_id, bot_version, locale_id)

intent_response = create_SizeFront_intent(client, bot_id, bot_version, locale_id)
slot_response = create_party_size_slot(client, intent_response['intentId'])
slot_id = slot_response['slotId']
update_SizeFront_intent(client, intent_response['intentId'], intent_response['intentName'], slot_id, bot_id, bot_version, locale_id)

intent_response = create_SizeGoodViewCheap_intent(client, bot_id, bot_version, locale_id)
slot_response = create_party_size_slot(client, intent_response['intentId'])
slot_id = slot_response['slotId']
update_SizeGoodViewCheap_intent(client, intent_response['intentId'], intent_response['intentName'], slot_id, bot_id, bot_version, locale_id)

intent_response = create_SizeCentralCheap_intent(client, bot_id, bot_version, locale_id)
slot_response = create_party_size_slot(client, intent_response['intentId'])
slot_id = slot_response['slotId']
update_SizeCentralCheap_intent(client, intent_response['intentId'], intent_response['intentName'], slot_id, bot_id, bot_version, locale_id)

intent_response = create_SizeCentral_intent(client, bot_id, bot_version, locale_id)
slot_response = create_party_size_slot(client, intent_response['intentId'])
slot_id = slot_response['slotId']
update_SizeCentral_intent(client, intent_response['intentId'], intent_response['intentName'], slot_id, bot_id, bot_version, locale_id)

intent_response = create_SizeFrontCheap_intent(client, bot_id, bot_version, locale_id)
slot_response = create_party_size_slot(client, intent_response['intentId'])
slot_id = slot_response['slotId']
update_SizeFrontCheap_intent(client, intent_response['intentId'], intent_response['intentName'], slot_id, bot_id, bot_version, locale_id)

intent_response = create_CommunicatePartySize_intent(client, bot_id, bot_version, locale_id)
slot_response = create_party_size_slot(client, intent_response['intentId'])
slot_id = slot_response['slotId']
update_CommunicatePartySize_intent(client, intent_response['intentId'], intent_response['intentName'], slot_id, bot_id, bot_version, locale_id)

intent_response = create_ChooseSectionByPrice_intent(client, bot_id, bot_version, locale_id)
slot_response = create_price_slot(client, intent_response['intentId'])
slot_id = slot_response['slotId']
update_ChooseSectionByPrice_intent(client, intent_response['intentId'], intent_response['intentName'], slot_id, bot_id, bot_version, locale_id)


# a custom slot type to reflect the sections of the theatre
def create_section_description_slot_type(client, bot_id, bot_version, locale_id):
    response = client.create_slot_type(
        slotTypeName='SectionDescription',
        slotTypeValues=[{'sampleValue': {'value': 'front side'}}, {'sampleValue': {'value': 'front central'}},
                        {'sampleValue': {'value': 'centre far side'}}, {'sampleValue': {'value': 'centre'}},
                        {'sampleValue': {'value': 'side back'}}, {'sampleValue': {'value': 'back central'}}],
        valueSelectionSetting={'resolutionStrategy': 'TopResolution'},
        botId=bot_id,
        botVersion=bot_version,
        localeId=locale_id,
    )
    return response


response = create_section_description_slot_type(client, bot_id, bot_version, locale_id)
slot_type_id = response['slotTypeId']

intent_response = create_ChooseSectionByName_intent(client, bot_id, bot_version, locale_id)
slot_response = create_section_description_slot(client, intent_response['intentId'], slot_type_id)
slot_id = slot_response['slotId']
update_ChooseSectionByName_intent(client, intent_response['intentId'], intent_response['intentName'], slot_id, bot_id,
                                  bot_version, locale_id)

# client.build_bot_locale(botId=bot_id, botVersion=bot_version, localeId=locale_id)
