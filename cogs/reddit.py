import os
import random

import asyncpraw
from dotenv import load_dotenv
from discord import ChannelType
from discord.ext import commands

load_dotenv()
reddit = asyncpraw.Reddit(
    client_id="60jDYF0yBOGlP0QCDvhFew",
    client_secret=os.getenv("SECRET"),
    user_agent="craftvoltage.tpbot:v1.0.0 (by u/craftvoltage)"
)


class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="reddit", brief="Gets images from Reddit.", help="""
    Fetches a random image or link from the 100 "hot" posts of the given subreddit. If the image/sub is NSFW then an NSFW Discord channel must be used.
    """, aliases=['redd', 'r'])
    async def redditimg(self, ctx, sub):
        sub = await reddit.subreddit(sub)
        img_posts = [i async for i in sub.hot(limit=100) if not i.is_self and i.domain != "v.redd.it"]
        if len(img_posts) == 0:
            await ctx.reply("This subreddit has no image posts!", mention_author=False)
        else:
            post = random.choice(img_posts)
            nsfw = post.over_18
            if nsfw and ctx.channel.type == ChannelType.text and not ctx.channel.is_nsfw():
                await ctx.reply("The selected post is NSFW, and this is not an NSFW channel.", mention_author=False)
            else:
                for i in get_image_embed(post):
                    await ctx.send(i)


def setup(bot):
    bot.add_cog(Reddit(bot))


def get_image_embed(post):
    result = ["Post by " + post.author.name + ": " + post.title]
    if hasattr(post, "is_gallery"):
        result.append("\nhttps://i." + list(post.media_metadata.values())[0]["p"][0]["u"].split('?')[0][16:])
    else:
        result.append("\n" + post.url)
    return result
