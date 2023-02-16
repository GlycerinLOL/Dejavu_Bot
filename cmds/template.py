import discord
from discord.ext import commands
import json

with open('setting.json', mode='r',encoding='utf8') as jfile:
    setting = json.load(jfile)

class template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cogs: template.py is loaded!")

    # @commands.command()
    # async def check(self, ctx):
    #     await ctx.send("bot check")

async def setup(bot):
    await bot.add_cog(template(bot))