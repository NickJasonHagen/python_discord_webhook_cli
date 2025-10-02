import requests
import argparse
def send_message(webhook_url, content):
    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        "content": content
    }

    response = requests.post(webhook_url, json=payload, headers=headers)

    if response.status_code == 204:
        print("Message sent successfully")
    elif response.status_code == 422:
        print("Invalid request data")
    else:
        print(f"Error sending message: {response.text}")

# get the arguments from the cli
parser = argparse.ArgumentParser(description='Send a message to a Discord webhook')
parser.add_argument('--webhook', required=True, help='Discord webhook URL')
parser.add_argument('--content', required=True, help='Message content')
args = parser.parse_args()
webhook_url = args.webhook
content = args.content
#run the call 
send_message(webhook_url, content)
