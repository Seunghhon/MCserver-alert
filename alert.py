from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import load_dotenv
import os
import time
from pathlib import Path
import datetime

load_dotenv()

webhook_url = [os.getenv('WEBHOOK'), os.getenv('WEBHOOK2')]
log_path = Path(os.getenv('LOGPATH'))

if not log_path.exists():
    print("Log file does not exist")
    exit()

last_position = 0
def send_webhook_message(description, title, webhook_url):
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title="", description=description, color='242424')
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()

def check_minecraft_server(description, title):
    global last_position
    while True:
        # Open the log file in read mode and seek to the last known position
        with open(log_path, 'r') as f:
            
            f.seek(last_position)
            console_log = f.read()
            
            if "Async Chat Thread" not in console_log:
                
            # Detect player joins
                if "joined the game" in console_log:
                    player = console_log.split("joined the game")[0].split()[-1]
                    description = f'{player} has joined the game!'
                    title = "Minecraft Server Alert"
                    for url in webhook_url:
                        send_webhook_message(description, title, url)

                # Detect player leaves
                if "left the game" in console_log:
                    player = console_log.split("left the game")[0].split()[-1]
                    description = f'{player} has left the game!'
                    title = "Minecraft Server Alert"
                    send_webhook_message(description, title, webhook_url)

            # Update the last position in the log file
            last_position = f.tell()

            # Wait for a few seconds before checking the log file again
            time.sleep(5)

check_minecraft_server(None, None)