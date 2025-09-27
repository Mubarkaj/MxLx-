import random as r
import json

def scale(iterable, datatype):
    if datatype == 'a':
        return [i for  n, i in enumerate(iterable, start = 1) if n % 2 == 0]
    elif datatype == 'q':
        return [i for  n, i in enumerate(iterable, start = 1) if not n % 2 == 0]
    else:
        raise NameError(
            "FIST PARAMETER (datatype) is must be 'a' or 'q'."
            "'a' for ANSWERS  | 'b' for QUESTIONS. "
            f"Got \"{datatype}\""
            )


with open("data.json") as f:
    it = json.load(f)

ansa = scale(it, 'a')
aska = scale(it, 'q')

print(ansa[0:5])
print(aska[0:5])














import discord
from discord.ext import commands


description = """An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here."""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    # Tell the type checker that User is filled up at this point
    assert bot.user is not None

    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
def main():
    for a, q in zip(ansa, aska):

        async def q(ctx):
            await ctx.send(a)




bot.run("MTQxMDI0NDI4NDAyNzc2ODkxMg.G6J6jH.hGK0edQqLKwL8SPbHobGfbhw72bHwOyf6zRIcA")
