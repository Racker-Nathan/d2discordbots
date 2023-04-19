from discord import SyncWebhook
import requests
import os
event = []
context = []

TERRORZONEURL = "https://d2runewizard.com/api/terror-zone"
D2RW_TOKEN = os.environ.get('D2RUNEWIZARDTOKEN')
CONTACT = os.environ.get('CONTACT')
PARAMETERS = {'token': D2RW_TOKEN}
HEADERS = {'D2R-Contact': CONTACT, 'D2R-Platform': 'Discord', 'D2R-Repo': 'https://github.com/Racker-Nathan/d2discordbots'}
WEBHOOK = 'https://discord.com/api/webhooks/1097987262349848596/IZecxSYb99YBUnUYeMpmS2NHZRm4lm6FIwYn-DcGMEGdHFwDW6ny1K_2wzVYu075scWS'

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

lambda_handler(event, context)