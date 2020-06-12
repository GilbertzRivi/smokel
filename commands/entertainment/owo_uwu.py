from client import client
from functions import discord_file

print('Pomyślnie załadowano owo_uwu.py')

@client.command()
async def owo(ctx):
    await ctx.message.delete()
    file = discord_file('resources/owo.png', 'owo.png', False)
    await ctx.send(file=file)

@client.command()
async def uwu(ctx):
    await ctx.message.delete()
    file = discord_file('resources/uwu.png', 'uwu.png', False)
    await ctx.send(file=file)