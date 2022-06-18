import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import bot_utils
import cogs.fun as fun
import cogs.utils as utils

intents = discord.Intents(messages=True, guilds=True, members=True, presences=True, reactions=True)
load_dotenv()
bot = commands.Bot(command_prefix="t!",
                   activity=discord.Activity(name="for commands", type=discord.ActivityType.watching))
bot.help_command = bot_utils.MyHelpCommand(command_attrs={'hidden': True})


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.display_name}!')


@bot.event
async def on_command_error(ctx, error):
    await bot_utils.parse_error(ctx, error)


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        ctx = await bot.get_context(message)
        if not ctx.author.bot:
          await ctx.reply("no u")
    await bot.process_commands(message)


fun.setup(bot)
utils.setup(bot)
bot.run(os.getenv("TOKEN"))
