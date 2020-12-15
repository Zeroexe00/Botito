import discord
from dotenv import load_dotenv
load_dotenv()
import os
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/hola'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('/help'):
        await message.channel.send('ayuda con que gil! hueee')

client.run(os.getenv('TOKEN'))