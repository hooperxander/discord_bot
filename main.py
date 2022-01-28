import discord
import secret_token
from random import randint
from nltk.sentiment import SentimentIntensityAnalyzer

client = discord.Client()
sia = SentimentIntensityAnalyzer()

mad_responses = ["Relax, Okay?", "You Sound Upset Bro Chill Haha", "Uh Oh.... Is Somebody... Angwy? Does Little Baby Need Some Milk? Some Mommy Milk?"]

async def uh_oh_u_mad(message):
    random_index = randint(0, len(mad_responses)-1)
    await message.channel.send(mad_responses[random_index])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if sia.polarity_scores(message.content)['compound'] < -.5:
        await uh_oh_u_mad(message)

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