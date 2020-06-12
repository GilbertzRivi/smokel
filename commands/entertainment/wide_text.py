from client import client

print('Pomyślnie załadowano wide_text.py')

@client.command()
async def stxt(ctx, *, args):
    await ctx.message.delete()
    counter = 0
    isp = 0
    output = ''
    for i in args:
        if len(args) <= 8:
            if counter == 1:
                isp += 1
                counter = 0
        elif len(args) > 8 and len(args) <= 16:
            if counter == 2:
                isp += 1
                counter = 0
        elif len(args) > 16:
            if counter == 3:
                isp += 1
                counter = 0
        output += i+isp*" "
        counter += 1
    output = output[0:-isp]
    await ctx.send(f"***{output}***")