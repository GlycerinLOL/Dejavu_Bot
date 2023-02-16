import discord
from discord.ext import commands
import wavelink
import json
import os
import asyncio

with open('setting.json', mode='r',encoding='utf8') as jfile:
    setting = json.load(jfile)

client = commands.Bot(command_prefix=";",intents=discord.Intents.all())
client.owner_id = setting['owner_id']

async def connect_nodes():
        """Connect to our Lavalink nodes."""
        await client.wait_until_ready()
        await wavelink.NodePool.create_node(bot=client,
                                            host='127.0.0.1',
                                            port=2333,
                                            password='youshallnotpass')

async def load_exts():
    for filename in os.listdir("./cmds"):
        if filename.endswith('.py'):
            await client.load_extension(f"cmds.{filename[:-3]}")

@client.event
async def on_wavelink_node_ready(node: wavelink.Node):
    """Event fired when a node has finished connecting."""
    print(f'Node: <{node.identifier}> is ready!')


@client.event
async def on_ready():
    print('登入身分:',client.user)
    await client.loop.create_task(connect_nodes())
    status = discord.Game(setting['status'])
    await client.change_presence(status=discord.Status.online, activity=status)
    

async def main():
    await load_exts()
    await client.start(setting['token'])

asyncio.run(main())
    


