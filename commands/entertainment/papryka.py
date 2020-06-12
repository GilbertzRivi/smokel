from client import client
from functions import discord_file

print('Pomyślnie załadowano papryka.py')

@client.command()
async def gimp_papryka(ctx):
    papryka = discord_file('resources/papryka.png', 'gimp_papryka.png', True)
    await ctx.send(file=papryka)