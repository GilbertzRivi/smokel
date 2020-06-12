import discord
from client import client
from functions import discord_file
from json import loads
from time import time, sleep
import bot_events.member_join as join
import variables as vrb
import commands.ban_kick as bk
import commands.silent_ban_kick as sbk

print('Pomyślnie załadowano member_leave.py')

@client.event
async def on_member_remove(member):
    if sbk.silent_ban_kick_user == member: return
    if bk.kicked_user == member: 
        image = discord_file('resources/kicked.png', 'Wyjebało jak gagarina.png', False)
        await vrb.main_chan.send(f'A co to? Czy to ptak? Czy to samolot? Nie to {member.name} został wyjebany na orbitę niczym gagarin w 1961', file=image)
        return
    bans = await member.guild.bans()
    if member.id in [ban.user.id for ban in bans]:
        image = discord_file('resources/banned.gif', 'Only gulag for ya~.gif', False)
        await vrb.main_chan.send(f'{member.name} dostał bana', file=image)
        return
    try:
        if time() - join.member_join_time < 60:
            try:
                async for msg in vrb.main_chan.history(limit=100):
                    if member.mention in msg.content and msg.author == client.user: await msg.delete()
            except: pass
            image = discord_file('resources/left_fast.gif', 'To było szybkie.gif', False)
            await vrb.main_chan.send(f'{member.name} niestety nie wytrzymał presji weryfikacji', file=image)
            return
    except: pass
    image = discord_file('resources/left.png', 'Do zobaczenia.png', False)
    await vrb.main_chan.send(f'{member.name} opuścił serwer', file=image)
    sleep(5)
    temp = vrb.msg_num_chan.fetch_message(vrb.msg_num_chan.last_message_id).content.split(' ')
    if int(temp[0]) == member.id:
        wiad_num = temp[1]
        await vrb.tech_chan.send(f'Użytkownik {member.name} który właśnie opuścił serwer miał {wiad_num} wiadomości')