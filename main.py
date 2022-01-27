import discord
import secret_token

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('maro hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('maro deez'):
        await message.channel.send("Aidan Is Gay! We Are So Proud Of Aidan For Coming Out As Gay!")

    if message.content.startswith('maro pls'):
            await message.channel.send("OOBLOOBLBLBLABOBLBLWAOOOOOOOOOO")
            await message.channel.send("GULUUGOBOGLOOUGOUBOGOLOOGUBOGOBUOGBOOOLOBOGOO")
            await message.channel.send("Haaah... Hah... Haaah... Hooo...")
            await message.channel.send("glooogoboAOGOBIGOBOLGOOBOOLLOBGLOLOAOLLIBLIGGUGLGUBUULL")
client.run(secret_token.secret_token)