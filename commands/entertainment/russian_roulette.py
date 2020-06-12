from client import client
from random import choice, randint
import variables as vrb

print('Pomyślnie załadowano russian_roulette.py')

man_live = ['no niestety ale jeszcze żyjesz', 'pudło!', 'nie trafiłeś', 'dostałeś ku... drugą szansę', 'niestety jeszcze trochę się pomęczysz']
man_death = ['no niestety ale nie żyjesz', 'w dziesiatkę!', 'nie wiem czy mnie słyszysz ale dostałeś kulką', 'do zobaczenia po drugiej stronie']
fem_live = ['no niestety ale jeszcze żyjesz', 'pudło!', 'nie trafiłaś', 'dostałaś ku... drugą szansę', 'niestety jeszcze trochę się pomęczysz']
fem_death = ['no niestety ale nie żyjesz', 'w dziesiatkę!', 'nie wiem czy mnie słyszysz ale dostałaś kulką', 'do zobaczenia po drugiej stronie']

@client.command()
async def ruletka(ctx):
    zabity = ctx.guild.get_role(604034572358778900)
    if zabity in ctx.author.roles:
        await ctx.send('Ja wiem, że ta gra uzależnia ale jak jesteś martwy to mógłbyś sobie dać na wstrzymanie')
        return
    if choice([randint(1,6) for i in range(36)]) == 6:
        if vrb.fem in ctx.author.roles:
            await ctx.send(f'{ctx.author.mention} {choice(fem_death)}')
        else:
            await ctx.send(f'{ctx.author.mention} {choice(man_death)}')
        await ctx.author.add_roles(zabity)
    else:
        if vrb.fem in ctx.author.roles:
            await ctx.send(f'{ctx.author.mention} {choice(fem_live)}')
        else:
            await ctx.send(f'{ctx.author.mention} {choice(man_live)}')