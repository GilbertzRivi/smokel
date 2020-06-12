from client import client
from discord import Embed, TextChannel
from functions import json_add, read, chk_list_cohesion
import variables as vrb
from json import loads
from time import mktime
from datetime import datetime

print('Pomyślnie załadowano exclude.py')

@client.command()
async def set_event(ctx, chan: TextChannel, data, *, opis):
    if not chk_list_cohesion(ctx.author.roles, vrb.management):
        await ctx.send('Nie masz uprawnień')
        return
    
    event_timestamp = mktime(datetime.strptime(data, '%H/%d/%m/%Y').timetuple())

    def check(m):
        return m.content == 'tak' and m.author == ctx.author and m.channel == ctx.channel
    
    confirmation_date = datetime.fromtimestamp(event_timestamp).strftime('%H godzina %d dnia %m miesiaca %Y roku')
    await ctx.send(f"Wpisz tak aby potwierdzić, że datą wydarzenia ma być {confirmation_date}")

    try:
        await client.wait_for('message', timeout=30.0, check=check)
    except TimeoutError:
        await ctx.channel.send('Czas minął')
        return

    embed = Embed(title='Przypominajka o evencie!\nZareaguj a bot w dniu eventu przypomni Ci o nim na pw!', timestamp=ctx.message.created_at)
    embed.add_field(name=opis.split(' /// ')[0], value=' '.join(opis.split(' /// ')[1:]))

    message = await chan.send(embed=embed)
    await message.add_reaction('❤️')
    json_add('events.json', ['all', 'events'], {str(event_timestamp): {'desc': opis, 'cid':message.channel.id, 'mid':message.id}}, True)

    await ctx.send('Poprawnie dodałem wydarzenie do przypominajki')