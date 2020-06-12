from client import client
import variables as vrb
from discord import Role
from functions import json_add, read, search_in_list
from time import time
from json import loads

print('Pomyślnie załadowano role_mention.py')

@client.command()
async def rment(ctx, *, role: Role):
    if not ctx.channel == vrb.game_chan:
        await ctx.send('To nie jest kanał od gier')
        return

    if not role in search_in_list(ctx.guild.roles[::-1], vrb.dividing_games, vrb.dividing_channels)[2:-1]:
        await ctx.send('To nie jest rola od gier')
        return

    await ctx.message.delete()

    roles = loads(read('commands/role_mentions.json'))['roles']
    c_time = time()

    if not str(role.id) in list(roles):
        json_add('commands/role_mentions.json', ['roles'], {str(role.id): c_time})
        await role.edit(mentionable = True)
        await ctx.send(f'{ctx.author.mention} wzmienia {role.mention}')
        await role.edit(mentionable = False)
        return

    for r_id in roles:
        if r_id == str(role.id):
            if c_time - roles[r_id] >= 3600:
                json_add('commands/role_mentions.json', ['roles'], {r_id: c_time})
                await role.edit(mentionable = True)
                await ctx.send(f'{ctx.author.mention} wzmienia {role.mention}')
                await role.edit(mentionable = False)
                return
            else: 
                how_long = int((3600 - (c_time - roles[r_id])) / 60)
                await ctx.send(f'Musisz jeszcze poczekać {how_long} minut aby znów oznaczyć tą rolę')
                return