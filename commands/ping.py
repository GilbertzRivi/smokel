from client import client

print('Pomyślnie załadowano ping.py')

@client.command()
async def ping(ctx):
    latency = int(client.latency*1000)
    await ctx.send(f'Pong, opóźnienie - {latency}ms')
