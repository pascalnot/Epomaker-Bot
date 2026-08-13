import os
 
from ezcord import discord
from ezcord.internal.dc import commands
 
from commands import setup as setup_commands
 
intents = discord.Intents.default()
intents.members = False
intents.message_content = False
intents.reactions = False
 
bot = commands.Bot(
    command_prefix="/",  # unused for slash commands, kept for compatibility
    intents=intents,
    help_command=None,
)
 
setup_commands(bot)
 
 
@bot.event
async def on_ready():
    await bot.tree.sync()


bot.run(os.environ["DISCORD_TOKEN"])
