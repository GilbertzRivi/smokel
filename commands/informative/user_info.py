from discord import Member, Embed
from client import client
from functions import chk_list_cohesion, user_info, time_to_days
import variables as vrb
from time import time
from datetime import datetime

print('Pomyślnie załadowano user_info.py')

@client.command()
async def uinf(ctx, *, member: Member):
    if not chk_list_cohesion(ctx.author.roles, vrb.management):
        await ctx.send('Nie masz uprawnień')
        return
    await ctx.send(embed=user_info(ctx.author, member, False))

@client.command()
async def inf(ctx):
    
    d_os, h_os, m_os, s_os = time_to_days(datetime.utcnow().timestamp() - ctx.author.joined_at.timestamp())
    d_ae, h_ae, m_ae, s_ae = time_to_days(datetime.utcnow().timestamp() - ctx.author.created_at.timestamp())

    on_serv = ''
    if d_os == 0:
        if h_os == 0:
            if m_os == 0:
                on_serv = f'{s_os} sekund'
            else:
                on_serv = f'{m_os} minut i {s_os} sekund'
        else:
            on_serv = f'{h_os} godzin, {m_os} minut i {s_os} sekund'
    else:
        on_serv = f'{d_os} dni, {h_os} godzin, {m_os} minut i {s_os} sekund'

    acc_age = ''
    if d_ae == 0:
        if h_ae == 0:
            if m_ae == 0:
                acc_age = f'{s_ae} sekund'
            else:
                acc_age = f'{m_ae} minut i {s_ae} sekund'
        else:
            acc_age = f'{h_ae} godzin, {m_ae} minut i {s_ae} sekund'
    else:
        acc_age = f'{d_ae} dni, {h_ae} godzin, {m_ae} minut i {s_ae} sekund'

    e = Embed(color=vrb.host.color, timestamp=ctx.message.created_at)
    e.set_author(name=f"informacje na twój temat")
    e.set_thumbnail(url=ctx.author.avatar_url)
    e.add_field(name="Na serwerze jesteś:", value=on_serv, inline=False)
    e.add_field(name="Konto masz:", value=acc_age, inline=False)
    e.set_footer(text=f"Na prośbę {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=e)
