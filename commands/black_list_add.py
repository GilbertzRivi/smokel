from client import client 
from discord.ext import commands
from functions import chk_list_cohesion, json_add
import variables as vrb
from random import choice

print('Pomyślnie załadowano black_list_add.py')
odpowiedzi = ['Roger that!', 'Tak jest', 'Zrozumiano', 'Dodałem', 'Done']

@client.command()
async def bliad(ctx, id):
    if not chk_list_cohesion(ctx.author.roles, vrb.management):
        await ctx.send('Nie masz uprawnień')
        return
    try: id = int(id)
    except:
        await ctx.send('to nie liczba')
        return
    json_add('config.json', ['black_list', str(id)], id)
    await ctx.send(choice(odpowiedzi))