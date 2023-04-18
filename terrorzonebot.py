import discord
import json
import requests
import os

URL = "https://d2runewizard.com/api/terror-zone"
TOKEN = os.environ.get('D2RUNEWIZARDTOKEN')


SOURCE=requests.get(URL, headers={'D2R-Contact': 'dakkoth@gmail.com', 'D2R-Platform': 'Discord', 'D2R-Repo': 'None yet, testing base code', 'token': 'N8QV55pTS_IcUve9hFTVJw'})
print(SOURCE.json())