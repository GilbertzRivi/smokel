from client import client
from random import randint

print('Pomyślnie załadowano random_spaces.py')

@client.command()
async def rspac(ctx, * args):
    await ctx.message.delete()
    args = ''.join(args)
    output = ''
    for i in args:
        output += i + randint(0,10)*' '
    await ctx.send('**'+output+'**')