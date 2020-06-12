from client import client
import variables as vrb
from random import randint
from discord import Member, Embed
from discord.ext.commands import MissingRequiredArgument

print('Pomyślnie załadowano random_penis.py')

@client.command()
async def penis(ctx, *, member: Member):
    if vrb.fem in member.roles:
        await ctx.send('Ona nie ma penisa, jest płci pięknej. Choć w tych czasach nigdy nic nie wiadomo...')
        return
    dlugosc = randint(1, 20)
    e = Embed(color=ctx.author.color, name="beniz")
    e.add_field(name=f'Beniz {member.display_name}a', value='8'+'='*dlugosc+'D', inline=True)
    e.set_footer(text='Beniz tego pana, hehe, bo wiecie', icon_url=member.avatar_url)
    await ctx.send(embed=e)

@penis.error
async def penis_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        dlugosc = randint(1, 20)
        e = Embed(color=ctx.author.color, name="beniz")
        e.add_field(name=f'Beniz {ctx.author.display_name}a', value='8'+'='*dlugosc+'D')
        e.set_footer(text='Beniz tego pana, hehe, bo wiecie', icon_url=ctx.author.avatar_url)
        if vrb.fem in ctx.author.roles:
            await ctx.send('Kobieta z penisem <:zeco:643165689452167169>', embed=e)
            return
        await ctx.send(embed=e)

@client.command()
async def gayrate(ctx, *, member: Member):
    hom = randint(1, 100)
    if hom <= 20: emotka = ':unamused:'
    if hom <= 40 and hom > 20: emotka = ':confused:'
    if hom <= 60 and hom > 40: emotka = ':thinking:'
    if hom <= 80 and hom > 60: emotka = ':blush:'
    if hom < 100 and hom > 80: emotka = ':smirk:'
    if hom == 100: emotka = ':heart:'
    e = Embed(color=ctx.author.color, name="gejostwo")
    e.add_field(name=f'Gej rejt maszin', value=f'Gejostwo {member.display_name}a \nwynosi: {hom}% {emotka}')
    e.set_footer(text='Gejizm tego furasa, hehe, bo wiecie', icon_url=member.avatar_url)
    await ctx.send(embed=e)

@gayrate.error
async def gayrate_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        hom = randint(1, 100)
        if hom <= 20: emotka = ':unamused:'
        if hom <= 40 and hom > 20: emotka = ':confused:'
        if hom <= 60 and hom > 40: emotka = ':thinking:'
        if hom <= 80 and hom > 60: emotka = ':blush:'
        if hom < 100 and hom > 80: emotka = ':smirk:'
        if hom == 100: emotka = ':heart:'
        e = Embed(color=ctx.author.color, name="gejostwo")
        e.add_field(name=f'Gej rejt maszin', value=f'Gejostwo {ctx.author.display_name}a \nwynosi: {hom}% {emotka}')
        e.set_footer(text='Gejizm tego furasa, hehe, bo wiecie', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=e)

@client.command()
async def hetrate(ctx, *, member: Member):
    het = randint(1, 100)
    if het <= 20: emotka = ':unamused:'
    if het <= 40 and het > 20: emotka = ':confused:'
    if het <= 60 and het > 40: emotka = ':thinking:'
    if het <= 80 and het > 60: emotka = ':blush:'
    if het < 100 and het > 80: emotka = ':smirk:'
    if het == 100: emotka = ':heart:'
    e = Embed(color=ctx.author.color, name="heteryzm")
    e.add_field(name=f'Het rejt maszin', value=f'Heteryzm {member.display_name}a \nwynosi: {het}% {emotka}')
    e.set_footer(text='Herizm tego furasa, hehe, bo wiecie', icon_url=member.avatar_url)
    await ctx.send(embed=e)

@hetrate.error
async def hetrate_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):    
        het = randint(1, 100)
        if het <= 20: emotka = ':unamused:'
        if het <= 40 and het > 20: emotka = ':confused:'
        if het <= 60 and het > 40: emotka = ':thinking:'
        if het <= 80 and het > 60: emotka = ':blush:'
        if het < 100 and het > 80: emotka = ':smirk:'
        if het == 100: emotka = ':heart:'
        e = Embed(color=ctx.author.color, name="heteryzm")
        e.add_field(name=f'Het rejt maszin', value=f'Heteryzm {ctx.author.display_name}a \nwynosi: {het}% {emotka}')
        e.set_footer(text='Herizm tego furasa, hehe, bo wiecie', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=e)
