from client import client
from functions import read, json_rem, discord_file, user_info
from json import loads
from time import time, sleep
import variables as vrb

print('Pomyślnie załadowano member_join.py')
member_join_time = None

@client.event
async def on_member_join(member):
    global member_join_time
    member_join_time = time()
    json_file = loads(read('config.json'))
    black_lista = [json_file['black_list'][key] for key in json_file['black_list']]
    if member.id in black_lista:
        await member.ban()
        json_rem('config.json', ['black_list', str(member.id)])
        return
    image = discord_file('resources/join.gif', 'Witamy.gif', False)
    await vrb.ver_chan.send(f"Witamy serdecznie {member.display_name} na serwerze FurHeaven. Celem tego miejsca jest zrzeszanie osob interesujacych sie tematyka furry. Jest tu sporo osob z ktorymi mozna pogadac na przerozne tematy. Mamy nadzieje, ze bedzie Ci tu z nami milo :grin:\nOdpowiedz tylko na  pięć pytań.\n1. Ile masz lat?\n2. Czy jestes futrzakiem?\n3. Czy przeczytales regulamin i bedziesz go przestrzegac?\n4. Mężczyzna/Kobieta?\n5. Skąd masz zaproszenie?\n\nJeżeli odpowiedziałeś/aś na pytania a nikt z moderacji ani administracji jeszcze nic nie zrobił, oznacz kogoś z nich, na pewno od razu przeprowadzą weryfikację :3", file=image)
    image = discord_file('resources/join.mp4', 'Witamy.mp4', False)
    await vrb.main_chan.send(f"<@{member.id}> wlasnie wbil/a na serwer! Zaraz powinien/na do nas dolaczyc.", file=image)
    for role in vrb.dividing_roles:await member.add_roles(role)
    await vrb.commands_chan.send(embed=user_info(vrb.host, member, True))
    sleep(5)
    await vrb.ver_chan.send(f'<@{member.id}>')
    msg = await vrb.ver_chan.send(vrb.host.mention)
    await msg.delete()