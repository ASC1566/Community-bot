# bot.py
from keep_alive import keep_alive 
import os

import discord
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()

bot = commands.Bot(
	command_prefix=". ",
	case_insensitive=True,
  intents=intents
)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    channels = [
      bot.get_channel(793480577230569534), #information
      bot.get_channel(793480577230569535), #server questions
      bot.get_channel(793480577230569536) #verification
    ]
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name},Welcome to the server! Feel free to go to these channels {channels[0].mention} and {channels[1].mention}# to find out the rules of the server and how to use the server. After going through that, you can verify yourself by going to{channels[2].mention}   to gain access to the channels  if you understand and agree to the rules of the server! Enjoy your stay ! ^^'
    )

keep_alive(botnt.run(TOKEN)
