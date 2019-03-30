import discord
from discord.ext import commands
import json

json="data/chooser/people.json"
fileW=open(json, 'w')
fileR=open(json, 'r')
last=0
data=json.loads(fileR)
fileR.flush()

class chooser:
    """Chooser!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def choose(self,ctx):
        """Chooser!"""
        if ctx.message.server is none:
            last+=1
            data[ctx.message.author.id]=last
            json.dumps(data,dataSave)
            fileW.write(dataSave)
            fileW.flush()
            await self.bot.say("You have number {}".format(last))

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def givemenumber(self,ctx,number):
        await self.bot.say("Number {} is {}".format(number,data[number]))

def setup(bot):
    bot.add_cog(chooser(bot))
