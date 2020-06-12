from client import client
from functions import json_add, json_rem

print('Pomyślnie załadowano twitch.py')

@client.command()
async def twitch(ctx, twitch_id, link):
    try:
        int(twitch_id)
    except:
        await ctx.send('Twoje ID jakimś cudem nie jest liczbą, jeżeli masz problem ze znalezieniem ID swojego twitchowego konta, użyj tego rozszerzenia:\n*https://chrome.google.com/webstore/detail/twitch-username-and-user/laonpoebfalkjijglbjbnkfndibbcoon*')
        return
    if 'https://www.twitch.tv/' in link:
        json_add('twitch.json', ['users', str(ctx.author.id)], {"id": int(twitch_id), "channel_link": link, "notyficated": 'no', "message_id": None})
    else:
        await ctx.send('Podaj pełny link do swojego kanału, łącznie z https://www.')
        return
    await ctx.send('Pomyślnie dodałem twój kanał do listy obserwowanych kanów')

@client.command()
async def remove_twitch(ctx):
    try:
        json_rem('twitch.json', ['users', str(ctx.author.id)])
    except:
        await ctx.send('Nie mam zapisanego żadnego kanału twitch pod twoim kontem')