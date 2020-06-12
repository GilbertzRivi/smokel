from client import client
from functions import discord_file
from os import listdir

print('Pomyślnie załadowano reaction_meme.py')

@client.command()
async def rmem(ctx, *, meme):
    await ctx.message.delete()
    memes = listdir('resources/reaction_memes')
    names = []
    for name in memes:
        names.append(name.split('.')[0])
        if meme == name.split('.')[0]: 
            extension = name.split('.')[-1]
    if meme == 'help':
        memes_formated = '\n-'.join(names)
        await ctx.author.send(f'Lista reaction memów dostępnych do wysłania:\n-{memes_formated}')
        return
    try: await ctx.send(f'{ctx.author.name} reaguje:', file=discord_file(f'resources/reaction_memes/{meme}.{extension}', f'{meme}.{extension}', False))
    except: await ctx.send('W mojej bazie nie ma takiego mema')