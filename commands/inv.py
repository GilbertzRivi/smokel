from json import loads
from discord.ext import commands
from client import client
from functions import json_add, read
from datetime import datetime
import variables as vrb

print('Pomyślnie załadowano inv.py')

@client.command()
async def inv(ctx):
    json_file = loads(read('config.json'))
    user_invs = json_file['user_invs']
    await ctx.message.delete()
    if ctx.author.id in [user_invs[key] for key in user_invs]:
        await ctx.send('Już dziś prosiłeś o jedno zaproszenie\nJeżeli chcesz więcej, poproś o nie kogoś z zarządu')
        return
    await ctx.channel.create_invite(max_age=1800, max_uses=1)
    zapki = await ctx.channel.invites()
    for i in zapki:
        if i.inviter == client.user and i.created_at.strftime('%M') == datetime.now().strftime('%M'):
            inv = i.code
    json_add('config.json', ['user_invs', str(ctx.author.id)], ctx.author.id)
    await ctx.author.send(f'Oto zaproszenie dla ciebie https://discord.gg/{inv}\nWażne 30 minut, jedno użycie')
    await vrb.tech_chan.send(f'Wysłałem zaproszenie do {ctx.author.name} aka {ctx.author.display_name}')
