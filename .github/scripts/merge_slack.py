import json
import requests
import os

my_variable = os.environ['MY_VARIABLE']

# Set the webhook_url to the one provided by Slack when you create the webhook at https://my.slack.com/services/new/incoming-webhook/
webhook_url = f'{my_variable}'

# Create your message
message = {'text': 'user requested the merge to master branch!'}

# Send the message to Slack
response = requests.post(
    webhook_url, data=json.dumps(message),
    headers={'Content-Type': 'application/json'}
)

# Check the response
if response.status_code != 200:
    raise ValueError(
        f'Request to slack returned an error {response.status_code}, the response is:\n{response.text}'
    )
