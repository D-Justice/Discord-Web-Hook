import json
import requests
import pprint
#A99BA5E1EEDC4073B16C4691209AFE1F
#76561198054487316
headers = {'TRN-Api-Key': '8ea28dd0-b8e9-4449-a66b-9531310dd37e'}
WebHook = "https://discordapp.com/api/webhooks/820460456027750476/Ojm4aWrFAvFCzCiFzyEMJWQgS8pY_0N4idfFq7jy11djbhnbOUDWYPSnG5QwSIg3G6iv"
apiURL = requests.get("https://public-api.tracker.gg/v2/csgo/standard/profile/steam/76561198054487316", headers = headers)

def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
#jprint(apiURL.json())

userName = apiURL.json()['data']['platformInfo']['platformUserHandle']
bombsDef = apiURL.json()['data']['segments'][0]['stats']['bombsDefused']['displayValue']
bombsPlanted = apiURL.json()['data']['segments'][0]['stats']['bombsPlanted']['displayValue']
deaths = apiURL.json()['data']['segments'][0]['stats']['deaths']['displayValue']
kd = apiURL.json()['data']['segments'][0]['stats']['kd']['displayValue']
kills = apiURL.json()['data']['segments'][0]['stats']['kills']['displayValue']
losses = apiURL.json()['data']['segments'][0]['stats']['losses']['displayValue']
wins = apiURL.json()['data']['segments'][0]['stats']['wins']['displayValue']
winLoss = apiURL.json()['data']['segments'][0]['stats']['wlPercentage']['displayValue']
matches = apiURL.json()['data']['segments'][0]['stats']['matchesPlayed']['displayValue']


hookData = {
    "username": "WebHook",
    "content": "CSGO player stats for {}".format(userName),
    "embeds": [
        {
            "author": {
                "name": "Hook BOY"
            },
            "title": "Kills:",
            "color": 15258703,
            "fields": [
                {
                "name": "",
                "value": 'kills',
                "inline": True
                
                }
            
            ]
        }
    ]
}

send = requests.post(WebHook, json = hookData)
try:
    send.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Delivered successfully, code {}.".format(send.status_code))
