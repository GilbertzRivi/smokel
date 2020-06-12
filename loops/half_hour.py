from discord.ext import tasks
from functions import search_in_list, chk_list_cohesion
from client import client
import variables as vrb

print('Pomyślnie załadowano half_hour.py')

@tasks.loop(minutes=30)
async def loop_30():
    guild = vrb.guild

    #nadawanie ról dzielących
    for i in guild.members:
        if i.bot: continue
        for r in vrb.dividing_roles:
            if not r in i.roles: await i.add_roles(r)

    #usuwanie zabitego
    for i in guild.members:
        for r in i.roles:
            if r.name == 'Zabity':
                await i.remove_roles(r)

    #ogarnianie roli "Nie Gra"
    for i in guild.members:
        if i.bot: continue
        user_games = search_in_list(i.roles[::-1], vrb.dividing_games, vrb.dividing_channels)
        user_games = user_games[1:-1]
        if vrb.nie_gra in user_games and len(user_games) > 1:
            await i.remove_roles(vrb.nie_gra)
        elif len(user_games) == 0:
            await i.add_roles(vrb.nie_gra)

    #nadawanie orientacji jak ktos nie ma
    for i in guild.members:
        if i.bot: continue
        if vrb.futrzak in i.roles:
            if not chk_list_cohesion(vrb.orientations, i.roles):
                await i.add_roles(vrb.nie_zarucham)
                
    #usuwanie ról od kanałów jak ktoś ma widzi wszystko
    for i in guild.members:
        if vrb.widzi_wszystko in i.roles:
            if chk_list_cohesion(vrb.role_nsfw[:-1], i.roles):
                for r in vrb.role_nsfw[:-1]: 
                    await i.remove_roles(r)

    #usuwanie ról od hugów jak ktoś ma nie lubi czułości
    for i in guild.members:
        if vrb.czulosc in i.roles:
            if chk_list_cohesion(vrb.hugel[:-1], i.roles):
                for r in vrb.hugel[:-1]: 
                    await i.remove_roles(r)
            
    #ogarnianie kolorów
    for i in guild.members:
        try:
            if len(search_in_list(i.roles[::-1], vrb.dividing_colors, vrb.dividing_forfun)) > 3:
                for r in search_in_list(i.roles[::-1], vrb.dividing_colors, vrb.dividing_forfun)[1:-2]:
                    await i.remove_roles(r)
                await i.send('Wybrałeś więcej niż jedną rolę od koloru, zostały Ci one usunięte, możesz je nadać z powrotem na kanale <#596020200080408596>')
        except: pass
