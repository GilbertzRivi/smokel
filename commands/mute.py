from discord.ext import commands
from discord import Member
from client import client
from functions import chk_list_cohesion, read, write, json_add
import variables as vrb
from time import time
from datetime import datetime

print('Pomyślnie załadowano mute.py')

@client.command()
async def mute(ctx, member: Member, *, mtime):
    if not chk_list_cohesion(ctx.author.roles, vrb.management):
        if ctx.author == member:
            pass
        else:
            await ctx.send('Nie masz uprawnień')
            return
    if chk_list_cohesion(member.roles, vrb.management):
        await ctx.send('Nie zmutuje nikogo z zarządu <:wtfkitus:593015681084030997>')
        return

    try:
        wtime = 0
        for i in mtime.split(' '):
            if 'd' in i:
                wtime += int(i.strip('d')) * 86400
            elif 'h' in i:
                wtime += int(i.strip('h')) * 3600
            elif 'm' in i:
                wtime += int(i.strip('m')) * 60
    except:
        await ctx.send('Twój argument jest inwalidą')
        return

    chan_roles_id = []
    for i in member.roles:
        if i in vrb.role_nsfw or i in vrb.orientations or i == vrb.futrzak:
            await member.remove_roles(i)
            chan_roles_id.append(i.id)
    await member.add_roles(vrb.izolatka)
    
    acttime = time()
    date = datetime.fromtimestamp(acttime+wtime).strftime('%d/%m/%Y, %H:%M')
    json_add('config.json', ['izolatki', str(member.id)], {'roles': chan_roles_id, 'time': time()+int(wtime)})
    await ctx.send(f'pomyślnie nadałem izolatkę {member.mention} do {date}')
    await member.send(f'Zostałeś wyciszony na serwerze do {date}')
