from client import client
from discord import Emoji, Embed

print('Pomyślnie załadowano emoji.py')

@client.command()
async def em(ctx, args: Emoji):
    await ctx.message.delete()
    e = Embed(color=ctx.author.colour)
    e.set_footer(text=f"{ctx.author.name} prosi o emotke", icon_url=ctx.author.avatar_url)
    e.set_image(url=args.url)
    await ctx.send(embed=e)
