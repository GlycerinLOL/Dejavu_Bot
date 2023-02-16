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

    @commands.command()
    async def embedTest(self, ctx):
        embed=discord.Embed(title="Test", description="Test", color=0xfe0606)
        embed.add_field(name="undefined", value="undefined", inline=False)
        await ctx.send(embed=embed)

        
async def setup(bot):
    await bot.add_cog(test(bot))