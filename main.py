import discord
from discord.commands import Option
import os


# Config:

debug_guilds=1084482528842366976
token=""


status = discord.Status.dnd
activity = discord.Activity(type=discord.ActivityType.playing, name="Python")

bot = discord.Bot(
    intents=discord.Intents.all(),
    debug_guilds=debug_guilds,
    status=status,
    activity=activity
)

if __name__ == "__main__":
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")


bot.run(token)
