from client import client
from functions import json_add, read, discord_file, chk_list_cohesion
from os.path import isfile
import variables as vrb
from json import loads
from random import choice, randint
from time import sleep, time
from discord import Embed
from functions import discord_file

print('Pomyślnie załadowano logger_save.py')

responses = {
    "alkoholizm": "że Geralt?",
    "degeneractwo": "Miałeś na myśli Gilberta?",
    "i chuj": "Ci w dupę <:kitus:531348685766787077>",
    "pedał": "Michał, wołają cię",
    "tak było": "https://imgur.com/a/aknRN3C",
    "gówniarz": "<@479271213030572055> wołają cię",
    "gówniarzu": "<@479271213030572055> wołają cię"
}

@client.event
async def on_message(message):

    await client.process_commands(message)

    if message.author != client.user and not message.mention_everyone:

        if message.author.id == vrb.geralt_id:
            if 'pizda' in message.content.lower() or 'pizdo' in message.content.lower() or 'pizdą' in message.content.lower() or 'pizdy' in message.content.lower():
                await message.channel.send('Pizda <:harold:625405098255843331>', file=discord_file(f'resources/gerwazy_pizda{randint(1,3)}.png', 'gerwazy.png', True))

        if message.content.lower().startswith("rawr"):
            await message.channel.send(choice(["RAWRR!", 'ror']))

        if message.content.lower().startswith("awoo"):
            await message.channel.send(f'*Awo{randint(3, 19)*"o"}!*')
        
        if message.content.split(' ')[0].lower() == "f":
            num = loads(read('config.json'))['counters']['f'] + 1
            if vrb.fem in message.author.roles:
                ending = "oddała"
            else:
                ending = "oddał"
            dedycation = message.content.split(' ')[1:]
            if len(dedycation) > 0:
                if 'dla' in [i.lower() for i in dedycation]:
                    dedycation = ' '.join(dedycation)
                else:
                    dedycation = 'dla ' + ' '.join(dedycation)
            if randint(1, 40) == 10:
                F = discord_file('resources/f.jpg', 'f.jpg', False)
                if len(dedycation) == 0:
                    await  message.channel.send(f"{message.author.display_name} {ending} honory\nHonory oddane w sumie: {num}", file=F)
                else:
                    await  message.channel.send(f'{message.author.display_name} {ending} honory {dedycation}\nHonory oddane w sumie: {num}', file=F)
            else:
                if len(dedycation) == 0:
                    await  message.channel.send(f"{message.author.display_name} {ending} honory\nHonory oddane w sumie: {num}")
                else:
                    await  message.channel.send(f'{message.author.display_name} {ending} honory {dedycation}\nHonory oddane w sumie: {num}')
            json_add('config.json', ['counters', 'f'], num)
        
        if "owo whats this" in message.content or "owo what's this" in message.content:
            owo_whats_this = discord_file('resources/owo.gif', 'owo.gif', False)
            await message.channel.send(file=owo_whats_this)
        
        if message.content.lower() == "whym":
            await message.channel.send("Whymming in progress")
            async for msg in message.channel.history(limit=5):
                if msg.content == "Whymming in progress":
                    break
            for i in range(9):
                await msg.edit(content=f'Whymming in progress{(i%3+1)*"."}')
                sleep(1)
            await msg.edit(content='Whymming complete!', delete_after=5)
        
        bad_words = loads(read('config.json'))['bad_words']
        bad_words_num = loads(read('config.json'))['counters']['bad_words']
        if chk_list_cohesion(bad_words, [i.lower() for i in message.content.split(' ')]):
            counter = 0
            for word in message.content.split(' '):
                if word.lower() in bad_words:
                    counter += 1
            bad_words_num += counter
            json_add('config.json', ['counters', 'bad_words'], bad_words_num)

        if message.content == '.u w u': 
            await message.delete()
            await message.channel.send('u w  u')
            async for msg in message.channel.history(limit=5):
                if msg.content == "u w  u":
                    break
            for i in range(10):
                if i%2 == 0:
                    await msg.edit(content='u  w u')
                else: 
                    await msg.edit(content='u w  u')
                sleep(0.5)
            await msg.delete()

        if message.content.count('kobiet') > 0:
            num = randint(1,100)
            if num == 50:
                await message.channel.send('jezu fuj, weź, kobiety <:tfu:614167432172535831>')

    if len(message.mentions) > 7:
        mentions_no_duplicates = []
        for i in message.mentions:
            if not i in mentions_no_duplicates:
                mentions_no_duplicates.append(i)
        if len(mentions_no_duplicates) > 10:
            message_member = message.guild.get_member(message.author.id)
            try: message_member.remove_roles(vrb.futrzak)
            except: pass
            try: message_member.remove_roles(vrb.nowy)
            except: pass
            await message_member.add_roles(vrb.izolatka)
            for i in vrb.nsfw_chans:
                try: await message_member.remove_roles(i)
                except: pass
            await vrb.tech_chan.send(f'{message.author.mention} oznaczyl wiecej niz 10 osob i dostal izloatke')

    if len(message.mentions) > 0 and client.get_user(614628305047388161) != message.author and message.content[0] != '-' and message.author != client.user:
        for member in message.mentions:
            if str(member.status) == 'idle':
                async for msg in message.channel.history(limit=25):
                    if msg.author.id == member.id:
                        return
                json_file = loads(read('commands/zw.json'))
                if str(member.id) in json_file['dnd']:
                    info = json_file['dnd'][str(member.id)]
                    e = Embed(color=member.color, timestamp=message.created_at)
                    e.set_author(name=f"Użytkownik afk")
                    e.set_thumbnail(url=member.avatar_url)
                    e.add_field(name=f"{member.display_name} jest afk, zostawił wiadomość", value=info)
                    e.set_footer(text='Wiadomość została zostawiona', icon_url=member.avatar_url)
                    await message.channel.send(embed=e)

    if message.content.lower() in responses and message.author != client.user:
        await message.channel.send(responses[message.content.lower()])