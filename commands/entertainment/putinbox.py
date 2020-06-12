from discord.ext import commands
from json import loads
from discord import Member
from client import client
from functions import json_add, read

print('Pomyślnie załadowano putinbox.py')

@client.command()
async def putinbox(ctx, *, member: Member):
    json_file = loads(read('config.json'))
    put_in_box = json_file['put_in_box']
    if ctx.author.id in [put_in_box[key] for key in put_in_box]:
        await ctx.send('Wyczerpałeś swój limit wkładania futrzaków do pudełek na dziś')
        return
    if member.bot: 
        if member.id == client.user.id: await ctx.send('Ja ne ce do pudeuka :<')
        else: await ctx.send('Nie wsadzaj bota do pudełka :< on sam potem z niego nie umie wyjść')
        return
    json_add('config.json', ['put_in_box', str(ctx.author.id)], ctx.author.id)
    await ctx.send(f'*<@{ctx.author.id}> wkłada <@{member.id}> do pudełka* uwu')
    await member.edit(nick=f'{member.display_name} in a box')