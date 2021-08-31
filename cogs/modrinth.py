import discord
from discord.ext import commands
import requests, datetime, math

class Modrinth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="modrinthmod", brief="Finds a given mod on Modrinth.", help="""Finds a given mod on Modrinth.
    You can provide either the slug (`fabric-for-fabric`) or the project ID (`u6KTKg89`).
    If you get a JSONDecodeError it's because the mod could not be found!""", aliases=['mrmod', 'modrmod'])
    async def modrinth_mod(self, ctx, mod): # 5da426
        response = requests.get(f'https://api.modrinth.com/api/v1/mod/{mod}').json()
        embed = discord.Embed(title = response['title'], url=f'https://modrinth.com/mod/{mod}', description = response['description'], color = 0x5da426)
        embed.set_thumbnail(url = response['icon_url'])
        embed.add_field(name='Mod ID', value = response['id'], inline=True)
        embed.add_field(name='Categories', value = ', '.join(response['categories']), inline=True)
        embed.add_field(name='Downloads', value = response['downloads'], inline=True)
        embed.set_footer(text='Tiny Potato Bot')
        await ctx.send(embed=embed)

    @commands.command(name="modrinthuser", brief="Finds a given user on Modrinth.", help="""Finds a given user on Modrinth.
        You can provide either the username (`redcreeper14385`) or the user ID (`pdimDmDX`).
        If you get a JSONDecodeError it's because the user could not be found!""", aliases=['mruser', 'modruser'])
    async def modrinth_user(self, ctx, user):  # 5da426
        response = requests.get(f'https://api.modrinth.com/api/v1/user/{user}').json()
        embed = discord.Embed(title=response['username'], url=f'https://modrinth.com/user/{user}',
                              description=response['bio'], color=0x5da426)
        embed.set_thumbnail(url=response['avatar_url'])
        embed.add_field(name='User ID', value=response['id'], inline=True)
        embed.add_field(name='Registered', value=f"<t:{math.trunc(datetime.datetime.fromisoformat(response['created'].replace('Z', '')).timestamp())}:R>", inline=True)
        embed.add_field(name='Role', value=response['role'].capitalize(), inline=True)
        embed.set_footer(text='Tiny Potato Bot')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Modrinth(bot))