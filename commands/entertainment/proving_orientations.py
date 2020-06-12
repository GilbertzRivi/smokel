from client import client
from functions import discord_file
from discord import Member

print('Pomyślnie załadowano proving_orientations.py')

@client.command()
async def gay(ctx, *, member: Member):
    await ctx.message.delete()
    await ctx.send(f"Udowodnione naukowo jest, ze {member.mention} jest homo", file=discord_file('resources/homo.png', 'homo.png', False))

@client.command()
async def hetero(ctx, *, member: Member):
    await ctx.message.delete()
    await ctx.send(f"Udowodnione naukowo jest, ze {member.mention} jest hetero", file=discord_file('resources/hetero.png', 'hetero.png', False))
