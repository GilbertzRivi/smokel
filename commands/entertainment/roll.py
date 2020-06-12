from discord.ext import commands
from client import client
from random import randint

print('Pomyślnie załadowano roll.py')

@client.command()
async def roll(ctx, *, num):
    try:
        num = int(num)
    except: 
        await ctx.send(f'{num} nie jest liczbą')
        return

    await ctx.send(f'wyrolowałeś {randint(1, num)} <:nice:668620480038567936>')