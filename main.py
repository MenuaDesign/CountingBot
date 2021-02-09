import discord
import os
client = discord.Client()
@client.event
async def on_ready():
    print("Logged {0.user}\nReady".format(client))
CountLast = 1
Author_last = None
Author_current = None
@client.event
async def on_message(message):
    try:
        global CountLast
        global Author_last

        msg = await message.channel.fetch_message('807740947290128395')
        print(msg)
        Author_current = message.author.id
        channelid = (806265386981916715)
        if message.channel.id == channelid:
            if Author_current == Author_last:
                await message.delete()
                return
            if int(message.content) == CountLast + 1:
                print("------------------------")
                print(CountLast)
                print("-----------")
                CountLast += 1
                print(CountLast)
                print("------------------------")
                Author_last = message.author.id
                return
            elif int(message.content) != CountLast + 1:
                await message.delete()
                return
    except ValueError:
        await message.delete()
client.run('ODA2MjcwNjcwNDQyMDcwMDU2.YBnAEw.cphNfm4URwKBmeuW9jSbGKbMW4A')