from client import client

print('Pomyślnie załadowano calculator.py')

async def nope(ctx, b):
    return True

@client.command()
async def calc(ctx, a, sign, b):
    try:
        a = int(a)
        b = int(b)
    except:
        await ctx.send(f'Któryś ze znaków nie jest liczbą, sprawdż czy w przypadku liczby z ułamkiem nie dałeś przecinka zamiast kropki')
        return
    if sign == '+': result = a+b
    elif sign == '-': result = a-b
    elif sign == 'x' or sign == '*': result = a*b 
    elif sign == '/':
        if b == 0:
            await ctx.send('=w= **nie**')
            return
        result = a/b
    elif sign == '%':
        if b == 0:
            await ctx.send('=w= **nie**')
            return
        result = a%b 
    elif sign == ':':
        if b == 0:
            await ctx.send('=w= **nie**')
            return
        result = a/b
        rest = a%b
    elif sign == '^': result = a**b
    try: 
        await ctx.send(f'Wynik to {int(result)} r. {rest}')
        return
    except: pass
    try: await ctx.send(f'Wynik to {result}')
    except: await ctx.sednd('Wynik jest dłuższy niż 2000 znaków, ze względu na wygodę użytkowników, nie wyślę go.')
