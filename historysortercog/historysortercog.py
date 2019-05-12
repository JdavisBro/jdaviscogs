import discord
from discord.ext import commands
import asyncio
import random

class historysortercog:
    """Only avalible in HistoryWars to sort you into your civ!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def sort(self,ctx):
        """Sorts you into a civ!"""
        if ctx.message.server.id=="506407988794490880":
            if ctx.message.channel.id=="548798868070858752":
                civs=["Egyptians","Vikings","Greeks","Samurai","Romans","Persians"]
                civname=random.choice(civs)
                civrole = discord.utils.get(ctx.message.server.roles, name=civname)
                tobesorted = discord.utils.get(ctx.message.server.roles, name="To Be Sorted")
                await self.bot.add_roles(ctx.message.author,civrole)
                await self.bot.remove_roles(ctx.message.author,tobesorted)
                embed=discord.Embed(title="Red-SorterCog", description="{} has been sorted into {}".format(ctx.message.author.name,civname), color=0x00e138)
                logschannel=discord.utils.get(ctx.message.server.channels,name='logs')
                await self.bot.send_message(logschannel,embed=embed)
                await self.bot.send_message(ctx.message.author,"You have been sorted into {}".format(civname))
                await self.bot.delete_message(ctx.message)
             
    @asyncio.coroutine
    async def on_message(self,message):
        if message.server.id=="506407988794490880":
            if message.channel.id=="548798868070858752":
                if message.content!="-sort":
                    await client.delete_message(message)

def setup(bot):
    bot.add_cog(historysortercog(bot))
