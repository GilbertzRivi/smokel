from client import client
from discord import Role, Member
from functions import chk_list_cohesion
import variables as vrb

print('Pomyślnie załadowano add_role.py')

@client.command()
async def addrole(ctx, member: Member, *, role: Role):
    if not chk_list_cohesion(ctx.author.roles, vrb.management):
        await ctx.send('Nie masz uprawnień')
        return
    await member.add_roles(role, reason=ctx.author.name)
    await ctx.send(f'Pomyślnie nadano rolę {role.name} użytkownikowi {member.name}')