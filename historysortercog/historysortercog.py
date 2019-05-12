import discord
from discord.ext import commands
import random

class historysortercog:
    """Only avalible in HistoryWars to sort you into your civ!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def sort(self,ctx):
        """Sorts you into a civ!"""
        civs=["Egyptians","Vikings","Greeks","Samurai","Romans","Persians"]
        civname=random.choice(civs)
        civrole = discord.utils.get(ctx.message.server.roles, name=civname)
        tobesorted = discord.utils.get(ctx.message.server.roles, id="546570117006229524")
        self.bot.add_roles(ctx.message.author,civrole)
        self.bot.remove_roles(ctx.message.author,tobesorted)
        embed=discord.Embed(title="Red-SorterCog", description="{} has been sorted into {}".format(ctx.message.author.name,civname), color=0x00e138)
        logschannel=discord.utils.get(ctx.message.server.channels,name='logs')
        await self.bot.send_message(logschannel,embed=embed)
        await self.bot.send_message(ctx.message.author,"You have been sorted into {}".format(civname))
        await self.bot.delete_message(ctx.message)

def setup(bot):
    bot.add_cog(historysortercog(bot))
