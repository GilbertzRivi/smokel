from discord import Game
from time import sleep
from variables import setup, token
import functions
from commands.mute import mute
from commands.black_list_add import bliad
from commands.black_list_remove import blire
from commands.ban_kick import ban, kick
from commands.autoroles import autorole, atrol
from commands.exclude import exclude
from commands.role_list import rlist
from commands.inv import inv
from commands.purge import purge
from commands.user_purge import upurge
from commands.new_role import nrole
from commands.add_role import addrole
from commands.ping import ping
from commands.help import help
from commands.twitch import twitch, remove_twitch
from commands.role_mention import rment
from commands.events import set_event
from commands.for_host.dsay import dsay
from commands.for_host.all_roles import give_roles
from commands.for_host.send_priv import send_priv
from commands.for_host.off import off
from commands.for_host.restart import restart
from commands.for_host.silence import silence
from commands.informative.user_info import uinf, inf
from commands.informative.role_info import rinf
from commands.informative.avatar import av
from commands.informative.emoji import em
from commands.informative.server import sinf
from commands.informative.wulg import wulg
from commands.informative.orientations import orient
from commands.entertainment.snipe import snipe
from commands.entertainment.zw import zw
from commands.entertainment.putinbox import putinbox
from commands.entertainment.unbox import unbox
from commands.entertainment.russian_roulette import ruletka
from commands.entertainment.reaction_meme import rmem
from commands.entertainment.proving_orientations import gay, hetero
from commands.entertainment.fight import fight
from commands.entertainment.wide_text import stxt
from commands.entertainment.owo_uwu import owo, uwu
from commands.entertainment.calculator import calc
from commands.entertainment.kill_unkill import kill, unkill
from commands.entertainment.random_spaces import rspac
from commands.entertainment.random_penis import penis, gayrate, hetrate
from commands.entertainment.ask_choice_etc import ask, choice 
from commands.entertainment.say import say
from commands.entertainment.loading_bar import loading
from commands.entertainment.papryka import gimp_papryka
from commands.entertainment.roll import roll
from loops.half_hour import loop_30
from loops.one_hour import loop_1
from loops.six_hour import loop_6
from loops.five_minutes import loop_5m
from loops.one_minute import loop_1m
from bot_events.member_join import on_member_join
from bot_events.member_leave import on_member_remove
from bot_events.raw_reaction import on_raw_reaction_add, on_raw_reaction_remove
from bot_events.on_message import on_message
from bot_events.member_update import on_member_update
from bot_events.voice_logger import on_voice_state_update
from bot_events.message_delete import on_message_delete, on_bulk_message_delete
from bot_events.message_edit import on_message_edit
from client import client
import commands.for_host.off as off

print('Pomyślnie załadowano main.py')
print('Inicjacja biblioteki discord')

@client.event
async def on_connect():
    print('Uzyskano połączenie z discordem')
    await client.wait_until_ready()
    print('Pomyślnie załadowano pamieć cache')
    await client.change_presence(activity=Game(name='.help'))
    if not setup(client):
        return
    print(f"Zalogowano jako {client.user.name}")
    loop_5m.start()
    loop_1m.start()
    loop_30.start()
    loop_1.start()
    loop_6.start()

@client.event
async def on_disconnect():
    print('Utracono połączenie z discordem')

@client.event
async def on_resumed():
    print('Wznowiono połączenie z discordem')
    print('Test zmiennych globalnych')
    setup(client)
    print('Ukończyłem test zmiennych globalnych')
    await client.change_presence(activity=Game(name='.help'))

while not off.off == True:
    client.run(token)
    if not off.off == True:
        print('Wznawianie połączenia z discordem za 10 sekund')
        sleep(10)