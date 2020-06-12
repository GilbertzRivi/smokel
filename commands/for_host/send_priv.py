from client import client
from discord import User
import variables as vrb 

print('Pomyślnie załadowano send_priv.py')

@client.command()
async def send_priv(ctx, user: User, *, content):
    if ctx.author != vrb.host: return
    await user.send(content)
    await ctx.send('Wysłano')