from client import client
from discord import Role
import variables as vrb
from functions import json_add, read
from json import loads

print('Pomyślnie załadowano exclude.py')

@client.command()
async def exclude(ctx, *, role: Role):
    if not vrb.adm_role in ctx.author.roles: return
    json_file = loads(read('config.json'))
    excluded = json_file['autoroles']['excluded']
    excluded.append(role.id)
    json_add('config.json', ['autoroles'], {'excluded': excluded}, True)
    await ctx.send('Pomyślnie dodałem rolę do wykluczonych')