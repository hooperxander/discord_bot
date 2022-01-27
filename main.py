import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$deez'):
        await message.channel.send("Aidan Is Gay! We Are So Proud Of Aidan For Coming Out As Gay!")

client.run('OTM2MzU4NDUyNzkwNDMxNzU0.YfMBww._ME6JBvomUkhYtDnfgZfvfzFrMg')