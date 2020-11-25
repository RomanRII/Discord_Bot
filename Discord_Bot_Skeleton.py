import discord

#Grab Token from https://discordapp.com/developers/applications/ ; Select the bot you want to use; then Settings > Bot > Build-A-Bot > Token [Grab or Generate a token]
#                                                                                                                                           and paste in the string below
TOKEN = ' '

#Client Connection Class
class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == client.user:
            return

print("Successfully logged in")

#Connection Attempt Start
print('[!] Attempting to conenct to server.')
client = MyClient()
client.run(TOKEN)
#Connection Attempt End

