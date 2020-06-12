from client import client
from discord.ext import tasks
import variables as vrb
from random import randint, choice
from time import sleep
from datetime import datetime

print('Pomyślnie załadowano five_minutes.py')

compliments = 'Świetnie dziś wyglądasz, Gdybyś był ziemniakiem to byłbyś pięknym ziemniakiem uwu, Jesteś tak cudowny że z binarnego chce przejść na dziesiątkowy, Jesteś może inwalidą? Bo chyba połamałeś sobie nogi jak spadałeś z nieba aniele <:uwukitus:678641429383348254>, Nie pracujesz przypadkiem dla ISIS? Bo jesteś tak słodki że mógłbyś im robić za bombę kaloryczną <:kitusflushed:696779219430277201>'.split(', ')

@tasks.loop(minutes=5)
async def loop_5m():

    #komplementy
    if randint(1, 360) == 1:
        print('a')
        if not datetime.now().strftime('%H') in '10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24'.split(', '):
            return
        sleep(randint(1, 120))
        active_users = []
        async for msg in vrb.main_chan.history(limit=100):
            if not msg.author in active_users and not msg.author.bot:
                active_users.append(msg.author)
            if len(active_users) > 5:
                break
        await vrb.main_chan.send(f'{choice(compliments)} {choice(active_users).mention}')
