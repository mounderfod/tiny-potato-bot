import nextcord
from nextcord.ext import commands

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="about", brief="Gives information about the bot.", help="Gives information about the bot.")
    async def about(self, ctx):
        embed = nextcord.Embed(title="Tiny Potato Bot",
                              description="The creator of Tiny Potato Bot is mounderfod (aka redcreeper14385), find him here:",
                              color=0xa37dca)
        embed.add_field(name="GitHub", value="https://github.com/redcreeper14385", inline=False)
        embed.add_field(name="Twitch", value="https://twitch.tv/mounderfod", inline=False)
        embed.add_field(name="Discord", value="mounderfod#4179", inline=False)
        embed.add_field(name="Reddit", value="https://www.reddit.com/user/mounderfod", inline=False)
        embed.set_footer(text="Tiny Potato Bot v1.0.0")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Utils(bot))