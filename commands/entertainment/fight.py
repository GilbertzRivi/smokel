from client import client
from discord import Member, Embed
from functions import discord_file
from random import randint, choice
from time import sleep

print('Pomyślnie załadowano fight.py')
weapons = ['wloczni','AK-47','M4','glocka','patyka','kamienia','piesci','zupki chinskiej','dziwnie wygladajacych kuleczek','dzidy','lin','pily lancuchowej','sztyletu','noza']

@client.command()
async def fight(ctx, member: Member):
    if ctx.author == member:
        await ctx.send('*nom*', file=discord_file('resources/gryz_w_ogon.jpg', 'nom.jpg', False))
        return
    hpa = 100
    hpo = 100
    autor = ctx.author.display_name
    oponent = member.display_name
    e = Embed(color=ctx.author.color, timestamp=ctx.message.created_at)
    e.add_field(name=f'{autor} vs {oponent}', value='***fight!***', inline=False)
    e.add_field(name=autor, value=100, inline=True)
    e.add_field(name=oponent, value=100, inline=True)
    e.set_footer(text='O bogowie, walka!', icon_url=client.user.avatar_url)
    await ctx.send(embed=e)
    content = ''
    while True:
        msg = ''
        async for message in ctx.channel.history(limit=100):
            if message.author == client.user and message.embeds[0].timestamp == ctx.message.created_at:
                msg = message
                break

        for field in msg.embeds[0].fields:
            temp = ''
            for line in field.value.split('\n')[-6:]:
                temp += line + '\n'
            content = temp
            break

        damage = randint(1, 20)
        weapon = choice(weapons)
        text = f'**{autor}** uzyl **{weapon}** i zadal **{oponent}** {damage} obrazen'
        if damage > 15:
            text = f'Uderzenie krytyczne! **{autor}** uzyl **{weapon}** i zadal **{oponent}** {damage} obrazen'
        text = content + '\n' + text
        e.set_field_at(index=0, name=f'{autor} vs {oponent}', value=text, inline=False)
        hpo -= damage
        e.set_field_at(index=2, name=oponent, value=hpo, inline=True)
        await msg.edit(embed=e)
        if hpo <= 0:
            text2 = text + '\n' + '\n' + f'**{autor}** wygrywa!'
            e.set_field_at(index=0, name=f'{autor} vs {oponent}', value=text2, inline=False)
            e.set_field_at(index=2, name=oponent, value=0, inline=True)
            await msg.edit(embed=e)
            break
        await msg.edit(embed=e)
        sleep(1)
        
        msg = ''
        async for message in ctx.channel.history(limit=100):
            if message.author == client.user and message.embeds[0].timestamp == ctx.message.created_at:
                msg = message
                break

        for field in msg.embeds[0].fields:
            temp = ''
            for line in field.value.split('\n')[-6:]:
                temp += line + '\n'
            content = temp
            break

        damage2 = randint(1, 20)
        weapon2 = choice(weapons)
        text = f'**{oponent}** uzyl **{weapon2}** i zadal **{autor}** {damage2} obrazen'
        if damage2 > 15:
            text = f'Uderzenie krytyczne! **{oponent}** uzyl **{weapon2}** i zadal **{autor}** {damage2} obrazen'
        text = content + '\n' + text
        e.set_field_at(index=0, name=f'{autor} vs {oponent}', value=text, inline=False)
        hpa -= damage2
        e.set_field_at(index=1, name=autor, value=hpa, inline=True)
        await msg.edit(embed=e)
        if hpa <= 0:
            text2 = text + '\n' + '\n' + f'**{oponent}** wygrywa!'
            e.set_field_at(index=0, name=f'{autor} vs {oponent}', value=text2, inline=False)
            e.set_field_at(index=1, name=autor, value=0, inline=True)
            await msg.edit(embed=e)
            break
        await msg.edit(embed=e)
        sleep(1)