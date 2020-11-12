# Work with Python 3.6
import discord

TOKEN = 'Nzc2NTY4NjI4ODMzMjg4MjIy.X62x5Q.Zi_sj4fgA-r5oC8hA2SSeJtuJjU'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('huh') or message.content.startswith('HUH') or message.content.startswith('HuH') or message.content.startswith('hUh'):
        await message.channel.send('huh')
    if message.content.startswith('!help'):
        await message.channel.send('```This is a simple bot for the "huh" channel to automaticaly respond whenever someone says, "huh". This bot was completley coded by an AI as a part of a diffrent project.```')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(client.guilds)
    print('------')

client.run(TOKEN)
