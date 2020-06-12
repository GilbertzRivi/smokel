from client import client
import bot_events.message_delete as delete
from discord import Embed
from discord.utils import get

@client.command()
async def snipe(ctx):
    snipe = delete.snipe
    e = Embed(color=ctx.author.color, timestamp=ctx.message.created_at)
    e.set_author(name='Sniped!')
    e.add_field(name=snipe['author'], value=snipe['content'])
    e.set_footer(text=f'Na prośbę {ctx.author.name}', icon_url=ctx.author.avatar_url)
    try:
        e.set_thumbnail(url=get(ctx.guild.members, id=snipe['id']).avatar_url)
    except:
        pass
    await ctx.send(embed=e)
    await ctx.message.delete()