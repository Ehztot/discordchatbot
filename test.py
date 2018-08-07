import discord
from discord.ext import commands
import random

description = '''전적을 검색합니다.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('로그인 했어요.')
    print(bot.user.name)
    print(bot.user.id)
    print('------')













bot.run('NDc2MjU5NjcxNjU3Njc2ODEw.Dkrccw.jqdXN-dhzaigXsA6mvykRYE5vB')
