from discord.ext import commands

class MainCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def acommand(self, ctx, argument):
       await self.bot.say("Stuff")        

    @commands.command()
    async def roll(ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command()
    async def invite(ctx):
      '''gives invite link'''
      await ctx.send("https://discordapp.com/api/oauth2/authorize?client_id=557976042476797952&permissions=0&scope=bot")
    @commands.command()
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



    @commands.command()
    async def bitcoin(ctx):
      '''
      get bitcoin price
      '''
      price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()['bpi']['USD']['rate']
      await ctx.send("Bitcoin is $" + price)
    @commands.command()
    async def ping(ctx):
        '''get ping time'''
        await ctx.send(" :ping_pong: Pong! Ping: {}ms".format(round(bot.latency * 10000)))
    @commands.command()
    async def members(ctx):

      await ctx.send(f"The server {ctx.guild.name} has {len(ctx.guild.members)} members.")

    async def on_message(self, message):
        print(message.content)

def setup(bot):
    bot.add_cog(MainCog(bot))
