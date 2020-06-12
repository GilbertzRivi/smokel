from client import client
from discord import Role, Embed, File
from functions import chk_list_cohesion, discord_file
import variables as vrb
from os import remove

print('Pomyślnie załadowano role_info.py')

@client.command()
async def rinf(ctx, *, role: Role):
    if not chk_list_cohesion(ctx.author.roles, vrb.management):
        await ctx.send('Nie masz uprawnień')
        return
    e = Embed(color=role.color, timestamp=ctx.message.created_at)
    e.set_author(name=f"informacje o roli {role.name}")
    e.set_footer(text=f"Na prosbe {ctx.author}", icon_url=ctx.author.avatar_url)
    e.add_field(name="Nazwa roli:", value=role.name, inline=False)
    e.add_field(name="Kolor roli:", value=role.color, inline=False)
    e.add_field(name="ID roli:", value=role.id, inline=False)
    e.add_field(name="ilosc uzytkownikow z rola:", value=str(len(role.members)), inline=False)
    await ctx.send(embed=e)

@client.command()
async def rcount(ctx, *, role: Role):
    if not chk_list_cohesion(ctx.author.roles, vrb.management):
        await ctx.send('Nie masz uprawnień')
        return

    mem_list = []
    for member in ctx.guild.members:
        if role in member.roles:
            mem_list.append(member)

    e = Embed(color=role.color, timestamp=ctx.message.created_at)
    e.set_author(name=f"informacje o roli {role.name}")
    e.set_footer(text=f"Na prosbe {ctx.author}", icon_url=ctx.author.avatar_url)
    e.add_field(name="Nazwa roli:", value=role.name, inline=False)
    for y in range(0, len(mem_list), 15):
        role_members = []
        for member in mem_list[y:y + 15]:
            role_members.append(member.name)
        e.add_field(name='Użytkownicy z rolą', value='\n'.join(role_members), inline=False)
    print(len(mem_list))
    await ctx.send(embed=e)
        