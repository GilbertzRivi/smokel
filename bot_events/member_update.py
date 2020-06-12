from client import client
import variables as vrb
from functions import introducion

print('Pomyślnie załadowano member_update.py')

@client.event
async def on_member_update(before, after):
    if not before.roles == after.roles:
        if vrb.nowy in after.roles and vrb.nowy not in before.roles:
            await vrb.intro.send(introducion(after))