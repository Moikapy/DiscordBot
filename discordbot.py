import os
import discord
from discord.ext import commands
from discord.ext.commands import has_role
from discord import Member
from discord.utils import get
import random
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
GUILD = os.environ.get("GUILD")
client = commands.Bot(command_prefix = '-')
#Connection info
@client.event
async def on_ready():
 print(f'{client.user.name} has connected to Discord!')