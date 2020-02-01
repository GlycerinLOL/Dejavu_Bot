import discord
from discord.ext import commands
import json
import os
import keep_alive

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('>> bot is online <<')
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['main_chat_channel']))
    await channel.send(f'{member} join!')
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['main_chat_channel']))
    await channel.send(f'{member} leave!')
@bot.command()
async def nh(ctx,msg):
    url = 'https://nhentai.net/g/'
    channel = bot.get_channel(int(jdata['R18_channel']))
    await channel.send(url+msg)

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
      bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(jdata['Token'])


