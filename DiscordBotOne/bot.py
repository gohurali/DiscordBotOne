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
    if(message.content.startswith('!hi')):
        print('Bot said bye');
        await client.send_message(message.channel, "HI PAL")
    elif(message.content.startswith('!bye')):
        print('Bot said bye');
        await client.send_message(message.channel, "BYE PAL")




client.run("")