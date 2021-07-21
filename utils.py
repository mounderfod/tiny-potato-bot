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
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Missing arguments! Make sure you've passed the correct ones.", mention_author=False)
    elif isinstance(error, commands.MissingPermissions):
        await ctx.reply("You do not have permission to do that!", mention_author=False)
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.reply("I don't have permission to do this! Make sure you've configured my role properly.", mention_author=False)
    else:
        raise error

class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=0xa37dca, description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)