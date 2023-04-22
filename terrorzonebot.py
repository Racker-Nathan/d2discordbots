from discord import SyncWebhook
import requests
import boto3
import os
import json

TERRORZONEURL = "https://d2runewizard.com/api/terror-zone"
D2CLONEURL = "https://d2runewizard.com/api/diablo-clone-progress/all"
D2RW_TOKEN = os.environ.get('D2RUNEWIZARDTOKEN')
CONTACT = os.environ.get('CONTACT')
PARAMETERS = {'token': D2RW_TOKEN}
HEADERS = {'D2R-Contact': CONTACT, 'D2R-Platform': 'Discord', 'D2R-Repo': 'https://github.com/Racker-Nathan/d2discordbots'}
WEBHOOK = os.environ.get('WEBHOOK')
S3 = boto3.client('s3')
BUCKETNAME = os.environ.get('BUCKETNAME')
event = {'event': 'clone'}

def webhook():
    webhook = SyncWebhook.from_url(WEBHOOK)
    return webhook

def terrorzone(webhook):
    SOURCE = requests.get(TERRORZONEURL, params=PARAMETERS, headers=HEADERS, timeout=10)
    MESSAGE = '**Terror Zone has changed**\nCorrupted Tremors have struck **' + SOURCE.json()['terrorZone']['zone'] + '**\n\nReported on d2runewizard.com\n\n<@&1097997443330752574>'
    webhook.send(MESSAGE)
    print(MESSAGE)


def d2cloneprogress(webhook):
    INFO = requests.get(D2CLONEURL, params=PARAMETERS, headers=HEADERS, timeout=10)
    print(INFO.json())
    for server in INFO.json()['servers']:
        if server['server'] == 'ladderSoftcoreAmericas':
            progress = server['progress']
            statusmessage = server['message']
            d2clonestatus(webhook, progress, statusmessage)
        else:
            continue

def d2clonestatus(webhook, progress, statusmessage):
    object = S3.get_object(
        Bucket = BUCKETNAME,
        Key = 'd2clonestatus'
    )
    currentstatus = json.loads(object['Body'].read())
    if str(progress) != str(currentstatus):
        MESSAGE = "**Diablo Clone Update for Softcore Ladder Americas**\n\n**Current Progress:** " + str(progress) + "\n**Current Status Message:** " + statusmessage
        webhook.send(MESSAGE)
        S3.put_object(
            Bucket=BUCKETNAME,
            Key = 'd2clonestatus',
            Body = str(progress)
        )
    else:
        print('Status is the same, exiting')
        return

#Input should be {'event': 'terror'} or {'event': 'clone'} - set in eventbridge
def main(event):
    webhooksetup = webhook()
    if event['event'] == "terror":
        terrorzone(webhooksetup)
    elif event['event'] == "clone":
        d2cloneprogress(webhooksetup)
    else:
        print("Error, incorrect input")
        exit(1)

def lambda_handler(event, context):
    main(event)