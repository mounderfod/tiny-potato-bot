import discord
import requests
from discord.ext import commands
import urllib.request
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="drama", brief="Wait, it's all discord-meta? Always has been.", help="""
    Fetches drama from various sources, all based on asiekierka's original generator.
    Valid sources:
    `fabric`: <http://fabric-drama.herokuapp.com>
    `forge`: <http://mc-drama.herokuapp.com>
    If no source (or an invalid source) is provided then a random one is picked from between the two.
    """)
    async def drama(self, ctx, source=None):
        url = ""
        if source == "fabric":
            url = "https://fabric-drama.herokuapp.com/txt"
        elif source == "forge":
            url = "https://mc-drama.herokuapp.com/raw"
        else:
            url = random.choice(["https://fabric-drama.herokuapp.com/txt", "https://mc-drama.herokuapp.com/raw"])
        response = urllib.request.urlopen(url).read().decode('utf-8')
        embed = discord.Embed(color=0xa37dca)
        embed.add_field(name=f"{ctx.author.name} caused drama!", value=response, inline=False)
        embed.set_footer(text="Tiny Potato Bot v1.0.0")
        await ctx.send(embed=embed)

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
