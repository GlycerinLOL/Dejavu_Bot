import discord
from discord.ext import commands
import os

class loadReload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cogs: loadReload.py is loaded!")

    @commands.command()
    async def load(self, ctx, extension):
        await self.bot.load_extension(f'cmds.{extension}')
        await ctx.send(f"{extension} 已上傳")

    @commands.command()
    async def unload(self, ctx, extension):
        await self.bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f'{extension} 已卸載')

    @commands.command()
    async def reload(self, ctx, extension):
        try:
            await self.bot.reload_extension(f'cmds.{extension}')
            await ctx.send(f'{extension} 已更新')
        except AttributeError:
            await ctx.send("reload error")

async def setup(bot):
    await bot.add_cog(loadReload(bot))