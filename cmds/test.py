import discord
from discord.ext import commands

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cogs: test.py is loaded!")

    @commands.command()
    async def check(self, ctx):
        await ctx.send("bot check")

    @commands.command()
    async def bot(self, ctx):
        await ctx.send("逼...逼...機油好難喝")

async def setup(bot):
    await bot.add_cog(test(bot))