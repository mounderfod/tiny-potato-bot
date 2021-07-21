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
            response = urllib.request.urlopen("http://ftb-drama.herokuapp.com/txt").read().decode('utf-8')
            await ctx.send(response)
        elif source == "forge":
            response = urllib.request.urlopen("https://mc-drama.herokuapp.com/raw").read().decode('utf-8')
            await ctx.send(response)
        else:
            await ctx.send(f'Could not find drama from source "{source}". Valid sources: `ftb`, `fabric`, `forge`.')

    @commands.command(name="mixinerror", brief="helpful Mixin errors when?", help="helpful Mixin errors when?")
    async def mixinerror(self, ctx):
        await ctx.send("https://i.imgur.com/bOLCsd4.png")

    @commands.command(name="xkcd", brief="Gets XKCD comics.", help="Gets comics from https://xkcd.com, with the given number.")
    async def xkcd(self, ctx, comic):
        if int(comic) == 0:
            await ctx.send("Invalid comic number!")
        if int(comic) == 1 and int(comic) != "1":
            await ctx.send("Invalid input!")
        else:
            try:
                response = requests.get(f'https://xkcd.com/{comic}/info.0.json').json()
                embed = discord.Embed(title=f"XKCD {response['num']}: {response['safe_title']}", colour=0xa37dca)
                embed.set_image(url=response['img'])
                embed.set_footer(text=response['alt'])
                await ctx.send(embed=embed)
            except:
                await ctx.send("An error occurred. This is most likely because you entered a number for a comic that doesn't exist.")


def setup(bot):
    bot.add_cog(Fun(bot))