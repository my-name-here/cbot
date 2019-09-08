

from discord.ext import commands
import discord
import keep_alive
import discord.client
import urllib
import urllib.request as request
import json
import requests
import random
import os
from requests import get
import wikipedia
import youtube_dl

bot = commands.Bot(command_prefix='!!' )           
cogs = ['cogs.maincog']
@bot.event
async def on_ready():
    for cog in cogs:
      bot.load_extension(cog)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='prefix is !! use !!help for commands'))
 
@bot.event
async def on_member_join(member):
    await bot.send_message(member.server, " {0.mention}, just joined".format(member))
from discord.ext import commands







  
token = os.environ.get("DISCORD_BOT_SECRET")
keep_alive.keep_alive()
bot.run(token)
