import discord
import os
client = discord.Client()
CountLast = 0
Author_last = None
Author_current = None
@client.event
async def on_ready():
    global CountLast
    global Author_last
    print("Logged {0.user}\nReady".format(client))
    channelid = (806265386981916715)
    object = await client.get_channel(channelid).history(limit=1).flatten()
    CountLast = int(object[0].content)
    Author_last = object[0].author.id
    print(CountLast)

@client.event
async def on_message(message):
    global CountLast
    global Author_last
    Author_current = message.author.id
    channelid = (806265386981916715)
    try:
        if message.channel.id == channelid:
            if Author_current == Author_last:
                print("Author can't write again")
                await message.delete()
                return
            if int(message.content) == CountLast + 1:
                print("------------------------")
                print(CountLast + 1)
                print("-----------")
                CountLast += 1
                print(CountLast + 1)
                print("------------------------")
                Author_last = message.author.id
                return
            elif int(message.content) != CountLast + 1:
                print("Wrong next number")
                await message.delete()
                return
    except ValueError:
        print('Except error Value')
        await message.delete()
client.run('ODA2MjcwNjcwNDQyMDcwMDU2.YBnAEw.cphNfm4URwKBmeuW9jSbGKbMW4A')