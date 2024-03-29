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
        self.latestCtx = any
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cogs: Music.py is loaded!")

    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player: CustomPlayer, track: wavelink.Track, reason):
        print("current track end")
        if not player.queue.is_empty:
            next_track = player.queue.get()
            print(next_track.title, next_track.uri, player.queue)
            await player.play(next_track)
        else:
            print("queue is empty")


    @commands.command()
    async def connect(self, ctx):
        self.latestCtx = ctx
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
        self.latestCtx = ctx
        vc = ctx.voice_client
        if vc:
            await vc.disconnect()
        else:
            await ctx.send("Error: Bot is not in any voice chat")

    @commands.command()
    async def play(self, ctx, *, search: wavelink.YouTubeTrack): # 一般Youtube Track
        self.latestCtx = ctx
        vc = ctx.voice_client
        if not vc:
            custom_player = CustomPlayer()
            vc: CustomPlayer = await ctx.author.voice.channel.connect(cls=custom_player)

        if vc.is_playing():
            vc.queue.put(item=search)
            print(search.title, search.uri, ctx.author,vc.queue,"queue")
            videoID = search.uri.split("watch?v=")[1].split("&")[0]
            embed=discord.Embed(title=search.title, url=search.uri, description=f"Queue {search.title} in {vc.channel}", color=0xfe0606)
            embed.set_author(name=ctx.author,icon_url=ctx.author.avatar)
            embed.set_image(url=f"https://img.youtube.com/vi/{videoID}/0.jpg")
            # embed.add_field(name="歌曲佇列:", value="undefined", inline=False)
            await ctx.send(embed=embed)
        else:
            await vc.play(search)
            print(vc.source.title, vc.source.uri, ctx.author,vc.queue,"play")
            videoID = vc.source.uri.split("watch?v=")[1].split("&")[0]
            embed=discord.Embed(title=vc.source.title, url=vc.source.uri, description=f"Playing {vc.source.title} in {vc.channel}", color=0xfe0606)
            embed.set_author(name=ctx.author,icon_url=ctx.author.avatar)
            embed.set_image(url=f"https://img.youtube.com/vi/{videoID}/0.jpg")
            # embed.add_field(name="歌曲佇列:", value="undefined", inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    async def playlist(self, ctx, *, search: wavelink.YouTubePlaylist): # 播放清單
        self.latestCtx = ctx
        vc = ctx.voice_client
        if not vc:
            custom_player = CustomPlayer()
            vc: CustomPlayer = await ctx.author.voice.channel.connect(cls=custom_player)

        for item in search.tracks:
            vc.queue.put(item=item)
        if vc.is_playing():
            print(search.name,ctx.author,vc.queue,"queue")
            embed=discord.Embed(title=search.name, description=f"Queue PlayList {search.name} in {vc.channel}", color=0xfe0606)
            embed.set_author(name=ctx.author,icon_url=ctx.author.avatar)
            # embed.add_field(name="歌曲佇列:", value="undefined", inline=False)
            await ctx.send(embed=embed)
        else:
            await vc.play(vc.queue.get())
            print(search.name,ctx.author,vc.queue,"play")
            embed=discord.Embed(title=search.name, description=f"Playing PlayList {search.name} in {vc.channel}", color=0xfe0606)
            embed.set_author(name=ctx.author,icon_url=ctx.author.avatar)
            # embed.add_field(name="歌曲佇列:", value="undefined", inline=False)
            await ctx.send(embed=embed)


    @commands.command()
    async def skip(self, ctx):
        self.latestCtx = ctx
        vc = ctx.voice_client
        if vc:
            if not vc.is_playing():
                return await ctx.send("Nothing is playing now.")
            if vc.queue.is_empty:
                return await vc.stop()
            
            await vc.seek(vc.track.length*1000)
            if vc.is_paused():
                await vc.resume()
        else:
            await ctx.send("Error: Bot is not in any voice chat")

    @commands.command()
    async def queue(self, ctx):
        self.latestCtx = ctx
        vc = ctx.voice_client
        if vc:
            await ctx.send(f"Queue now: {vc.queue}")
        else:
            await ctx.send("Error: Bot is not in any voice chat")

    @commands.command()
    async def clear_queue(self, ctx):
        self.latestCtx = ctx
        vc = ctx.voice_client
        if vc:
            await ctx.send(f"Clear queue now: {vc.queue}")
            vc.queue.clear()
            await vc.stop() 
        else:
            await ctx.send("Error: Bot is not in any voice chat")

    @commands.command()
    async def stop(self, ctx):
        self.latestCtx = ctx
        vc = ctx.voice_client
        if vc:
            await vc.stop() 
        else:
            await ctx.send("Error: Bot is not in any voice chat")

    @commands.command()
    async def pause(self, ctx):
        self.latestCtx = ctx
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
        self.latestCtx = ctx
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
        print(error)
        if isinstance(error, commands.BadArgument):
            await ctx.send("Could not find a track.")
        else:
            await ctx.send("Some Error Occurs.")

        

    

async def setup(bot):
    await bot.add_cog(Music(bot))