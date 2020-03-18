import sys
from slack import WebClient

def start_bot():
    token = 'xoxb-2661557430-892686613618-Xo01ZMpms9mULDZmk1udfVbk'
    slack_client = WebClient(token)
    #slack_client.connect()
    #slack_client.chat_postMessage(channel="#chiba-daq", text="Slow Monitoring Online")
    return slack_client

def send_message(msg):
    slack_client = start_bot()
    slack_client.chat_postMessage(channel="#chiba-daq", text=msg)

def send_warning(msg, shifter_id="UK5NBFEGZ"):
    slack_client = start_bot()
    slack_client.chat_postMessage(channel="#chiba-daq", text=msg)
    slack_client.chat_postMessage(channel=shifter_id, text=msg)

def send_critical(msg, shifter_id="UK5NBFEGZ", admin_id="UK5NBFEGZ"):
    slack_client = start_bot()
    slack_client.chat_postMessage(channel="#chiba-daq", text=msg)
    slack_client.chat_postMessage(channel=shifter_id, text=msg)
    slack_client.chat_postMessage(channel=admin_id, text=msg)

def push_slow_mon(up_file, title):
    slack_client = start_bot()
    with open(up_file, 'rb') as file_content:
        slack_client.files_upload(channels="#chiba-daq", file=file_content, title=title)
