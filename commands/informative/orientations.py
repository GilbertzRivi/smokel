from client import client
import variables as vrb

print('Pomyślnie załadowano orientations.py')

@client.command()
async def orient(ctx):
    het = 0
    hom = 0
    bi = 0 
    ase = 0
    nzrch = 0
    for member in ctx.guild.members:
        for role in member.roles:
            if role == vrb.het: het += 1
            if role == vrb.hom: hom += 1
            if role == vrb.bi: bi += 1
            if role == vrb.aseks: ase += 1
            if role == vrb.nie_zarucham: nzrch += 1
    cal = het + hom + bi + ase + nzrch
    het = str(het/cal*100)[:6]
    hom = str(hom/cal*100)[:6]
    bi = str(bi/cal*100)[:6]
    ase = str(ase/cal*100)[:6]
    nzrch = str(nzrch/cal*100)[:6]
    await ctx.send(f'Populacja seksualistow na serwerze\nheterycy stanowia jedynie {het} procent naszej ~~zjebanej~~ wspanialej spolecznosci\nhomozegzualizdzi to zniewalajace {hom} procent z was\nwiecznie niezdecydowani baj segz ualisci to rowno {bi} procent\nnatomiast procent osob nie lubiacych zadnych ludzi lub nieludzi to {ase}\nWieczne przegrywy to zaledwie {nzrch}%')
