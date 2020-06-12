from client import client
import variables as vrb
from functions import chk_list_cohesion

print('Pomyślnie załadowano role_list.py')

@client.command()
async def rlist(ctx):
    if not chk_list_cohesion(ctx.author.roles, vrb.management): return
    await ctx.message.delete()
    role_list = ''
    licznik = 0
    for r in ctx.guild.roles[::-1]:
        if r.name == '@everyone': continue
        counter = 0
        for member in ctx.guild.members:
            if r in member.roles: counter += 1
        role_list += (f'\n{r.id} - {counter}     {r.name}')
        if licznik == 20:
            await ctx.channel.send(f'```{role_list}```')
            role_list = ''
            licznik = 0
        licznik += 1