from datetime import datetime, timezone, timedelta
import asyncio
import json
import os

from ezcord import discord
from ezcord.internal.dc import commands, tasks
from commands import setup as setup_commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.reactions = True

# neuer ! command
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# commands
setup_commands(bot)

bot.run(os.environ["DISCORD_TOKEN"])