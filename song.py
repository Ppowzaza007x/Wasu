import discord
from discord.ext import commands
import youtube_dl 

intents = discord.Intents.default()
intents.message_content = True  
client = commands.Bot(command_prefix="!", intents=intents)


youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'noplaylist': 'True'
}
ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


@client.command()
async def play(ctx, url):
    try:
        
        if ctx.author.voice:
            voice_channel = ctx.author.voice.channel
            voice_client = await voice_channel.connect()
        else:
            await ctx.send("You need to be in a voice channel to play music!")
            return

        
        info = ytdl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        
        
        voice_client.play(discord.FFmpegPCMAudio(url2, **ffmpeg_options))
        await ctx.send(f"Now playing: {info['title']}")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@client.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Left the voice channel")
    else:
        await ctx.send("I'm not in a voice channel.")

client.run('MTMwMDI5NjE1ODgzMjM2NTU4OA.Gd5D0D.VWyQh0RWlsqGrGHAqbDMoc1zkf_quqFfAeJAOA')

