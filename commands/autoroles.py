from client import client
from functions import read, search_in_list
import variables as vrb
from json import loads
from discord import Embed
from time import sleep
from discord.utils import get
from datetime import datetime

print('Pomyślnie załadowano autoroles.py')

@client.command()
async def autorole(ctx, args):
    await ctx.message.delete()
    
    if not vrb.adm_role in ctx.author.roles:
        await ctx.send('Nie masz uprawnień')
        return

    json_file = loads(read('config.json'))
    excluded = json_file['autoroles']['excluded']
    embed = False
    category = False

    chan = ctx.channel

    if args == 'kolory':
        await chan.send('``================``\n  **Role od kolorów**\n``================``')
        upper = vrb.dividing_colors
        lower = vrb.dividing_forfun
        category = True
        embed = True
        
    elif args == '4fun':
        await chan.send('``============``\n  **Role for fun**\n``============``')
        upper = vrb.dividing_forfun
        lower = vrb.dividing_games
        category = True

    elif args == 'gry':
        await chan.send('``==================``\n   **Pokaż w co grasz**\n``==================``')
        upper = vrb.dividing_games
        lower = vrb.dividing_channels
        category = True

    elif args == 'funkcyjne':
        await chan.send('``========================================``\n   **Role funkcyjne, dające dostęp do kanałów\n           lub pozwalające na ich oznaczenie**\n``========================================``')
        upper = vrb.dividing_channels
        lower = get(ctx.guild.roles, name='@everyone')
        category = True

    elif args.split(' ')[0] == 'wykluczone':
        await ctx.send([ctx.guild.get_role(role_id).name for role_id in excluded])
        return

    if not category: return

    embeds = [] 
    desc_counter = 0
    for i in search_in_list(ctx.guild.roles[::-1], upper, lower)[1:-1]:
        if i.id in excluded: continue
        if embed:
            e = Embed(color=i.color, name=i.name, timestamp=datetime.utcnow())
            e.add_field(name=i.name, value=f'*hex* - ``{str(i.color).upper()}``')
            e.set_footer(text=f'-={i.name}=-', icon_url=ctx.guild.icon_url)
        else:
            if args == 'funkcyjne':
                if desc_counter == 0: e = f'Rola pokazująca twoją przynależność do grupy dzidowców\n**{i.name}** - *{i.color}*'
                if desc_counter == 1: e = f'Jeżeli masz tą rolę, nie można na tobie użyć komendy -hug\n**{i.name}** - *{i.color}*'
                if desc_counter == 2: e = f'Jeżeli masz tą rolę, nie można na tobie użyć komendy -kiss\n**{i.name}** - *{i.color}*' 
                if desc_counter == 3: e = f'Jeżeli masz tą rolę, nie można na tobie użyć komendy -boop\n**{i.name}** - *{i.color}*'
                if desc_counter == 4: e = f'Jeżeli masz tą rolę, nie można na tobie użyć komendy -pat\n**{i.name}** - *{i.color}*'
                if desc_counter == 5: e = f'Jeżeli masz tą rolę, nie można na tobie użyć komendy -lick\n**{i.name}** - *{i.color}*'
                if desc_counter == 6: e = f'Jeżeli masz tą rolę, nie można na tobie użyć komendy -nom\n**{i.name}** - *{i.color}*'
                if desc_counter == 7: e = f'Jeżeli masz tą rolę, nie można na tobie użyć żadnej z komend <@614628305047388161>a\n**{i.name}** - *{i.color}*'
                if desc_counter == 8: e = f'Jeżeli masz tą rolę, osoby przeciwnej płci nie mogą na tobie użyć <@614628305047388161>a\n**{i.name}** - *{i.color}*'
                if desc_counter == 9: e = f'Jeżeli masz tą rolę, osoby tej samej płci nie mogą na tobie użyć <@614628305047388161>a\n**{i.name}** - *{i.color}*'
                if desc_counter == 10: e = f'Weź tą rolę jeżeli jesteś rysownikiem, czasem jest pingowana gdy ktoś chce kupić arta\n**{i.name}** - *{i.color}*'
                if desc_counter == 11: e = f'Jeżeli posiadasz Fursuita, ta rola jest dla ciebie :3\n**{i.name}** - *{i.color}*'
                if desc_counter == 12: e = f'Rola ta daje dostęp do kanału **NSFW** <#531261766634831873>\n**{i.name}** - *{i.color}*'
                if desc_counter == 13: e = f'Rola ta daje dostęp do kanału **NSFW** <#531261813749448755>\n**{i.name}** - *{i.color}*'
                if desc_counter == 14: e = f'Rola ta daje dostęp do kanału **NSFW** <#531261855302418433>\n**{i.name}** - *{i.color}*'
                if desc_counter == 15: e = f'Rola ta daje dostęp do kanału **NSFW** <#531268391760297995>\n**{i.name}** - *{i.color}*'
                if desc_counter == 16: e = f'Rola ta daje dostęp do kanału **NSFW** <#531268417811120148>\n**{i.name}** - *{i.color}*'
                if desc_counter == 17: e = f'Rola ta daje dostęp do kanału **NSFW** <#541394633306144781>\n**{i.name}** - *{i.color}*'
                if desc_counter == 18: e = f'Rola ta daje dostęp do kanału **NSFW** <#672514951704870932>\n**{i.name}** - *{i.color}*'
                if desc_counter == 19: e = f'Rola ta daje dostęp do kanału **NSFW** <#541395282336808994>\n**{i.name}** - *{i.color}*'
                if desc_counter == 20: e = f'Rola ta daje dostęp do kanału **NSFW** <#542336916973027341>\n**{i.name}** - *{i.color}*'
                if desc_counter == 21: e = f'Rola ta daje dostęp do kanału **NSFW** <#622056811440242698>\n**{i.name}** - *{i.color}*'
                if desc_counter == 22: e = f'Rola ta daje dostęp do WSZYSTKICH kanałów **NSFW**\n**{i.name}** - *{i.color}*'
                if desc_counter == 23: e = f'Role poniżej odnoszą się do twojej orientacji seksualnej, jeżeli nie chcesz jej specjalnie ujawniać weź "I tak nie zarucham"\n**{i.name}** - *{i.color}*'
                if desc_counter == 24: e = f'**{i.name}** - *{i.color}*'
                if desc_counter == 25: e = f'**{i.name}** - *{i.color}*'
                if desc_counter == 26: e = f'**{i.name}** - *{i.color}*'
                if desc_counter == 27: e = f'**{i.name}** - *{i.color}*'
                desc_counter += 1
            else:
                e = f'**{i.name}** - *{i.color}*'
        embeds.append(e)

    for e in embeds:
        if embed: message = await chan.send(embed=e)
        else: message = await chan.send(e)
        
        await message.add_reaction('☑')
        try: await client.wait_for('reaction_add', timeout=5.0)
        except: await message.add_reaction('☑')

