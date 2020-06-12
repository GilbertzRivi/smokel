from client import client
from functions import discord_file
from discord import Member
from discord.utils import get
import variables as vrb
from random import randint

print('Pomyślnie załadowano kill_unkill.py')

@client.command()
async def kill(ctx, *, member: Member):
    role = get(ctx.guild.roles, name='Zabity')
    if member == client.user:
        file = discord_file('resources/not_this_time.jpg', "nie tym razem.jpg", False)
        await ctx.send(file=file)
        return
    if member == vrb.host:
        if randint(1,4) == 2:
            await ctx.send(f'Niestety masz słaby aim i trafiłeś w ziemię, pocisk zrykoszetował i trafił cię prosto między oczy {ctx.author.mention}.\nGilbert oczywiście nie miał z tym nic wspólnego <:uszanowanko:625405180665659392>')
            await ctx.author.add_roles(role)
            return
    if ctx.author == member:
        if not role in ctx.author.roles:
            gun = discord_file('resources/gun.jpg', "pistolet.png", False)
            await ctx.send('Trzymaj, zabij się sam', file=gun)
        else:
            await ctx.send('Już nie żyjesz mordo')
    else:
        if role in ctx.author.roles:
            baton = discord_file('resources/ociebaton.jpg', "baton.png", False)
            await ctx.send('O cie baton, gadający trup', file=baton)
            return
        if not role in member.roles:
            await ctx.send(f'Zabiłem na chwilkę delikwenta pod nickiem {member.display_name}')
            await member.add_roles(role)
        else: await ctx.send('On już nie żyje, nie zabiję martwego')

@kill.error
async def kill_error(ctx, error):
    await ctx.send(file=discord_file('resources/who_to_kill.jpg', 'kogo_zabić.jpg', False))

@client.command()
async def unkill(ctx, *, member: Member):
    role = get(ctx.guild.roles, name='Zabity')
    if ctx.author == vrb.host and member == ctx.author:
        await member.remove_roles(role)
        await ctx.send('Do usług')
        return
    if ctx.author == member:
        if role in member.roles:
            await ctx.send('Oj chciałbyś <:kitus:531348685766787077>')
        else: await ctx.send('Przecież żyjesz')
    else:
        if role in ctx.author.roles:
            baton = discord_file('resources/ociebaton.jpg', "baton.png", False)
            await ctx.send('O cie baton, gadający trup', file=baton)
            return
        if role in member.roles:
            await ctx.send(f'Wskrzesiłem {member.display_name}, tyle bycia martwym powinno mu starczyć <:yee:581772500040548353>')
            await member.remove_roles(role)
        else: await ctx.send('On już żyje, jak chcesz możesz go zabić <:kitus:531348685766787077>')

@unkill.error
async def unkill_error(ctx, error):
    await ctx.send(file=discord_file('resources/who_to_unkill.jpg', 'kogo_zabić.jpg', False))
