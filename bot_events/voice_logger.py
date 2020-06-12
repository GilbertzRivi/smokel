from client import client
import variables as vrb
from discord import Embed
from functions import json_add, json_rem, read
from json import loads
from datetime import datetime

print('Pomyślnie załadowano voice_logger.py')

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        
        a = ''
        if vrb.fem in member.roles: 
            a = 'a'
        embed = Embed(colour=vrb.host.colour, timestamp=datetime.utcnow())

        if before.channel != None and after.channel != None:
            embed.add_field(name=f'{member.name} zmienił{a} kanał', value=f'{member.mention} ``{before.channel.name}`` **->** ``{after.channel.name}``')
        elif before.channel != None:
            embed.add_field(name=f'{member.name} opuścił{a} kanał', value=f'{member.mention} ``{before.channel.name}``')
        elif after.channel != None:
            embed.add_field(name=f'{member.name} dołączył{a} na kanał', value=f'{member.mention} ``{after.channel.name}``')

        embed.set_footer(text=f'{member.name} {member.id}', icon_url=member.avatar_url)
        await vrb.logs_chan_2.send(embed=embed)
