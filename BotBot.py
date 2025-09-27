import discord
import youtube_dl
import random as r
import asyncio
from fixer import simple_fixer
from discord.ext import commands
import os
import json
with open("data.json") as f:
    cokGicik = json.load(f)

question = [i for n,i in enumerate((cokGicik), start = 1) if not n % 2 == 0]
answer = [i for n,i in enumerate((cokGicik), start = 1) if     n % 2 == 0]

f.close()

dictonary = {}
for q, a in zip(question, answer):
    dictonary[q] = a
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
youtube_dl.utils.bug_reports_message = lambda: ''

def blank(func):
    func()

    return 0

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def play(self, ctx, *, query):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {query}')

    @commands.command()
    async def yt(self, ctx, *, url):
        """Plays from a url (almost anything youtube_dl supports)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def stream(self, ctx, *, url):
        """Streams from a url (same as yt, but doesn't predownload)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")

    @commands.command()
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @play.before_invoke
    @yt.before_invoke
    @stream.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
@bot.event
async def on_ready():
    from os import system
    try:    
        system("cls")
    except:
        system("clear")
    print(f'We have logged in as {bot.user}')
    # for qe in question[0:5]:
    #     print(qe)
    # print(100*"=")
    # for an in answer[0:5]:
    #     print(an)

    for qe in dictonary.keys():
        print(qe)
    print(100*"=")

    for an in dictonary.values():
        print(an)


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def calc(ctx,n1,eq,n2):
    if eq in ['+','-','*','/','//']:
        has = eval(f"{n1} {eq} {n2}")
        await ctx.send(f'Hmm, {n1} {eq} {n2} is {has}')


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


#




@bot.command()

async def lazy(ctx, *, thing):
    try:
        if thing in dictonary.keys():
            await ctx.send(dictonary.get(thing,"I don't understand."))
        else:
            await ctx.send(dictonary.get(simple_fixer(thing, dictonary.keys()),"I don't understand."))
    except:
            await ctx.send(dictonary.get(thing,"I don't understand."), '..')


@bot.command()

async def daurulang(ctx):
            await ctx.send(
        "Daur ulang itu penting, jangan buang sampah sembarangan! "
        "Dengan mendaur ulang barang-barang seperti kertas, plastik, dan logam, "
        "kita dapat mengurangi limbah yang mencemari lingkungan. "
        "Selain itu, daur ulang juga membantu menghemat sumber daya alam dan energi. "
        "Ayo mulai memilah sampah dari sekarang dan jadilah bagian dari perubahan positif untuk bumi kita!"
        "Mau penjelasan lebih lanjut? Ketik $lanjut!"
                )
@bot.command()
async def lanjut(ctx):  
    await ctx.send(
        "Daur ulang adalah proses mengubah limbah menjadi bahan baru yang dapat digunakan kembali. "
        "Dengan mendaur ulang, kita dapat mengurangi jumlah sampah yang berakhir di tempat pembuangan akhir (TPA) "
        "dan mengurangi pencemaran lingkungan. Selain itu, daur ulang juga membantu menghemat energi dan sumber daya alam, "
        "karena produksi barang dari bahan daur ulang biasanya memerlukan lebih sedikit energi dibandingkan dengan produksi dari bahan mentah. "
        "Jadi, mari kita semua berkontribusi dalam menjaga kebersihan lingkungan dengan cara mendaur ulang barang-barang yang sudah tidak terpakai!"
    )
@bot.command()
async def meme(ctx):
    with open(f"images/{r.choice(os.listdir('images'))}", 'rb') as f:
        img = discord.File(f)

    await ctx.send(file=img)











bot.run(" Your Token Here ")