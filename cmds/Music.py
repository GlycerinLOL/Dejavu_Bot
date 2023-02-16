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

    @commands.Cog.listener()
    async def on_wavelink_track_end(player: CustomPlayer, track: wavelink.Track, reason):
        if not player.queue.is_empty:
            next_track = player.queue.get()
            await player.play(next_track)

    @commands.command()
    async def connect(self, ctx):
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
    async def disconnect(self, ctx):
        vc = ctx.voice_client
        if vc:
            await vc.disconnect()
        else:
            await ctx.send("Error: Bot is not in any voice chat")

    @commands.command()
    async def play(self, ctx, *, search: wavelink.YouTubeTrack):
        vc = ctx.voice_client
        if not vc:
            custom_player = CustomPlayer()
            vc: CustomPlayer = await ctx.author.voice.channel.connect(cls=custom_player)

        if vc.is_playing():

            vc.queue.put(item=search)
            print(search.title, search.uri, ctx.author,vc.queue,"queue")
            await ctx.send(f"Now queueing {search.title} by {ctx.author}")
        else:
            await vc.play(search)
            print(vc.source.title, vc.source.uri, ctx.author,vc.queue,"play")
            await ctx.send(f"Now playing {search.title} by {ctx.author}")


    @commands.command()
    async def skip(self, ctx):
        vc = ctx.voice_client
        if vc:
            if not vc.is_playing():
                return await ctx.send("Nothing is playing now.")
            if vc.queue.is_empty:
                return await vc.stop()
            
            print(vc.track.length)
            await vc.seek(vc.track.length*1000)
            if vc.is_paused():
                await vc.resume()
        else:
            await ctx.send("Error: Bot is not in any voice chat")

    @commands.command()
    async def queue(self, ctx):
        vc = ctx.voice_client
        if vc:
            await ctx.send(f"Queue now: {vc.queue}")
        else:
            await ctx.send("Error: Bot is not in any voice chat")

    @commands.command()
    async def clear_queue(self, ctx):
        vc = ctx.voice_client
        if vc:
            await ctx.send(f"Clear queue now: {vc.queue}")
            vc.queue.clear()
        else:
            await ctx.send("Error: Bot is not in any voice chat")

    @commands.command()
    async def pause(self, ctx):
        vc = ctx.voice_client
        if vc:
            if vc.is_playing() and not vc.is_paused():
                await vc.pause()
            else:
                await ctx.send("Nothing is playing.")
        else:
            await ctx.send("The bot is not connected to a voice channel")

    @commands.command()
    async def resume(self, ctx):
        vc = ctx.voice_client
        if vc:
            if vc.is_paused():
                await vc.resume()
            else:
                await ctx.send("Nothing is paused.")
        else:
            await ctx.send("The bot is not connected to a voice channel")

    @play.error
    async def play_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Could not find a track.")
        else:
            await ctx.send("Please join a voice channel.")

        

    

async def setup(bot):
    await bot.add_cog(Music(bot))