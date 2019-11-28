import discord
import asyncio
from PIL import Image, ImageDraw, ImageFont
from discord.ext import commands
import database
from database import *
from random import randint

# cluester = MongoClient("mongodb+srv://thiago:x@cluster0-jhejj.gcp.mongodb.net/test?retryWrites=true&w=majority")
# db = cluester['test']
# collection = db


client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("Ready!")


@client.event
async def on_message(message):
    id = client.get_guild(145551479292428288)
    channels = ["bot"]
    # valid_users = ["THIAGO#6785"]

    update(str(message.author))

    if str(message.channel) in channels:
        if message.content == "!hello":
            await message.channel.send("Hi", file=discord.File('images/fuinha.jpg'))

        elif message.content == "!divulga":
            embed = discord.Embed(title="DIVULGA MEU SITE", url="https://github.com/ThiagoCComelli",
                                  description="Pense em uma boa descricao", color=0x552583)
            embed.set_author(name="Thiago Comelli", url="https://github.com/ThiagoCComelli",
                             icon_url="https://avatars3.githubusercontent.com/u/51216389?s=460&v=4")
            embed.set_thumbnail(url="https://avatars3.githubusercontent.com/u/51216389?s=460&v=4")
            embed.add_field(name="Só trabalho bom", value="é?", inline=False)
            await message.channel.send(embed=embed)

        elif message.content.startswith("!gerador") == True:
            palavras = (message.content).split(" ")
            if len(palavras) == 1:
                await message.channel.send("Falta argumentos. Ex: !gerador 100 30 20 'Hello World!'")
            else:
                palavra = str(palavras[4:])
                img = Image.new('RGB', (int(palavras[1]), int(palavras[2])), color=(255, 255, 255))
                fnt = ImageFont.truetype('misc/times.ttf', int(palavras[3]))
                d = ImageDraw.Draw(img)
                d.text((5, 0), "{}".format(criaFrase(palavras[4:])), font=fnt, fill=(0, 0, 0))
                img.save('images/{}.png'.format(str(message.author)))
                await message.channel.send(file=discord.File("images/{}.png".format(str(message.author))))


def criaFrase(lista):
    frase = ""
    for i in lista:
        frase += i + " "
    frasef = frase.replace('"',"")
    return frasef



client.run('NjQ5MDQzMDM4ODE0ODYzMzYw.Xd3EDg.2aDPqofdtZFcFx9mZkraDp6iMAU')


