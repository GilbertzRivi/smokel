from client import client
import variables as vrb

print('Pomyślnie załadowano off.py')

@client.command()
async def off(ctx):
    global off
    if ctx.author != vrb.host: return
    off = True
    await client.close()