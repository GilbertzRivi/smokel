from discord.ext import commands
from discord import Member
from client import client

print('Pomyślnie załadowano unbox.py')

@client.command()
async def unbox(ctx, *, member: Member):
    box = 'in a box'.split(' ')
    if ctx.author == member:
        await ctx.send('Ni :3')
        return
    if box != member.display_name.split(' ')[-3:]:
        await ctx.send('Fuczak nie siedzi już w pudełku, nie możesz go z niego wyjąć')
        return
    await ctx.send(f'*<@{ctx.author.id}> wyciąga <@{member.id}> z pudełka* uwu')
    await member.edit(nick=' '.join(member.display_name.split(' ')[:-3]))