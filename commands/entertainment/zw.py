from client import client
from functions import json_add, json_rem, read
from json import loads

print('Pomyślnie załadowano zw.py')

@client.command()
async def zw(ctx, *, info):
    if info == 'delete':
        try: 
            json_rem('commands/zw.json', ['dnd', str(ctx.author.id)])
            await ctx.send('Pomyślnie usunąłem twoje zw')
        except: await ctx.send('Aktualnie nie masz żadnego ustawionego zw')
    elif info == 'check':
        try:
            user_zw = loads(read('commands/zw.json'))['dnd'][str(ctx.author.id)]
            await ctx.send(f'Oto twoje obecne zw```{user_zw}```')
        except: await ctx.send('Aktualnie nie masz żadnego ustawionego zw')
    else:
        json_add('commands/zw.json', ['dnd'], {str(ctx.author.id): info}, True)
        await ctx.send('Pomyślnie zaktualizowałem twoje zw')