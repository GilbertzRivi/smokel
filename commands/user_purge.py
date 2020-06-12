from client import client
from discord import Member

print('Pomyślnie załadowano user_purge.py')

@client.command()
async def upurge(ctx, amount, *, user: Member):
    try:
        amount = int(amount) + 1
    except:
        await ctx.channel.send("Twój argument jest inwalidą")
        return
    if ctx.channel.permissions_for(ctx.author).manage_messages:
        counter = 0
        async for message in ctx.channel.history(limit=10000):
            if message.author == user:
                await message.delete()
                counter += 1
            if amount <= counter:
                break