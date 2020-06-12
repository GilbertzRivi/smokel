from client import client 
from discord.ext import commands
from functions import chk_list_cohesion, json_rem
import variables as vrb
from random import choice

print('Pomyślnie załadowano black_list_remove.py')
odpowiedzi = ['Roger that!', 'Tak jest', 'Zrozumiano', 'Dodałem', 'Done']

@client.command()
async def blire(ctx, id):
    if not chk_list_cohesion(ctx.author.roles, vrb.management):
        await ctx.send('Nie masz uprawnień')
        return
    try: id = int(id)
    except:
        await ctx.send('to nie liczba')
        return
    try: json_rem('config.json', ['black_list', str(id)])
    except:
        await ctx.send('W mojej bazie danych nie odnotowałem wpisu z podanym id')
        return
    await ctx.send(choice(odpowiedzi))