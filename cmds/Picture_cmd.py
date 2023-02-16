import discord
from discord.ext import commands
import json

with open('setting.json', mode='r',encoding='utf8') as jfile:
    setting = json.load(jfile)

class Picture_cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cogs: Picture_cmd.py is loaded!")

    @commands.command()
    async def shark(self, ctx):
        pic = discord.File(setting['shark_dancing'])
        await ctx.send(file = pic)

async def setup(bot):
    await bot.add_cog(Picture_cmd(bot))