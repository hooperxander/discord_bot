import discord
import secret_token
import time
import sqlite3

from random import randint
from nltk.sentiment import SentimentIntensityAnalyzer

client = discord.Client()
sia = SentimentIntensityAnalyzer()
gif_db = sqlite3.connect('gifs.db')

mad_responses = ["Relax, Okay?", "You Sound Upset Bro Chill Haha", "Uh Oh.... Is Somebody... Angwy? Does Little Baby Need Some Milk? Some Mommy Milk?"]

async def send_random_gif(channel):
    gif_list_cursor = gif_db.execute("SELECT * from GIFS")
    gif_list = gif_list_cursor.fetchall()
    if len(gif_list) > 0:
        random_gif_index = randint(0, len(gif_list)-1)
        await channel.send("here is gif " + str(random_gif_index+1) + " of " + str(len(gif_list)) + " stored gifs:")
        await channel.send(gif_list[random_gif_index][0])
    else:
        await channel.send("maro doesnt have any gifs stored")

async def uh_oh_u_mad(message):
    random_index = randint(0, len(mad_responses)-1)
    await message.channel.send(mad_responses[random_index])

@client.event
async def on_ready():
    print('{0.user} has logged in'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #print("\"" + message.content + "\" " + str(sia.polarity_scores(message.content)['compound']))

    if 'tenor.com' in message.content:
        gif_db.execute("INSERT INTO GIFS (URL) VALUES(" + "\'" + message.content + "\')")
        gif_db.commit()

    if sia.polarity_scores(message.content)['compound'] < -.5:
        await uh_oh_u_mad(message)

    if (message.channel.name == 'epic-gamers') and ('http' in message.content) and not ('tenor.com' in message.content):
        for i in range(6):
            time.sleep(10)
            await message.channel.send("<@!" + str(message.author.id) + '> you are a fucking retard stupid cow, post links in the right channel')

    if message.content.startswith('maro hello'):
        await message.channel.send('Hello!')
        return

    if message.content.startswith('maro gif pls'):
        await send_random_gif(message.channel)
        return
    
    if message.content.startswith('maro deez'):
        await message.channel.send("Aidan Is Gay! We Are So Proud Of Aidan For Coming Out As Gay!")
        return

    if message.content.startswith('maro pls'):
        await message.channel.send("OOBLOOBLBLBLABOBLBLWAOOOOOOOOOO")
        await message.channel.send("GULUUGOBOGLOOUGOUBOGOLOOGUBOGOBUOGBOOOLOBOGOO")
        await message.channel.send("Haaah... Hah... Haaah... Hooo...")
        await message.channel.send("glooogoboAOGOBIGOBOLGOOBOOLLOBGLOLOAOLLIBLIGGUGLGUBUULL")
        return
client.run(secret_token.secret_token)