from client import client
from discord import Member, Embed, File
from discord.ext.commands import MissingRequiredArgument
from time import time
from io import BytesIO


print('Pomyślnie załadowano avatar.py')

@client.command()
async def av(ctx, *, member: Member):
    await ctx.message.delete()
    e = Embed(color=ctx.author.colour)
    e.set_footer(text=f"{ctx.author.name} prosi o avka {member.display_name}-a", icon_url=ctx.author.avatar_url)
    e.set_image(url=member.avatar_url)
    await ctx.send(embed=e)

@av.error
async def av_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.message.delete()
        e = Embed(color=ctx.author.colour)
        e.set_footer(text=f"Oto twój awek", icon_url=ctx.author.avatar_url)
        e.set_image(url=ctx.author.avatar_url)
        await ctx.send(embed=e)

@client.command()
async def avas(ctx, format, *, member: Member):
    await ctx.message.delete()
    try: av_binary = await member.avatar_url_as(static_format=format, size=4096).read()
    except:
        await ctx.send('Możesz użyć jednego z podanych formatów, jpg, png, webp, jpeg lub gif')
    av_file = File(BytesIO(av_binary), f'avatar.{format}')
    await ctx.send(file=av_file)

@avas.error
async def avas_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.message.delete()
        try: av_binary = await ctx.author.avatar_url_as(static_format=ctx.message.content.split(' ')[1], size=4096).read()
        except:
            await ctx.send('Możesz użyć jednego z podanych formatów, jpg, png, webp, jpeg lub gif')
        av_file = File(BytesIO(av_binary), f"avatar.{ctx.message.content.split(' ')[1]}")
        await ctx.send(file=av_file)