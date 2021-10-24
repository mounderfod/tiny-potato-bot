import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
import bot_utils
import cogs.fun as F
import cogs.utils as U
import cogs.modrinth as M
import cogs.reddit as R

load_dotenv()
bot = commands.Bot(command_prefix="t!", activity=nextcord.Activity(name="for commands", type=nextcord.ActivityType.watching))
bot.help_command = bot_utils.MyHelpCommand(command_attrs={'hidden':True})


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
        await ctx.reply("<:irritater:882309845427036230>")
    await bot.process_commands(message)

F.setup(bot)
R.setup(bot)
M.setup(bot)
U.setup(bot)
bot.run(os.getenv("TOKEN"))
