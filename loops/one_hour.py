from json import loads
from discord.ext import tasks
from functions import read, json_rem, json_add
from client import client
from datetime import datetime
import variables as vrb

print('Pomyślnie załadowano one_hour.py')

@tasks.loop(hours=1)
async def loop_1():
    json_file = loads(read('config.json'))
    invitki = json_file['user_invs']

    #reset zaproszen
    if datetime.now().strftime('%H') == '05':
        for i in invitki:
            json_rem('config.json', ['user_invs', i])   
    
    #zapisywanie permisji kanałów
    for channel in vrb.guild.text_channels:
        if loads(read('commands/for_host/silence.json'))['silenced'] != True:
            json_add('commands/for_host/silence.json', ['saved_perms'], {str(channel.id): {}}, True)
            for role in channel.changed_roles:
                perms = dict(channel.overwrites_for(role))
                sorted_perms = {}
                for perm in perms:
                    if perms[perm] != None:
                        sorted_perms[perm] = perms[perm]
                json_add('commands/for_host/silence.json', ['saved_perms', str(channel.id)], {str(role.id): sorted_perms}, True)
