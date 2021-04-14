import sys
from slack import WebClient
from chiba_slackbot import info

def start_bot():
    token = info.token
    slack_client = WebClient(token)
    #slack_client.connect()
    #slack_client.chat_postMessage(channel="#chiba-daq", text="Slow Monitoring Online")
    return slack_client

def send_message(msg):
    slack_client = start_bot()
    slack_client.chat_postMessage(channel=info.channel, text=msg)

def send_warning(msg, shifter_id=info.shifter_id, 
                 expert_id=info.expert_id,
		 admin_id=info.admin_id):
    slack_client = start_bot()
    slack_client.chat_postMessage(channel=info.channel, text=msg)
    slack_client.chat_postMessage(channel=shifter_id, text=msg)
    slack_client.chat_postMessage(channel=expert_id, text=msg)
    slack_client.chat_postMessage(channel=admin_id, text=msg)

def send_critical(msg, shifter_id=info.shifter_id, expert_id1=info.expert_id, 
                  expert_id2=info.shifter_idbkp, admin_id=info.admin_id):
    slack_client = start_bot()
    slack_client.chat_postMessage(channel=info.channel, text=msg)
    slack_client.chat_postMessage(channel=shifter_id, text=msg)
    slack_client.chat_postMessage(channel=expert_id1, text=msg)
    slack_client.chat_postMessage(channel=expert_id2, text=msg)
    slack_client.chat_postMessage(channel=admin_id, text=msg)

def push_slow_mon(up_file, title):
    slack_client = start_bot()
    with open(up_file, 'rb') as file_content:
        slack_client.files_upload(channels=info.channel, file=file_content, title=title)
