import json
import requests
import pprint
import auth

headers = {'TRN-Api-Key': '{}'.format(auth.authenticate)}
user = input("Enter players Steam name, id, or URL: ")
WebHook = "https://discordapp.com/api/webhooks/820459719856357417/yWgUi6Kefaq735ZExao5OG9h0dnPyXMAoMR1anBDjRBH-ZJG3TMd5dqUKGfR-kynB8XI"
apiURL = requests.get("https://public-api.tracker.gg/v2/csgo/standard/profile/steam/{}".format(user), headers = headers)

def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

try:
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
except:
    print("No user by this name found. Try again")
    quit()

hookData = {
  "username": "Webhook",
  "avatar_url": "https://cdn.ndtv.com/tech/gadgets/cs_go_header_valve.jpg",
  "embeds": [
    {
      "author": {
        "name": "STAT BOY",
        "url": "https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/",
        "icon_url": "https://cdn.mos.cms.futurecdn.net/5zHA4DXhWdQfiyaBKXeQyg.jpg"
      },
      "title": "CS:GO STATS FOR: {}".format(userName),
      "fields": [
        {
          "name": "Bombs:",
          "value": "Defuses: {}\n Plants: {}".format(bombsDef, bombsPlanted),
          "inline": True
        },
        {
          "name": "Kills:".format(kills),
          "value": "Kills: {}\nK/D: {}".format(kills,kd),
          "inline": True
        },
        {
            "name": "Out of {} matches:".format(matches),
            "value": "{} had:\n{} wins\n{} losses\nWith a winrate of {}".format(userName,wins,losses,winLoss),
            "inline": True
        },
        {
            "name": "Deaths",
            "value": "You have died {} times".format(deaths),
            "inline": True
        }
        
      ],
      "image": {
          "url": "https://cdn.ndtv.com/tech/gadgets/cs_go_header_valve.jpg"
      },
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
