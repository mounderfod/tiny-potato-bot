import discord
from discord.ext import commands


async def parse_error(ctx, error):
    if hasattr(ctx.command, 'on_error'):
        return
    cog = ctx.cog
    if cog:
        if cog._get_overridden_method(cog.cog_command_error) is not None:
            return

    if isinstance(error, commands.CommandNotFound):
        pass
    else:
        embed = discord.Embed(title="An error occurred!", color=0xc71a1a)
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/798974923954978817.png?v=1")
        embed.add_field(name=type(error).__name__, value=error, inline=False)
        embed.set_footer(text="Tiny Potato Bot")
        await ctx.send(embed=embed)


class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=0xa37dca, description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)
