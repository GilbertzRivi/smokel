from discord.ext import tasks
from client import client
from functions import json_rem, read
from json import loads
from datetime import datetime
from discord import Embed
import variables as vrb

print('Pomyślnie załadowano ten_minutes.py')

@tasks.loop(seconds=15)
async def loop_10m():
    now = datetime.now().timestamp()
    json_file = loads(read('events.json'))
    events = json_file['all']['events']
    for event in events:
        print(now, float(event), now > float(event))
        if now > float(event):
            temp = 0
            chan = client.get_channel(events[event]['cid'])
            msg = await chan.fetch_message(events[event]['mid'])
            opis = events[event]['desc']
            embed = Embed(title='Przypominajka o evencie!', timestamp=datetime.utcnow())
            embed.add_field(name=opis.split(' /// ')[0], value=' '.join(opis.split(' /// ')[1:]))
            react_num = len(msg.reactions)
            for react in msg.reactions:
                async for user in react.users(limit=None, after=None):
                    if user == client.user: continue
                    try:
                        await user.send(embed=embed)
                        temp += 1
                    except: 
                        pass
            json_rem('events.json', ['all', 'events', event])
        await vrb.host.send(f'Wysłano wiadomości przypominające do {temp} osób, zareagowało {react_num} osób\n**Nie zapomnij pousuwać 3 części kodu z tej komendy po przeprowadzeniu testu!**')