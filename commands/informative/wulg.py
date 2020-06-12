from client import client
from json import loads 
from functions import read

print('Pomyślnie załadowano wulg.py')

@client.command()
async def wulg(ctx):
    json_file = loads(read('config.json'))
    wulg = json_file['counters']['bad_words']
    await ctx.send(f'Ilość wulgaryzmów jakie udało mi się odnotować to {wulg}')