from client import client
from discord import Member
from discord.ext import commands
from functions import chk_list_cohesion
import variables as vrb

print('Pomyślnie załadowano silent_ban_kick.py')

silent_ban_kick_user = None

@client.command()
async def sban(ctx, member: Member):
    global silent_ban_kick_user
    silent_ban_kick_user = member
    if not chk_list_cohesion(ctx.author.roles, vrb.management):
        return
    await member.ban(reason=ctx.author.name, delete_message_days=0)
    await ctx.send(f'Pomyślnie zbanowałem {member.name}')

@client.command()
async def skick(ctx, member: Member):
    global silent_ban_kick_user
    silent_ban_kick_user = member
    if not chk_list_cohesion(ctx.author.roles, vrb.management):
        return
    await member.kick(reason=ctx.author.name)
    await ctx.send(f'Pomyślnie wyrzuciłem {member.name}')