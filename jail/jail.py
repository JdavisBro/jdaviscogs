import discord
from discord.ext import commands
from discord.utils import get
import time

class jail:
    """JAIL!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def jail(self,ctx,person,*,message="30 you've been very bad today!"):
        """Put this guy in Prison!"""
        if ctx.message.startswith <= 0:
            await self.bot.say("Oi m8, that's lower than 0, dont want me broken do ya m8")
        else:
            log= get(server.channel,id="474058752597688320")
            role= get(server.roles, id="564190693287788544")
            if "473868799536398356" in [y.id for y in ctx.message.author.roles]:
                await self.bot.add_roles(person,role)
                try:
                    await self.bot.say("Okay! {} has been jailed!".format(person.name)
                except:
                    pass
                await self.bot.send_message(log,"{} has been jailed for {} minutes by {}".format(person.name,ctx.message.content.startswith,ctx.message.author.name))
                timefor=int(ctx.message.content.startswith*60)
                time.sleep(timefor)
                await self.bot.remove_roles(person,role)
                await self.bot.send_message(log,"{} has been freed from prison!".format(person.name))
            elif "517644591218950154" in [y.id for y in ctx.message.author.roles]:
                if ctx.message.content.startswith <= 240:
                    await self.bot.add_roles(person,role)
                    try:
                        await self.bot.say("Okay! {} has been jailed!".format(person.name))
                    except:
                        pass
                    await self.bot.send_message(log,"{} has been jailed for {} minutes by {}".format(person.name,ctx.message.content.startswith,ctx.message.author.name))
                    timefor=int(ctx.message.content.startswith*60)
                    time.sleep(timefor)
                    await self.bot.remove_roles(person,role)
                    await self.bot.send_message(log,"{} has been freed from prison!".format(person.name))
                else:
                    await self.bot.say("Oi m9 ur a moderator that means you can excede 4 hours of jail givin m8")
            elif "513380418901377025" in [y.id for y in ctx.message.author.roles]:
                if ctx.message.content.startswith <= 30:
                    await self.bot.add_roles(person,role)
                    try:
                        await self.bot.say("Okay! {} has been jailed!".format(person.name))
                    except:
                        pass
                    await self.bot.send_message(log,"{} has been jailed for {} minutes by {}".format(person.name,ctx.message.content.startswith,ctx.message.author.name))
                    timefor=int(ctx.message.content.startswith*60)
                    time.sleep(timefor)
                    await self.bot.remove_roles(person,role)
                    await self.bot.send_message(log,"{} has been freed from prison!".format(person.name))
                else:
                    await self.bot.say("Oi m9 ur a moderator that means you can excede 4 hours of jail givin m8")


def setup(bot):
    bot.add_cog(jail(bot))
