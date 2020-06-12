from discord.ext import tasks
from client import client
from json import loads
from twitch import TwitchClient
import variables as vrb
from discord import Embed
from functions import read, json_add, json_rem
from datetime import datetime
from time import sleep, time
from random import randint, choice
from discord import Embed

print('Pomyślnie załadowano one_minute.py')
TwitchClient = TwitchClient(client_id='1rj0udj2r8t8ld47gv9pcc9dg6f95x')

@tasks.loop(minutes=1)
async def loop_1m():

    #twitch
    json_file = loads(read('twitch.json'))
    json_users = json_file['users']
    for json_user in json_users: 
        stream = TwitchClient.streams.get_stream_by_user(json_users[json_user]['id'])
        if stream != None:
            if json_users[json_user]["notyficated"] == 'no':
                dc_user = client.get_user(int(json_user))
                e = Embed(colour=vrb.host.color, timestamp=datetime.utcnow())
                e.set_thumbnail(url=dc_user.avatar_url)
                e.set_footer(icon_url=dc_user.avatar_url, text="Dołącz do streama ku uciesze autora!")
                e.add_field(name="Stream!", value=f"Użytkownik właśnie zaczął stream!\nWbij i zobacz co tam się dzieje\n{json_users[json_user]['channel_link']}")
                message = await vrb.ogloszenia_userow.send(embed=e)
                json_add('twitch.json', ['users', json_user, "notyficated"], "yes")
                json_add('twitch.json', ['users', json_user, "message_id"], message.id)
        elif stream == None and json_users[json_user]["notyficated"] == 'yes':
            async for msg in vrb.ogloszenia_userow.history(limit=100):
                if msg.id == json_users[json_user]["message_id"]:
                    await msg.delete()
                    break
            json_add('twitch.json', ['users', json_user], {"notyficated": "no", "message_id": None}, True)

    #eventy
    now = datetime.now().timestamp()
    json_file = loads(read('events.json'))
    events = json_file['all']['events']
    for event in events:
        if now > float(event):
            chan = client.get_channel(events[event]['cid'])
            msg = await chan.fetch_message(events[event]['mid'])
            opis = events[event]['desc']
            embed = Embed(title='Przypominajka o evencie!', timestamp=datetime.utcnow())
            embed.add_field(name=opis.split(' /// ')[0], value=' '.join(opis.split(' /// ')[1:]))
            for react in msg.reactions:
                async for user in react.users(limit=None, after=None):
                    if user != client.user:
                        try: await user.send(embed=embed)
                        except: pass
            json_rem('events.json', ['all', 'events', event])

    #usuwanie izolatek
    json_file = loads(read('config.json'))
    izolatki = json_file['izolatki']
    tnow = time()
    for izolatka_id in izolatki:
        if not int(izolatka_id) in [u.id for u in vrb.guild.members]:
            json_rem('config.json', ['izolatki', izolatka_id])
            json_file = loads(read('config.json'))
            izolatki = json_file['izolatki']
            continue
        if izolatki[izolatka_id]['time'] <= tnow:
            member = vrb.guild.get_member(int(izolatka_id))
            for r in izolatki[izolatka_id]['roles']:
                temp_rol = vrb.guild.get_role(r)
                await member.add_roles(temp_rol)
            await member.remove_roles(vrb.izolatka)
            json_rem('config.json', ['izolatki', izolatka_id])
