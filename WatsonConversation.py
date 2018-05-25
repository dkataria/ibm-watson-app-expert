import json
from watson_developer_cloud import ConversationV1
'''
This code has been adapted from IBM Watson's Github page (https://github.com/watson-developer-cloud/python-sdk)
and modified to be used with our application.
This program connects to Watson's Conversation service enabling users to use the service via
console.

'''

# credentials for connecting to workspace
conversation = ConversationV1(
    username='275a20b8-448d-42f7-b764-93f47b864c3b',
    password='FG2A45ggMStn',
    version='2016-09-20')
workspace_id = '18b0f85d-4ad8-4141-93e1-86f6d0349f83'



# Watson Conversation service logic
keepRunning = True
counter = 0

response = conversation.message(workspace_id=workspace_id, message_input={
        'text': 'initializing conversation'})
print(response['output']['text'][0])
print('Keep shooting queries after Watson replies to you. Watson is waiting for your input')
print('Type in STOP any time to stop talking to Watson')


response = conversation.message(workspace_id=workspace_id, message_input={
        'text': 'initializing conversation again'},context = response['context'])

while keepRunning:
    userInput = str(input())
    if userInput.lower() == 'stop':
        keepRunning = False
        print('Thank you for talking to me. Hope I was helpful')
    else:
        response = conversation.message(workspace_id=workspace_id, message_input={
        'text': userInput}, context = response['context'])
        print(response['output']['text'][0])
