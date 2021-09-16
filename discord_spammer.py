import requests

token = #add your discord token here
channelID = #put id of channel that you want to spam over here
headers = {"authorization": token}

#make a file called text.txt in the same directory with the text you want to spam
file = open("text.txt", "r")
lines = file.readlines()

for line in lines:
    requests.post(f"https://discord.com/api/v9/channels/{channelID}/messages", headers = headers, json = {"content": line})
