from client import client
from discord import Member, Color
from functions import chk_list_cohesion
import variables as vrb

print('Pomyślnie załadowano new_role.py')

@client.command()
async def nrole(ctx, member: Member, color: Color, *, name):
    if not chk_list_cohesion(ctx.author.roles, vrb.management):
        await ctx.send('Nie masz uprawnień')
        return
    rol = await ctx.guild.create_role(name=name, colour=color)
    await member.add_roles(rol, reason=ctx.author.name)
    await ctx.send(f'Pomyślnie stworzono rolę {name} i nadano ją użytkownikowi {member.name}')
