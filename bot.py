# Work with Python 3.6
import discord

TOKEN = str('pppNzc2NTY4NpppjI4ODMpppzMjg4pppMjIy.X62pppx5Q.pppRYO3nAOdDqXl0ppplHonwYZ2RUz_M4ppp'.replace('ppp',''))

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('uh') or message.content.startswith('uH') or message.content.startswith('hu') or message.content.startswith('Hu') or message.content.startswith('hU') or message.content.startswith('Uh') or message.content.startswith('huh') or message.content.startswith('HUH') or message.content.startswith('HuH') or message.content.startswith('hUh') or message.content.startswith('Huh') or message.content.startswith('huH'):
        await message.channel.send('huh')
    if message.content.startswith('!help'):
        await message.channel.send('```This is a simple bot for the "huh" channel to automaticaly respond whenever someone says, "huh". This bot was completley coded by an AI as a part of a diffrent project.```')
        await message.channel.send('```say "huh" to see what it does!```')
@client.event
async def on_ready():
    activity = discord.Game(name='!help or "huh"')
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(client.guilds)
    print('------')

client.run(TOKEN)
