from client import client
from random import choice as random_choice

print('Pomyślnie załadowano ask_choice_etc.py')
odp_ask = ['Bez dwóch zdań','W rzeczy samej','Jeszcze jak','Bynajmniej nie inaczej','Dokładnie tak, nic dodać nic ująć','Ale gdzie tam','Co? Nie, skąd w ogóle ten pomysł?','Jeszcze czego','Uchowaj Boże','Niech ręka boska chroni']

@client.command()
async def choice(ctx, *, args):
    if '@everyone' in args or '@here' in args:
        await ctx.send('Nie')
        return
    await ctx.send(f'Wybieram to: {random_choice(args.split(","))}')

@client.command()
async def ask(ctx):
    await ctx.send(random_choice(odp_ask))