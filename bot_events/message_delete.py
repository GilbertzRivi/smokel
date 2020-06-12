from client import client
from datetime import datetime
from time import time
from discord import Embed
import variables as vrb
from functions import discord_file
from os import remove

print('Pomyślnie załadowano message_delete.py')

snipe = {"author": None, "content": None, "id": None}

@client.event
async def on_message_delete(message):
    global snipe
    attachments_saveing_channel = client.get_channel(555876098819227649)
    if '-hug' in message.content or '-lick' in message.content or '-pat' in message.content or '-boop' in message.content or '-kiss' in message.content or message.channel.id == 559910981392793601: return
    if message.author.bot: return

    snipe = {"author": message.author.name, "content": message.content, "id": message.author.id}
    e = Embed(colour=message.author.color, timestamp=datetime.utcnow())
    e.set_thumbnail(url=message.author.avatar_url)
    e.set_author(name=f"Wiadomosc usunięta")
    e.add_field(name='Kanał', value=message.channel, inline=False)
    if len(message.content) > 0:
        e.add_field(name='Treść', value=message.content, inline=False)
    else:
        e.add_field(name='Treść', value='Brak zawartości', inline=False)
    e.set_footer(text=f'{message.author.name} {message.author.id}', icon_url=message.author.avatar_url)
    try:
        await vrb.logs_chan.send(embed=e)
    except: pass
    if len(message.attachments) > 0:
        await vrb.logs_chan.send('Załączniki załączone do wiadomości')
        for a in message.attachments:
            await a.save(fp=a.filename, use_cached=True)
            saveing_file = discord_file(a.filename, a.filename, False)
            saveing_msg = await attachments_saveing_channel.send(file=saveing_file)
            a_url = saveing_msg.attachments[0].url
            ea = Embed(colour=vrb.host.colour, timestamp=datetime.utcnow())
            ea.set_footer(text=f'{message.author.name} {message.author.id}', icon_url=message.author.avatar_url)
            ea.set_author(name='Pliki załączone do wiadomości')
            ea.set_image(url=a_url)
            await vrb.logs_chan.send(embed=ea)
            remove(a.filename)

@client.event
async def on_bulk_message_delete(messages):
    attachments_saveing_channel = client.get_channel(555876098819227649)
    for message in messages:    
        if message.channel.id == 559910981392793601: return
        e = Embed(colour=message.author.color, timestamp=datetime.utcnow())
        e.set_author(name=f"Wiadomosc usunięta")
        e.add_field(name='Kanał', value=message.channel, inline=False)
        if len(message.content) > 0:
            e.add_field(name='Treść', value=message.content, inline=False)
        else:
            e.add_field(name='Treść', value='Brak zawartości', inline=False)
        e.set_footer(text=f'{message.author.name} {message.author.id}', icon_url=message.author.avatar_url)
        try:
            await vrb.logs_chan.send(embed=e)
        except: pass
        if len(message.attachments) > 0:
            await vrb.logs_chan.send('Załączniki załączone do wiadomości')
            for a in message.attachments:
                await a.save(fp=a.filename, use_cached=True)
                saveing_file = discord_file(a.filename, a.filename, False)
                saveing_msg = await attachments_saveing_channel.send(file=saveing_file)
                a_url = saveing_msg.attachments[0].url
                ea = Embed(colour=vrb.host.colour, timestamp=datetime.utcnow())
                ea.set_footer(text=f'{message.author.name} {message.author.id}', icon_url=message.author.avatar_url)
                ea.set_author(name='Pliki załączone do wiadomości')
                ea.set_image(url=a_url)
                await vrb.logs_chan.send(embed=ea)
                remove(a.filename)
    