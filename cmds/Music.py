import wavelink
import discord
from discord.ext import commands

class CustomPlayer(wavelink.Player):
    def __init__(self):
        super().__init__()
        self.queue = wavelink.Queue()

class Music(commands.Cog):
    """Music cog to hold Wavelink related commands and listeners."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cogs: Music.py is loaded!")

    @commands.command()
    async def connect(ctx):
        vc = ctx.voice_client
        try:
            channel = ctx.author.voice.channel
        except AttributeError:
            return await ctx.send("Error: Author not in any voice chat.")

        if not vc:
            await ctx.author.voice.channel.connect(cls=CustomPlayer())
        else:
            await ctx.send("Bot is already in a voice chat")

    @commands.command()
    async def play(ctx, *, search: wavelink.YouTubeTrack):
        vc = ctx.voice_client
        if not vc:
            custom_player = CustomPlayer()
            vc: CustomPlayer = await ctx.author.voice.channel.connect(cls=custom_player)

        if vc.is_playing():

            vc.queue.put(item=search)
            await ctx.send(embed=discord.Embed(
                title=search.title,
                url=search.uri,
                author=ctx.author,
                description=f"Queue {search.title} in {vc.channel}"
            ))
        else:
            await vc.play(search)

            await ctx.send(embed=discord.Embed(
                title=vc.source.title,
                url=search.uri,
                author=ctx.author,
                description=f"Queue {vc.source.title} in {vc.channel}"
            ))
        

    

async def setup(bot):
    await bot.add_cog(Music(bot))