from discord import SyncWebhook
import requests
import os

TERRORZONEURL = "https://d2runewizard.com/api/terror-zone"
D2RW_TOKEN = os.environ.get('D2RUNEWIZARDTOKEN')
CONTACT = os.environ.get('CONTACT')
PARAMETERS = {'token': D2RW_TOKEN}
HEADERS = {'D2R-Contact': CONTACT, 'D2R-Platform': 'Discord', 'D2R-Repo': 'https://github.com/Racker-Nathan/d2discordbots'}
WEBHOOK = os.environ.get('WEBHOOK')

def webhook():
    webhook = SyncWebhook.from_url(WEBHOOK)
    return webhook

def terrorzone(webhook):
    SOURCE = requests.get(TERRORZONEURL, params=PARAMETERS, headers=HEADERS, timeout=10)
    MESSAGE = '**Terror Zone has changed**\nCorrupted Tremors have struck **' + SOURCE.json()['terrorZone']['zone'] + '**\n\nReported on d2runewizard.com\n\n<@&1097997443330752574>'
    webhook.send(MESSAGE)
    print(MESSAGE)

def main(event):
    webhooksetup = webhook()
    terrorzone(webhooksetup)

def lambda_handler(event, context):
    main(event)