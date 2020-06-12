from client import client
from discord.utils import get
import variables as vrb
from json import loads
from functions import read, chk_list_cohesion, same_pos_in_lists

print('Pomyślnie załadowano raw_reaction.py')

@client.event
async def on_raw_reaction_add(payload):

    json_file = loads(read('config.json'))
    single_roles_orientations = json_file['autoroles']['single_roles_orientations']
    single_roles_colors = json_file['autoroles']['single_roles_colors']
    single_roles_hugel = json_file['autoroles']['single_roles_hugel']

    guild = client.get_guild(payload.guild_id)
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    member = guild.get_member(payload.user_id)

    if not channel == vrb.autoroles_chan1 and not channel == vrb.autoroles_chan2 or member == client.user: return
    if len(message.content.split('\n')) > 1: role_name = message.content.split('\n')[-1].split(' - ')[0][2:-2]
    elif len(message.embeds) == 0: role_name = message.content.split(' - ')[0][2:-2]
    else: role_name = message.embeds[0].fields[0].name
    role = get(guild.roles, name=role_name)

    if role.id in single_roles_colors and chk_list_cohesion([role.id for role in member.roles], single_roles_colors):
        for role_id in same_pos_in_lists([role.id for role in member.roles], single_roles_colors):
            try: await member.remove_roles(guild.get_role(role_id))
            except: pass
    
    if role.id in single_roles_orientations and chk_list_cohesion([role.id for role in member.roles], single_roles_orientations):
        for role_id in same_pos_in_lists([role.id for role in member.roles], single_roles_orientations):
            try: await member.remove_roles(guild.get_role(role_id))
            except: pass

    if role.id in single_roles_hugel and chk_list_cohesion([role.id for role in member.roles], single_roles_hugel):
        for role_id in same_pos_in_lists([role.id for role in member.roles], single_roles_hugel):
            try: await member.remove_roles(guild.get_role(role_id))
            except: pass

    await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):

    json_file = loads(read('config.json'))
    single_roles_orientations = json_file['autoroles']['single_roles_orientations']

    guild = client.get_guild(payload.guild_id)
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    member = guild.get_member(payload.user_id)

    if not channel == vrb.autoroles_chan1 and not channel == vrb.autoroles_chan2 or member == client.user: return
    if len(message.content.split('\n')) > 1: role_name = message.content.split('\n')[-1].split(' - ')[0][2:-2]
    elif len(message.embeds) == 0: role_name = message.content.split(' - ')[0][2:-2]
    else: role_name = message.embeds[0].fields[0].name
    role = get(guild.roles, name=role_name)
    
    await member.remove_roles(role)

    if role.id in single_roles_orientations and not chk_list_cohesion([role.id for role in member.roles], single_roles_orientations):
        await member.add_roles(vrb.nie_zarucham)