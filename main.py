

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

bot = commands.Bot(command_prefix='!!')
@bot.event


async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='prefix is !! use !!help for commands'))
 
@bot.event
async def on_member_join(member):
    await bot.send_message(member.server, " {0.mention}, just joined".format(member))

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def invite(ctx):
  '''gives invite link'''
  await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=557976042476797952&permissions=0&scope=bot")
@bot.command()
async def xkcd(ctx,number):
  '''use !!xkcd number to get numberth xkcd'''
  num=number
  print(str("http://xkcd.com/{}/info.0.json".format(num)))
  req = request.urlopen(str("http://xkcd.com/{}/info.0.json".format(num)))


  str_response = req.read()

  obj = json.loads(str_response)
  obj=json.dumps(obj)
  obj = json.loads(obj)
  image_url=obj['img']
  print(obj)
  titletext=obj['alt']
  title=obj['safe_title']

  resource = urllib.request.urlopen(image_url)
  output = open("cat.jpg","wb")
  output.write(resource.read())
  output.close()

  x=(json.dumps(obj, indent = 4, sort_keys=True))
  await ctx.send(title)
  await ctx.send(image_url)
  await ctx.send(titletext)



@bot.command()
async def bitcoin(ctx):
  '''
  get bitcoin price
  '''
  price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()['bpi']['USD']['rate']
  await ctx.send("Bitcoin is $" + price)
@bot.command()
async def ping(ctx):
    '''get ping time'''
    await ctx.send(" :ping_pong: Pong! Ping: {}ms".format(round(bot.latency * 10000)))
@bot.command()
async def members(ctx):

	await ctx.send(f"The server {ctx.guild.name} has {len(ctx.guild.members)} members.")

  
token = os.environ.get("DISCORD_BOT_SECRET")
keep_alive.keep_alive()
bot.run(token)