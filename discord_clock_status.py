import requests
from datetime import datetime
import time

print(f"Started at {datetime.now()}")
headers = {
    #replace <token> with the token of your discord account
    "authorization": "<token>",
    "content-type": "application/json",
}

count = 0
clockEmojis = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛", "🕜", "🕝", "🕞", "🕟", "🕠", "🕡", "🕢", "🕣", "🕤", "🕥", "🕦", "🕧"]

while True:
    currentTime = datetime.now().strftime("%I:%M %p")
    if currentTime[0] == "0":
        currentTime = currentTime[1:]
    #replace GMT + 3 with whatever timezone you are in.
    text = f"{currentTime} GMT+3"
    emoji = clockEmojis[count]
    if count >= 23:
        count = 0
    else:
        count += 1
    payload = {"custom_status": {"text": text, "emoji_name": emoji}}
    response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers = headers, json = payload)
    time.sleep(0.6)
