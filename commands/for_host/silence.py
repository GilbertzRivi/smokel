from client import client
from functions import read, json_add
from string import ascii_letters
from asyncio import TimeoutError
from random import choice
from json import loads
from discord import PermissionOverwrite
import variables as vrb

print('Pomyślnie załadowano silence.py')

@client.command()
async def silence(ctx, arg):
    if ctx.author != vrb.host or not vrb.kanclerz in ctx.author.roles:
        await ctx.send('Nie masz uprawnień')
        return

    if arg == 'on':
        letters = ascii_letters
        safety_string = ''.join(choice(letters) for i in range(6))
        await ctx.send(f'Wpisz ten ciąg znaków aby potwierdzić decyzję o zablokowaniu wszystkich kanałów serwera\n``{safety_string}``')

        def check(m):
            return m.content == safety_string and m.author == ctx.author and m.channel == ctx.channel

        try:
            await client.wait_for('message', timeout=15.0, check=check)
        except TimeoutError:
            await ctx.channel.send('Czas minął')
            return

        loading = await ctx.send('``Wyciszanie trwa\n'+25*'-'+'``')
        loading_counter = 0
        json_add('commands/for_host/silence.json', ['silenced'], True)
        for channel in ctx.guild.text_channels:
            loading_progress = int(loading_counter/len(ctx.guild.channels)*25)
            for role in channel.changed_roles:
                await channel.set_permissions(role, overwrite=None)
            await channel.set_permissions(ctx.guild.default_role, read_messages=False)
            await loading.edit(content='``Wyciszanie trwa\n'+loading_progress*'#'+(25-loading_progress)*'-'+'``')
            loading_counter += 1
        silenced = await ctx.guild.create_text_channel(name='inf kryzysowa', overwrites={ctx.guild.default_role: PermissionOverwrite(send_messages=False)})
        await silenced.send('Przepraszamy ale wystąpiła sytuacja kryzysowa i serwer będzie niedostępny przez pewien okres czasu.\nAdministracja zajmuje się sytuacją i powinna wam przekazać więcej informacji.')
        await loading.edit(content='``Done\n'+25*'#'+'``')
    
    if arg == 'off':
        all_chans = loads(read('commands/for_host/silence.json'))['saved_perms']
        loading = await ctx.send('``Odciszanie trwa\n'+25*'-'+'``')
        loading_counter = 0
        for chan_id in all_chans:
            channel = client.get_channel(int(chan_id))
            await channel.set_permissions(ctx.guild.default_role, overwrite=None)
            for role_id in all_chans[chan_id]:
                perms = all_chans[chan_id][role_id]
                role = ctx.guild.get_role(int(role_id))
                if len(perms) == 0: continue
                await channel.set_permissions(role, **perms)
            loading_progress = int(loading_counter/len(ctx.guild.channels)*25)
            await loading.edit(content='``Odciszanie trwa\n'+loading_progress*'#'+(25-loading_progress)*'-'+'``')
            loading_counter += 1
        await loading.edit(content='``Done\n'+25*'#'+'``')

        json_add('commands/for_host/silence.json', ['silenced'], False)