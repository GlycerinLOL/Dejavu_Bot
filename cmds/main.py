import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):

    quote ={
        '我有叫你尻槍嗎' : 'chat_1',
        '蘿莉邪教' : 'chat_2',
        '靠' : 'chat_3',
        '本子真的' : 'chat_4',
        '靠北喔' : 'chat_5',
        '靠真的喔' : 'chat_6',
        '興奮' : 'chat_7',
        '言論自由' : 'chat_8' 
    }

    @commands.command()
    async def who(self,ctx):
        await ctx.send('Hi! I am a bot design by GlycerinLOL!')

    @commands.command()
    async def 鯊鯊舞(self,ctx):
        pic = discord.File(jdata['shark_dancing'])
        await ctx.send(file=pic)

    @commands.command()
    async def 語錄(self,ctx,msg):
        if msg == 'list':
            await ctx.send('These are quotes you can use:')
            result = [(i+1,list(quote.keys())[i]) for i in range(len(quote))]
            for item in result:
                await ctx.send(f'{result[0]} : {result[1]}')
            return 
        token = quote.get(msg)
        if token == None:
            return 
        else:
            pic = discord.File(jdata[token])
            await ctx.message.delete()
            await ctx.send(f'{ctx.message.author} :')
            await ctx.send(file=pic)


def setup(bot):
    bot.add_cog(Main(bot))