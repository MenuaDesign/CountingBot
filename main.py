import discord
import os
client = discord.Client()
@client.event
async def on_ready():
    print("Logged {0.user}\nReady".format(client))
Count = 0
Author_last = None
Author_current = None
@client.event
async def on_message(message):
    try:
        global Count
        global Author_last
        Author_current = message.author.id
        channelid = (806265386981916715)
        if Author_current == Author_last:
            await message.delete()
            return
        if message.channel.id == channelid:
            if int(message.content) == Count + 1:
                Count += 1
                Author_last = message.author.id
                return
            elif int(message.content) != Count + 1:
                await message.delete()
                return
    except ValueError:
        await message.delete()
client.run(os.environ['TOKEN'])