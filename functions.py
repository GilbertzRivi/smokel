from json import loads, dumps
from io import BytesIO, StringIO
from os import path
from discord import File, Embed, Member
from time import time
from client import client
import variables as vrb
from datetime import datetime
 
print('Pomyślnie załadowano functions.py')

def read(file_path):
    file_path = path.join(f'{path.dirname(path.abspath(__file__))}', file_path)
    with open(file_path) as f:
        return f.read()

def read_b(file_path):
    file_path = path.join(f'{path.dirname(path.abspath(__file__))}', file_path)
    with open(file_path, 'rb') as f:
        return f.read()

def write(file_path, data):
    file_path = path.join(f'{path.dirname(path.abspath(__file__))}', file_path)
    with open(file_path, 'w') as f:
        f.write(data)

def search_in_list(list, first, last):
    return list[(list.index(first)):(list.index(last)+1)]

def chk_list_cohesion(list1, list2):
    temp = False
    for i in list1:
        if i in list2: temp = True
    return temp

def same_pos_in_lists(list1, list2):
    temp = []
    for i in list1:
        if i in list2: temp.append(i)
    return temp

def json_add(path, place, data, update = False):
    json_file = loads(read(path))
    json_copy = json_file
    for i in place[:-1]:
        if i not in json_copy:
            json_copy[i] = dict()
        json_copy = json_copy[i]
    if update: json_copy[place[-1]].update(data)
    else: json_copy[place[-1]] = data
    write(path ,dumps(json_file, indent=4, sort_keys=True))

def json_rem(path, place):
    json_file = loads(read(path))
    json_copy = json_file
    for i in place[:-1]:
        if i not in json_copy:
            json_copy[i] = dict()
        json_copy = json_copy[i]
    del json_copy[place[-1]]
    write(path ,dumps(json_file, indent=4, sort_keys=True))

def discord_file(path, name, spoiler):
    return File(BytesIO(read_b(path)), filename=name, spoiler=spoiler)

def user_info(author, member: Member, new):
    if new:
        e = Embed(color=vrb.host.color)
        e.set_footer(text=f"Na potrzeby serwera", icon_url=author.avatar_url)
    else:
        e = Embed(color=member.color)
        e.set_footer(text=f"Na prośbę {author}", icon_url=author.avatar_url)

    d_os, h_os, m_os, s_os = time_to_days(datetime.utcnow().timestamp() - member.joined_at.timestamp())
    d_ae, h_ae, m_ae, s_ae = time_to_days(datetime.utcnow().timestamp() - member.created_at.timestamp())

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

    e.set_author(name=f"informacje na temat użytkownika {member.name}")
    e.set_thumbnail(url=member.avatar_url)
    e.add_field(name="ID:", value=member.id, inline=False)
    e.add_field(name="Nick:", value=member.name, inline=False)
    e.add_field(name="Nick na serwerze:", value=member.display_name, inline=False)
    e.add_field(name="Dołączyl do discorda:", value=member.created_at.strftime("%H:%M - %d.%m.%Y"), inline=False)
    e.add_field(name="Dołączyl na serwer:", value=member.joined_at.strftime("%H:%M - %d.%m.%Y"), inline=False)
    e.add_field(name="Na serwerze jest:", value=on_serv, inline=False)
    e.add_field(name="Konto ma:", value=acc_age, inline=False)
    return e

def introducion(member):
    if vrb.fem in member.roles:
        intro = f'Witaj w przedsionku serwera {member.mention}!\nAby dostać pełen dostęp do serwera musisz wybrać sobie role na kanale <#{vrb.autoroles_chan1.id}>.\nMusisz wybrać rolę dotyczącą twojej orientacji (jeżeli nie chcesz podawać wybierz <@&{vrb.nie_zarucham.id}>) reszta jest opcjonalna.\nJeżeli chciała byś jakieś dodatkowe role, możesz je sobie nadać na <#{vrb.autoroles_chan2.id}>. Kiedy wybierzesz co chcesz, oznacz kogoś z moderacji/administracji, jeżeli masz jakieś pytania również pisz do nich.'
    else: 
        intro = f'Witaj w przedsionku serwera {member.mention}!\nAby dostać pełen dostęp do serwera musisz wybrać sobie role na kanale <#{vrb.autoroles_chan1.id}>.\nMusisz wybrać rolę dotyczącą twojej orientacji (jeżeli nie chcesz podawać wybierz <@&{vrb.nie_zarucham.id}>) reszta jest opcjonalna.\nJeżeli chciał byś jakieś dodatkowe role, możesz je sobie nadać na <#{vrb.autoroles_chan2.id}>. Kiedy wybierzesz co chcesz, oznacz kogoś z moderacji/administracji, jeżeli masz jakieś pytania również pisz do nich.'
    return intro

def time_to_days(time):

    days = int(time / 86400)
    rest = time % 86400
    hours = int(rest / 3600)
    rest = rest % 3600
    minutes = int(rest / 60)
    seckonds = int(rest % 60)

    return days, hours, minutes, seckonds