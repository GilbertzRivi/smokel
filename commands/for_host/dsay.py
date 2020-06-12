from discord.ext import commands
from discord import TextChannel
from client import client
import variables as vrb

print('Pomyślnie załadowano dsay.py')

@client.command()
async def dsay(ctx, channel: TextChannel, *, args):
    if ctx.author != vrb.host: return
    await ctx.message.delete()
    await channel.send(args)