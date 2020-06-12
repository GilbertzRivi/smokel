from client import client
import variables as vrb

print('Pomyślnie załadowano help.py')

@client.command()
async def help(ctx):
    await ctx.send(f'Wszystkie moje komendy znajdziesz na <#584054176607371284>, jeżeli potrzebujesz pomocy z którąś z nich, napisz do właściciela serwera - {vrb.host}')