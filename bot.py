import os

from ezcord import discord
from ezcord.internal.dc import commands
from commands import setup as setup_commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.reactions = True

bot = commands.Bot(intents=intents, help_command=None)

setup_commands(bot)

bot.run(os.environ["DISCORD_TOKEN"])