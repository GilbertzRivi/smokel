from client import client
from discord import Member
from discord.ext import commands
from functions import chk_list_cohesion
import variables as vrb

print('Pomyślnie załadowano ban_kick.py')

kicked_user = None

@client.command()
async def ban(ctx, member: Member):
    temp = False
    if not chk_list_cohesion(ctx.author.roles, vrb.management):
        if ctx.author == member:
            await ctx.send('No skoro tak ładnie prosisz')
            temp = True
        else:
            await ctx.send('Nie masz uprawnień')
            return
    if temp:
        await member.send('Nie no wracaj xD\nhttps://discord.gg/RY6wV3B')
    await member.ban(reason=ctx.author.name, delete_message_days=0)
    await ctx.send(f'Pomyślnie zbanowałem {member.name}')
    if temp:
        await member.unban()

@client.command()
async def kick(ctx, member: Member):
    global kicked_user
    kicked_user = member
    if not chk_list_cohesion(ctx.author.roles, vrb.management):
        await ctx.send('Nie masz uprawnień')
        return
    await member.kick(reason=ctx.author.name)
    await ctx.send(f'Pomyślnie wyrzuciłem {member.name}')
