import requests #dependency
from discord_webhook import DiscordWebhook

url = "https://discord.com/api/webhooks/1164075899369566250/-nWpkw79OA5NFeNyIB2wtxwY464mdFdxILLdLn640l9xM-rEiRl83fvT2UQkblBiPrJD" #webhook url, from here: https://i.imgur.com/f9XnAew.png

#for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
data = {
    "content" : "서버 상태 알림!",
    "username" : "노예봇",
}

#leave this out if you dont want an embed
#for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
def send_webhook_message(description, title):
    data["embeds"] = [
        {
            "description" : description,
            "title" : title,
            "color" : 123456,
        }
    ]

result = requests.post(url, json = data)
#server_api_url = "https://api.mcsrvstat.us/3/mc.seunghoon.me"

def check_minecraft_server():
    while True:
        with open("server log file path") as f:
            console_log = f.read()
            if "joined the game" in console_log:
                player = console_log.split("joined the game")[0].split(" ")[-1]
                description = f'{player} has joined the game!'
                title = "Minecraft Server Alert"
                send_webhook_message(description, title)
        
        

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))