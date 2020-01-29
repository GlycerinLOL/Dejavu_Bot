import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):

    @commands.command()
    async def who(self,ctx):
        await ctx.send('Hi! I am a bot design by GlycerinLOL!')

def setup(bot):
    bot.add_cog(Main(bot))