from client import client
from random import randint
from time import sleep

print('Pomyślnie załadowano loading_bar.py')

@client.command()
async def loading(ctx):
    message = await ctx.send('``'+'-'*25+'``')
    while message.content != '``'+'#'*25+'``':
        num = message.content.count('#')
        rand_num = randint(1,3) + num
        if rand_num > 25: rand_num = 25
        txt = '``'+rand_num*'#'+(25-rand_num)*'-'+'``'
        await message.edit(content=txt)
        sleep(0.5)
    await message.edit(content='Loading complete')