@client.command()
async def atrol(ctx):
    await ctx.message.delete()
    if not vrb.adm_role in ctx.author.roles:
        await ctx.send('Nie masz uprawnień')
        return

    json_file = loads(read('config.json'))
    excluded = json_file['autoroles']['excluded']
    
    def send(upper, lower, embed = False, funkcyjne = False):
        embeds = [] 
        desc_counter = 0
        for i in search_in_list(ctx.guild.roles[::-1], upper, lower)[1:-1]:
            if i.id in excluded: continue
            if embed:
                e = Embed(color=i.color, name=i.name, timestamp=datetime.utcnow())
                e.add_field(name=i.name, value=f'*hex* - ``{str(i.color).upper()}``')
                e.set_footer(text=f'-={i.name}=-', icon_url=ctx.guild.icon_url)
            else:            
                if funkcyjne:
                    if desc_counter == 0: e = f'Rola pokazująca twoją przynależność do grupy dzidowców\n**{i.name}** - *{i.color}*'
                    if desc_counter == 1: e = f'Jeżeli masz tą rolę, nie można na tobie użyć komendy -hug\n**{i.name}** - *{i.color}*'
                    if desc_counter == 2: e = f'Jeżeli masz tą rolę, nie można na tobie użyć komendy -kiss\n**{i.name}** - *{i.color}*' 
                    if desc_counter == 3: e = f'Jeżeli masz tą rolę, nie można na tobie użyć komendy -boop\n**{i.name}** - *{i.color}*'
                    if desc_counter == 4: e = f'Jeżeli masz tą rolę, nie można na tobie użyć komendy -pat\n**{i.name}** - *{i.color}*'
                    if desc_counter == 5: e = f'Jeżeli masz tą rolę, nie można na tobie użyć komendy -lick\n**{i.name}** - *{i.color}*'
                    if desc_counter == 6: e = f'Jeżeli masz tą rolę, nie można na tobie użyć komendy -nom\n**{i.name}** - *{i.color}*'
                    if desc_counter == 7: e = f'Jeżeli masz tą rolę, nie można na tobie użyć żadnej z komend <@614628305047388161>a\n**{i.name}** - *{i.color}*'
                    if desc_counter == 8: e = f'Jeżeli masz tą rolę, osoby przeciwnej płci nie mogą na tobie użyć <@614628305047388161>a\n**{i.name}** - *{i.color}*'
                    if desc_counter == 9: e = f'Jeżeli masz tą rolę, osoby tej samej płci nie mogą na tobie użyć <@614628305047388161>a\n**{i.name}** - *{i.color}*'
                    if desc_counter == 10: e = f'Weź tą rolę jeżeli jesteś rysownikiem, czasem jest pingowana gdy ktoś chce kupić arta\n**{i.name}** - *{i.color}*'
                    if desc_counter == 11: e = f'Jeżeli posiadasz Fursuita, ta rola jest dla ciebie :3\n**{i.name}** - *{i.color}*'
                    if desc_counter == 12: e = f'Rola ta daje dostęp do kanału **NSFW** <#531261766634831873>\n**{i.name}** - *{i.color}*'
                    if desc_counter == 13: e = f'Rola ta daje dostęp do kanału **NSFW** <#531261813749448755>\n**{i.name}** - *{i.color}*'
                    if desc_counter == 14: e = f'Rola ta daje dostęp do kanału **NSFW** <#531261855302418433>\n**{i.name}** - *{i.color}*'
                    if desc_counter == 15: e = f'Rola ta daje dostęp do kanału **NSFW** <#531268391760297995>\n**{i.name}** - *{i.color}*'
                    if desc_counter == 16: e = f'Rola ta daje dostęp do kanału **NSFW** <#531268417811120148>\n**{i.name}** - *{i.color}*'
                    if desc_counter == 17: e = f'Rola ta daje dostęp do kanału **NSFW** <#541394633306144781>\n**{i.name}** - *{i.color}*'
                    if desc_counter == 18: e = f'Rola ta daje dostęp do kanału **NSFW** <#672514951704870932>\n**{i.name}** - *{i.color}*'
                    if desc_counter == 19: e = f'Rola ta daje dostęp do kanału **NSFW** <#541395282336808994>\n**{i.name}** - *{i.color}*'
                    if desc_counter == 20: e = f'Rola ta daje dostęp do kanału **NSFW** <#542336916973027341>\n**{i.name}** - *{i.color}*'
                    if desc_counter == 21: e = f'Rola ta daje dostęp do kanału **NSFW** <#622056811440242698>\n**{i.name}** - *{i.color}*'
                    if desc_counter == 22: e = f'Rola ta daje dostęp do WSZYSTKICH kanałów **NSFW**\n**{i.name}** - *{i.color}*'
                    if desc_counter == 23: e = f'Role poniżej odnoszą się do twojej orientacji seksualnej, jeżeli nie chcesz jej specjalnie ujawniać weź "I tak nie zarucham"\n**{i.name}** - *{i.color}*'
                    if desc_counter == 24: e = f'**{i.name}** - *{i.color}*'
                    if desc_counter == 25: e = f'**{i.name}** - *{i.color}*'
                    if desc_counter == 26: e = f'**{i.name}** - *{i.color}*'
                    if desc_counter == 27: e = f'**{i.name}** - *{i.color}*'
                    desc_counter += 1
                else:
                    e = f'**{i.name}** - *{i.color}*'
            embeds.append(e)
        return embeds

    chan = ctx.channel  
    await chan.send('``==================``\n   **Pokaż w co grasz**\n``==================``')
    upper = vrb.dividing_games
    lower = vrb.dividing_channels
    embed = False

    embeds = send(upper, lower)
    for e in embeds:
        if embed: message = await chan.send(embed=e)
        else: message = await chan.send(e)
            
        await message.add_reaction('☑')
        try: await client.wait_for('reaction_add', timeout=5.0)
        except: await message.add_reaction('☑')
    
    await chan.send('``================``\n  **Role od kolorów**\n``================``')
    upper = vrb.dividing_colors 
    lower = vrb.dividing_forfun
    embed = True
    
    embeds = send(upper, lower, embed)
    for e in embeds:
        if embed: message = await chan.send(embed=e)
        else: message = await chan.send(e)
            
        await message.add_reaction('☑')
        try: await client.wait_for('reaction_add', timeout=5.0)
        except: await message.add_reaction('☑')
    
    await chan.send('``========================================``\n   **Role funkcyjne, dające dostęp do kanałów\n           lub pozwalające na ich oznaczenie**\n``========================================``')
    upper = vrb.dividing_channels
    lower = get(ctx.guild.roles, name='@everyone')
    embed = False
        
    embeds = send(upper, lower, funkcyjne = True)
    for e in embeds:
        if embed: message = await chan.send(embed=e)
        else: message = await chan.send(e)
            
        await message.add_reaction('☑')
        try: await client.wait_for('reaction_add', timeout=5.0)
        except: await message.add_reaction('☑')
    