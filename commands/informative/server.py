from client import client
from discord import Embed
from functions import time_to_days
from datetime import datetime

print('Pomyślnie załadowano server.py')

@client.command()
async def sinf(ctx):
    d, h, m, s = time_to_days(datetime.utcnow().timestamp() - ctx.guild.created_at.timestamp())
    
    age = ''
    if d == 0:
        if h == 0:
            if m == 0:
                age = f'{s} sekund'
            else:
                age = f'{m} minut i {s} sekund'
        else:
            age = f'{h} godzin, {m} minut i {s} sekund'
    else:
        age = f'**{d}** dni, **{h}** godzin, **{m}** minut i **{s}** sekund'

    counter = 0
    for member in ctx.guild.members:
        if member.bot:
            counter += 1 
    e = Embed(color=ctx.author.color, name=f"Informacje na temat serwera {ctx.guild.name}", timestamp=ctx.message.created_at)
    e.add_field(name='Nazwa serwera:', value=ctx.guild.name, inline=True)
    e.set_thumbnail(url=ctx.guild.icon_url)
    e.add_field(name="Host serwera:", value=f"{ctx.guild.owner} aka {ctx.guild.owner.display_name}", inline=True)
    e.add_field(name="Ilosc emotek:", value=len(ctx.guild.emojis), inline=True)
    e.add_field(name="Ilosc kanalow tekstowych:", value=len(ctx.guild.text_channels), inline=True)
    e.add_field(name="Ilosc kanalow glosowych:", value=len(ctx.guild.voice_channels), inline=True)
    e.add_field(name="Ilosc kanalow w sumie:", value=len(ctx.guild.voice_channels) + len(ctx.guild.text_channels), inline=True)
    e.add_field(name="Ilosc uzytkownikow:", value=len(ctx.guild.members) - counter, inline=True)
    e.add_field(name="Ilosc botow:", value=counter, inline=True)
    e.add_field(name="Ilosc rol:", value=len(ctx.guild.roles), inline=True)
    e.add_field(name="Stworzony:", value=f'{ctx.guild.created_at.strftime(("%S:%H:%M - %d.%m.%Y"))}\nCzyli:\n{age} temu', inline=False)
    e.set_footer(text=f'Na prośbę {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=e)
