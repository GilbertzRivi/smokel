from client import client

print('Pomyślnie załadowano say.py')

@client.command()
async def say(ctx, *, args):
    if '@everyone' in args or '@here' in args or '<@&' in args:
        await ctx.send('Nie')
        return
    await ctx.message.delete()
    await ctx.send(args)
