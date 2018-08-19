__author__ = "Gohur Ali"
__version__ = "0.1"
__status__ = "Initial Build Stage"
import discord
from discord.ext import commands
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is online and running")
    channel = discord.Object(id='general');

@client.event
async def on_message(message):

    # Words to represent bad words..
    specificWords = ["soup", "food", "supreme", "backpack"]

    # Loop looks for words within the array, if the "bad" word appears, delete and warn the user
    for i in specificWords:
        if(i in message.content):
            await client.delete_message(message)
            await client.send_message(message.channel, "No bad words please")

    if(message.content.startswith('!hello')):
        print('Bot said bye');
        await client.send_message(message.channel, "HI PAL")
    elif(message.content.startswith('!bye')):
        print('Bot said bye');
        await client.send_message(message.channel, "BYE PAL")
    elif(message.content.startswith('!hibotone')):
        user_id = message.author.id
        await client.send_message(message.channel,"Hi <@%s>" % (user_id))

# Keep token empty with each push in order to keep bot secure!
client.run("")