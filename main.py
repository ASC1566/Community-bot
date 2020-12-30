# bot.py
from keep_alive import keep_alive 
import os

import discord
from discord.ext import commands
import traceback
import sys
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(
	command_prefix=". ",
	case_insensitive=True
)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name},Welcome to the server! Feel free to go to these channels #🟠information and #🟠server-questions to find out the rules of the server and how to use the server. After going through that, you can verify yourself by going to #🟠verification  to gain access to the channels :ShibaHeart: if you understand and agree to the rules of the server! Enjoy your stay ! ^^'
    )


keep_alive()
client.run(TOKEN)
