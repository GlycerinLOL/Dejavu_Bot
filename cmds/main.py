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
    @commands.command()
    async def 鯊鯊舞(self,ctx):
        pic = discord.File(jdata['shark_dancing'])
        await ctx.send(file=pic)
    @commands.command()
    async def 語錄(self,ctx,msg):
        if msg == '我有叫你尻槍嗎':
            pic = discord.File(jdata['chat_1'])
            await ctx.message.delete()
            await ctx.send(f'{ctx.message.author} :')
            await ctx.send(file=pic)
        elif msg == '蘿莉邪教':
            pic = discord.File(jdata['chat_2'])
            await ctx.message.delete()
            await ctx.send(f'{ctx.message.author} :')
            await ctx.send(file=pic)
        elif msg == '靠':
            pic = discord.File(jdata['chat_3'])
            await ctx.message.delete()
            await ctx.send(f'{ctx.message.author} :')
            await ctx.send(file=pic)
        elif msg == '本子真的':
            pic = discord.File(jdata['chat_4'])
            await ctx.message.delete()
            await ctx.send(f'{ctx.message.author} :')
            await ctx.send(file=pic)
        elif msg == '靠北喔':
            pic = discord.File(jdata['chat_5'])
            await ctx.message.delete()
            await ctx.send(f'{ctx.message.author} :')
            await ctx.send(file=pic)
        elif msg == '靠真的喔':
            pic = discord.File(jdata['chat_6'])
            await ctx.message.delete()
            await ctx.send(f'{ctx.message.author} :')
            await ctx.send(file=pic)
        elif msg == '興奮':
            pic = discord.File(jdata['chat_7'])
            await ctx.message.delete()
            await ctx.send(f'{ctx.message.author} :')
            await ctx.send(file=pic)
        elif msg == '言論自由':
            pic = discord.File(jdata['chat_8'])
            await ctx.message.delete()
            await ctx.send(f'{ctx.message.author} :')
            await ctx.send(file=pic)
    

def setup(bot):
    bot.add_cog(Main(bot))