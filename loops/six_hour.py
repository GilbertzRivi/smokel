from discord.ext import tasks
from client import client
from functions import json_rem, read
from json import loads

print('Pomyślnie załadowano six_hours.py')

@tasks.loop(hours=6)
async def loop_6():
    json_file = loads(read('config.json'))
    put_in_box = json_file['put_in_box']
    for i in put_in_box:
        json_rem('config.json', ['put_in_box', i])