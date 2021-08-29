import discord
import requests
from discord.ext import commands
import urllib.request

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="drama", brief="Wait, it's all discord-meta? Always has been.", help="""
    Fetches drama from various sources, all based on asiekierka's original generator.
    Valid sources:
    `ftb`: <http://ftb-drama.herokuapp.com>
    `fabric`: <http://fabric-drama.herokuapp.com>
    `forge`: <http://mc-drama.herokuapp.com>
    """)
    async def drama(self, ctx, source):
        if source == "fabric":
            response = urllib.request.urlopen("https://fabric-drama.herokuapp.com/txt").read().decode('utf-8')
            await ctx.send(response)
        elif source == "ftb":
            try:
                response = urllib.request.urlopen("http://ftb-drama.herokuapp.com/txt").read().decode('utf-8')
                await ctx.send(response)
            except HTTPError:
                await ctx.send("This site is currently unavailable.")
        elif source == "forge":
            response = urllib.request.urlopen("https://mc-drama.herokuapp.com/raw").read().decode('utf-8')
            await ctx.send(response)
        else:
            await ctx.send(f'Could not find drama from source "{source}". Valid sources: `ftb`, `fabric`, `forge`.')

    @commands.command(name="mixinerror", brief="helpful Mixin errors when?", help="helpful Mixin errors when?")
    async def mixinerror(self, ctx):
        await ctx.send("https://i.imgur.com/bOLCsd4.png")

    @commands.command(name="xkcd", brief="Gets XKCD comics.", help="Gets comics from https://xkcd.com, with the given number.")
    async def xkcd(self, ctx, comic=None):
        if comic is None:
            try:
                response = requests.get('https://xkcd.com/info.0.json').json()
                embed = discord.Embed(title=f"XKCD {response['num']}: {response['safe_title']}", colour=0xa37dca)
                embed.set_image(url=response['img'])
                embed.set_footer(text=response['alt'])
                await ctx.send(embed=embed)
            except:
                raise commands.CommandInvokeError("Comic not found. The XKCD database may be down.")
        elif int(comic) == 0:
            raise commands.CommandInvokeError("Invalid comic number!")
        else:
            try:
                response = requests.get(f'https://xkcd.com/{comic}/info.0.json').json()
                embed = discord.Embed(title=f"XKCD {response['num']}: {response['safe_title']}", colour=0xa37dca)
                embed.set_image(url=response['img'])
                embed.set_footer(text=response['alt'])
                await ctx.send(embed=embed)
            except:
                raise commands.CommandInvokeError("Comic not found. The XKCD database may be down.")


def setup(bot):
    bot.add_cog(Fun(bot))
