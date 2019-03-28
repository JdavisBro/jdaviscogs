import discord
import time
import random
from discord.ext import commands

class jroll:
    """Jroll!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def jroll(self, ctx):
        """tHIS ROLLS and lag"""
        stop= random.randint(1,5)
        message= await self.bot.say("Rolling\n⠀1\n⠀2\n>3<\n⠀4\n⠀5\nRolling")
        time.sleep(0.4)
        await self.bot.edit_message(message,new_content=str("Rolling\n⠀2\n⠀3\n>4<\n⠀5\n⠀1\nRolling"))
        time.sleep(0.4)
        await self.bot.edit_message(message,new_content=str("Rolling\n⠀3\n⠀4\n>5<\n⠀1\n⠀2\nRolling"))
        time.sleep(0.4)
        await self.bot.edit_message(message,new_content=str("Rolling\n⠀4\n⠀5\n>1<\n⠀2\n⠀3\nRolling"))
        time.sleep(0.4)
        await self.bot.edit_message(message,new_content=str("Rolling\n⠀5\n⠀1\n>2<\n⠀3\n⠀4\nRolling"))
        time.sleep(0.4)
        await self.bot.edit_message(message,new_content=str("Rolling\n⠀1\n⠀2\n>3<\n⠀4\n⠀5\nRolling"))
        time.sleep(0.4)
        await self.bot.edit_message(message,new_content=str("Rolling\n⠀2\n⠀3\n>4<\n⠀5\n⠀1\nRolling"))
        time.sleep(0.5)
        await self.bot.edit_message(message,new_content=str("Rolling\n⠀3\n⠀4\n>5<\n⠀1\n⠀2\nRolling"))
        time.sleep(0.5)
        await self.bot.edit_message(message,new_content=str("Rolling\n⠀4\n⠀5\n>1<\n⠀2\n⠀3\nRolling"))
        time.sleep(0.6)
        await self.bot.edit_message(message,new_content=str("Rolling\n⠀5\n⠀1\n>2<\n⠀3\n⠀4\nRolling"))
        time.sleep(0.7)
        await self.bot.edit_message(message,new_content=str("Rolling\n⠀1\n⠀2\n>3<\n⠀4\n⠀5\nRolling"))
        if stop==1:
            time.sleep(0.8)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀2\n⠀3\n>4<\n⠀5\n⠀1\nRolling"))
            time.sleep(0.9)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀3\n⠀4\n>5<\n⠀1\n⠀2\nRolling"))
            time.sleep(1)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀4\n⠀5\n>1<\n⠀2\n⠀3\nRolling"))
        elif stop==2:
            time.sleep(0.8)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀2\n⠀3\n>4<\n⠀5\n⠀1\nRolling"))
            time.sleep(0.9)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀3\n⠀4\n>5<\n⠀1\n⠀2\nRolling"))
            time.sleep(1.0)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀4\n⠀5\n>1<\n⠀2\n⠀3\nRolling"))
            time.sleep(1.1)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀5\n⠀1\n>2<\n⠀3\n⠀4\nRolling"))
        elif stop==3:
            time.sleep(0.8)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀2\n⠀3\n>4<\n⠀5\n⠀1\nRolling"))
            time.sleep(0.9)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀3\n⠀4\n>5<\n⠀1\n⠀2\nRolling"))
            time.sleep(1.0)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀4\n⠀5\n>1<\n⠀2\n⠀3\nRolling"))
            time.sleep(1.1)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀5\n⠀1\n>2<\n⠀3\n⠀4\nRolling"))
            time.sleep(1.2)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀1\n⠀2\n>3<\n⠀4\n⠀5\nRolling"))
        elif stop==4:
            time.sleep(0.8)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀2\n⠀3\n>4<\n⠀5\n⠀1\nRolling"))
        else:
            time.sleep(0.8)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀2\n⠀3\n>4<\n⠀5\n⠀1\nRolling"))
            time.sleep(0.9)
            await self.bot.edit_message(message,new_content=str("Rolling\n⠀3\n⠀4\n>5<\n⠀1\n⠀2\nRolling"))

def setup(bot):
    bot.add_cog(jroll(bot))
