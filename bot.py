import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import utils

load_dotenv()
bot = commands.Bot(command_prefix="t!", activity=discord.Activity(name="for commands", type=discord.ActivityType.watching))
bot.help_command = utils.MyHelpCommand(command_attrs={'hidden':True})

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.display_name}!')

@bot.event
async def on_command_error(ctx, error):
    await utils.parse_error(ctx, error)
    
@bot.event
async def on_message(message):
    if client.user.mentioned_in(message):
        ctx = await bot.get_context(message)
        ctx.reply("<irritatered:766468833564688395>")
    await bot.process_commands(message)

def load_extensions(bot):
    extensions = ['cogs.fun', 'cogs.about', 'cogs.modrinth']
    if __name__ == '__main__':
        for i in extensions:
            bot.load_extension(i)

bot.load_extension('jishaku')
load_extensions(bot)
bot.run(os.getenv("TOKEN"))
