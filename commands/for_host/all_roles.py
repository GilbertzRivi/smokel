from client import client
import variables as vrb
from discord import Role

print('Pomyślnie załadowano all_roles.py')

@client.command()
async def give_roles(ctx, *, role: Role):
    if ctx.author != vrb.host:
        await ctx.send('Nie masz uprawnień')
        return
    await ctx.send('-'*100)
    message = ctx.channel.last_message
    counter = 0
    for member in ctx.guild.members:
        await member.add_roles(role, reason='Masowe nadanie roli')
        counter += 1
        percent = int(counter/len(ctx.guild.members)*100)
        await message.edit(content=str(percent*'#'+(100-percent)*'-'))
    await message.edit('Pomyślnie nadano role wszyskim użytkownikom')
