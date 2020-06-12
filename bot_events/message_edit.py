from client import client
import variables as vrb
from discord import Embed
from datetime import datetime

print("Pomyślnie załadowano on_message_edit.py")

@client.event
async def on_message_edit(before, after):
    if before.author.bot or before.content == after.content: return
    await client.process_commands(after)

    e = Embed(colour=after.author.colour, timestamp=datetime.utcnow())
    e.set_author(name=f"Wiadomosc edytowana")
    e.set_thumbnail(url=after.author.avatar_url)
    e.add_field(name="Kanał:", value=after.channel, inline=False)
    e.add_field(name='Przed', value=before.content, inline=False)
    e.add_field(name='Po', value=after.content, inline=False)
    e.set_footer(text=f'{after.author.name} {after.author.id}', icon_url=after.author.avatar_url)

    await vrb.logs_chan.send(embed=e)