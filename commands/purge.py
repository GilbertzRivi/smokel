from client import client

print('Pomyślnie załadowano purge.py')

@client.command()
async def purge(ctx, amount):
    try:
        amount = int(amount) + 1
    except:
        await ctx.channel.send("Twój argument jest inwalidą")
        return
    if ctx.channel.permissions_for(ctx.author).manage_messages:
        if amount > 99:
            purge_times = int(amount/99)
            rest = amount%99
            for i in range(purge_times):
                await ctx.channel.purge(limit=99)
            await ctx.channel.purge(limit=rest)
        else: 
            await ctx.channel.purge(limit=amount)