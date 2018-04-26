import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')

@client.event
async def on_message(message):
  if message.content.startswith('/help'):
      await client.send_message(message.channel, '안녕하세요 테스트 중입니다. 지금 가능한 명령어 목록입니다.  /help \n/hi \n/echo \n등등?  ')

  if message.content.startswith('/hi'):
      await client.send_message(message.channel, '안녕하세요! 새로운 기능을 원하시면 \n소원수리 혹은 Ezhtot에게 보내주세요! ')

  if message.content.startswith('/sex'):
      await client.send_message(message.channel, '너도 유꾸니?')

  if message.content.startswith('하실?'):
      await client.send_message(message.channel, '나도! 나도! ')
  elif message.content.startswith('/echo'):
      await client.send_message(message.channel, '말해봐!')
      msg = await client.wait_for_message(timeout=15.0, author=message.author)

      if msg is None:
          await client.send_message(message.channel, '메아리는 15초 동안 들립니다.')
          return
      else:
          await client.send_message(message.channel, msg.content)

client.run('NDM4NjczNDkzNDk2OTU0ODkw.DcIS0g.XQUj1w7FjLE28VeA9XrT2Sq8voA')
