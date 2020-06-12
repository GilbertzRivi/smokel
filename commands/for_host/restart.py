from client import client
import variables as vrb
from functions import chk_list_cohesion
from os import execl
from sys import executable, argv
from discord import Game

print('Pomyślnie załadowano restart.py')

@client.command()
async def restart(ctx):
    if not chk_list_cohesion(ctx.author.roles, vrb.management): return
    await ctx.send('Restartowanie...')
    await client.change_presence(activity=Game(name='restart...'))
    print('\n\n\n\n\nRESTART\n\n\n\n\n')
    execl(executable, executable, *argv)
