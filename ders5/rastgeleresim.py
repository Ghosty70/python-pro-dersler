import discord
import random
from discord import File
import os
import discord.ext.commands as commands
import requests

# Discord bot token
TOKEN = 'apı anahtarı buraya'

# Bot istemcisini başlat
# Bot tanımı
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command(name='duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda ördek fotoğrafı yollar.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run(TOKEN)









