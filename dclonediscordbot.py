import requests
import json
import boto3
import os
import discord
from datetime import datetime

##########
##Config##
##########

#AWS API Calls
s3 = boto3.client('s3')
DISCORD_TOKEN=os.environ.get('discordtoken')

#diablo2.io API Reference - https://diablo2.io/forums/diablo-clone-uber-diablo-tracker-public-api-t906872.html
PARAMETERS = {
    "region": os.environ.get('region'), #Americas
    "ladder": os.environ.get('ladder'), #Ladder
    "hc": os.environ.get('hc') #Softcore
}

#Source of the query, for this we're using the Americas, Softcore, Ladder set by the environmental variables
SOURCE = requests.get("https://diablo2.io/dclone_api.php?", params=PARAMETERS)



#############
##Functions##
#############

#Format response into readable json - used for troubleshooting.  Add function to main run with the json query
def formatresponse(SOURCE):
    FORMATTEDRESPONSE = json.dumps(SOURCE.json(), sort_keys=True, indent=4)
    print(FORMATTEDRESPONSE)

def d2clonestatus(SOURCE):
    statusnumber = SOURCE[0]['progress']
    time = datetime.fromtimestamp(int(SOURCE[0]['timestamped']))
    if statusnumber == "3":
        statusmessage = str(time) + " - Diablo is doing things bad"
        d2clonemessage(statusmessage)
    else:
        print("don't got it")


def d2clonemessage(statusmessage):
    return

def checkbackend():
    return

#Main run process
def main(SOURCE):
    d2clonestatus(SOURCE.json())
    #print(SOURCE.json())
    #formatresponse(SOURCE)

#Initiates the code
main(SOURCE)