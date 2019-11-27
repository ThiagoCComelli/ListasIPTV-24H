import discord
import asyncio

client = discord.Client()
# id = 145551479292428288

@client.event
async def on_message(message):
    id = client.get_guild(145551479292428288)
    channels = ["bot"]
    valid_users = ["THIAGO#6785"]

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content == "!hello":
            await message.channel.send("Hi")

        if message.content == "!help":
            embed = discord.Embed(title="DIVULGA MEU SITE", url="https://github.com/ThiagoCComelli",description="Pense em uma boa descricao", color=0x552583)
            embed.set_author(name="Thiago Comelli", url="https://github.com/ThiagoCComelli",icon_url="https://avatars3.githubusercontent.com/u/51216389?s=460&v=4")
            embed.set_thumbnail(url="https://avatars3.githubusercontent.com/u/51216389?s=460&v=4")
            embed.add_field(name="Só trabalho bom", value="é?", inline=False)
            await message.channel.send(embed=embed)
    else:
        print("{} tried to do command {}, in channel {}".format(message.author,message.content,message.channel))

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "defeituosa":
            await client.send_message("Bem Vindo {}".format(member.mention))







client.run('NjQ5MDQzMDM4ODE0ODYzMzYw.Xd3EDg.2aDPqofdtZFcFx9mZkraDp6iMAU')
