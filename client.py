from discord import client
from discord.ext import commands

print('Pomyślnie załadowano client.py')

client = commands.Bot(command_prefix=".")
client.remove_command("help")