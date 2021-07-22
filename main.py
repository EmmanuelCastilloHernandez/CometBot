''' 
Comet's code
This program was made by Emmanuel Castillo
Student at NHHS in NH, CA, USA

Developers:
Emmanuel Castillo
GitHub: EmmanuelCastilloHernandez
Discord: eta_c4rinae#7810
Email: emmanuelino2@gmail.com

Garen Gevoryan
Discord: Warlex#7860
'''

import os
try:
  os.system('pip3 uninstall -y googletrans')
  os.system('pip3 install googletrans==3.1.0a0')
except:
  os.system('pip3 install googletrans==3.1.0a0')

os.system('pip install git+https://github.com/CodeWithSwastik/prsaw.git')
chatbotAPIKey = os.getenv('chatbotKey')

os.system('pip install discord_components')
# Importing libraries used in the bot
import asyncio
from bs4 import BeautifulSoup
from datetime import datetime
import discord
from discord.ext import commands
from discord.utils import get
from discord.utils import find
from discord import FFmpegPCMAudio
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
from dontDie import dontDieOnMe
from googletrans import Translator
from gtts import gTTS
import lxml
from lxml import etree
import math
import numpy as np
from numpy import *
from PIL import Image, ImageFont, ImageDraw, ImageOps
from io import BytesIO
import random
from random import randint
import randfacts
import string
import sympy as sp
import ffmpeg
import urllib
import urllib.request
import requests, json
import youtube_dl
from zalgo_text import zalgo
import re
from googleapiclient.discovery import build
import audioread
from urllib.parse import parse_qs, urlparse
import requests
from requests import get
import wikipedia
from youtube_dl import YoutubeDL
#from prsaw import RandomStuff

# Thanks to CodeWithSwastik for his python tutorials
# his work is the reason why the bot has a decent warn system
# and a economy system that works. Also thanks to his work this bot has an AI 
# chatbot. You are a GOD!

#chatBot = RandomStuff(api_key = chatbotAPIKey, async_mode = True)

# Snipe variables
regularSnipeAuthor = {}
regularSnipeImage = {}
regularSnipeMessage = {}
snipeMessage = {}
snipeMessageAuthor = {}
snipeMessage2 = {}
snipeMessageAuthor2 = {}
snipeMessage3 = {}
snipeMessageAuthor3 = {}
snipeCounter = 1

usersToLevelUp = {}
useSpammyCharacters = {}
intuitiveBlacklist = {}
levelUpCheck = {}
users = None
reactionMessage = None
title = None
views = 0
likes = 0
length = 0
queuedMusic = None

def startupMsg():
  '''
  ░█████╗░░█████╗░███╗░░░███╗███████╗████████╗
  ██╔══██╗██╔══██╗████╗░████║██╔════╝╚══██╔══╝
  ██║░░╚═╝██║░░██║██╔████╔██║█████╗░░░░░██║░░░
  ██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░░░░██║░░░
  ╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗░░░██║░░░
  ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░
  
  Version **2** Aldebaran ready to use!
  '''

  pass

# Comet audio player dictionary
players = {}
queues = {}
queueTitles = {}

def howLong(length):
  hours = length // 3600
  length %= 3600
  mins = length // 60
  length %= 60
  seconds = length
  
  return hours, mins, seconds

def search(query):
  with YoutubeDL({'format': 'bestaudio', 'noplaylist':'True'}) as ydl:
    try: requests.get(query)
    except: info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
    else: info = ydl.extract_info(query, download=False)
  
  duration = info['duration']

  hours = duration // 3600
  duration %= 3600
  mins = duration // 60
  duration %= 60
  seconds = duration
  return (info, info['formats'][0]['url'], hours, mins, seconds)

#prefix for the bot
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
client = commands.Bot(command_prefix=["#",'comet do ','COMET ', 'comet ', 'Comet '], intents=intents)
client.remove_command('help')

@client.event
async def on_guild_join(guild):
  with open('serverCount.json','r+') as f:
    serverCount = json.load(f)

  serverCount["server count"] = len(client.guilds)
  servers = serverCount["server count"]

  with open('serverCount.json','w') as f:
    serverCount = json.dump(serverCount, f)
  
  general = find(lambda x: x.name == 'general',  guild.text_channels)
  if general and general.permissions_for(guild.me).send_messages:
    embed=discord.Embed(title="My name is Comet. Pleasure to be here!", url="https://cometbot.emmanuelch.repl.co/", description="My alias is # and to find what commands I have, run #help and you should be ready to go. To see if the bot is online, go to the website embedded in this message or if that doesn't work go to: https://cometbot.emmanuelch.repl.co/\nOne final thing: **`run #setup warning`** to configure the bot's warning system.\nThank you for choosing Comet 2.0.0.", color=0x34363b)
    embed.set_author(name=f"Hello, {guild.name}")
    embed.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/favicon.png")
    embed.add_field(name="Sincerely,", value="Emmanuel Castillo", inline=True)
    embed.add_field(name="This bot now runs on:", value=f"{servers} servers", inline=False)
    embed.set_footer(text="Comet Welcome Message")
    await general.send(embed=embed)

@client.event
async def on_guild_remove(guild):
  with open('serverCount.json','r+') as f:
    serverCount = json.load(f)
  
  serverCount["server count"] = len(client.guilds)

  with open('serverCount.json','w') as f:
    serverCount = json.dump(serverCount, f)

@client.event
async def on_member_join(member):
  '''
  This code is put in place at the request of one of the patron
  servers after a member who solicited two girls for inappropriate
  pictures left before he could get banned. This code should
  only affect the server that requested it
  '''

  if member.id == 713566308695932950:
    if member.guild_id == 736621294350499931:
      channel = client.get_channel(777364217673678858)
      embed=discord.Embed(title=f"{member.name} TRIED TO COME BACK", color=0xc53302)
      embed.set_author(name="UNWANTED USER DETECTED")
      embed.add_field(name=f"Hi {member.name},", value="If you're seeing this, it's because the bot caught you trying to slip back into a server you were barred from entering. You are banned from entering again because you asked two underaged girls to show you their boobs as part of a $5 bet by dav#0560. You don't go and ask for boob pics from girls you 13-year old pervert. Get a life and learn some basic manners because you are going to be in some serious problems in the future, you sellout.", inline=True)
      embed.set_footer(text="Unapologetically, the Developer")

      await member.send(embed=embed)
      await member.ban()
      await channel.send(embed=embed)

regEditMessageAuthor = {}
regBeforeMessage = {}
regAfterMessage = {}
@client.event
async def on_message_edit(before, after):
  global regEditMessageAuthor
  global regBeforeMessage
  global regAfterMessage

  if before.content != after.content:
    regEditMessageAuthor[before.channel.id] = before.author
    regBeforeMessage[before.channel.id] = before.content
    regAfterMessage[after.channel.id] = after.content
    
    await asyncio.sleep(80)
    
    del regEditMessageAuthor[before.channel.id]
    del regBeforeMessage[before.channel.id]
    del regAfterMessage[after.channel.id]

# This executes when a message is sent
@client.event
async def on_message(message):
  await client.process_commands(message)

  '''if message.content.startswith(';'):
    msg = message.content.replace(';','')
    responseToSend = await chatBot.get_ai_response(msg)
  
    await message.reply(responseToSend[0]["message"])'''

  allowMessage = True
  # Neo Blacklist Code
  checkBannedWords = ""
  with open("slurs.json", "r") as slurs: slurPrepare = json.load(slurs)

  if str(message.guild.id) in slurPrepare: uselessVariable = 1
  else: slurPrepare[str(message.guild.id)] = []
  
  checkBannedWords = slurPrepare[str(message.guild.id)]
    
  with open('slurs.json','w') as f: json.dump(slurPrepare, f)

  content = str(message.content)
  httpsResult = content.startswith('https')
  emojiResult = content.startswith('<a:')
  content = content.lower()
  if emojiResult == True or httpsResult == True: pass
  else: content = content.translate(str.maketrans('', '', string.punctuation))

  if message.guild.id in intuitiveBlacklist:
    if message.author.id in intuitiveBlacklist[message.guild.id]:
      if 'message' in intuitiveBlacklist[message.guild.id][message.author.id]:
        intuitiveBlacklist[message.guild.id][message.author.id]['message'].append(content)
      else:
        intuitiveBlacklist[message.guild.id][message.author.id]['message'] = []
        intuitiveBlacklist[message.guild.id][message.author.id]['message'].append(content)
    else:
      intuitiveBlacklist[message.guild.id][message.author.id] = {}
      intuitiveBlacklist[message.guild.id][message.author.id]['message'] = []
      intuitiveBlacklist[message.guild.id][message.author.id]['message'].append(content)
  else:
    intuitiveBlacklist[message.guild.id] = {}
    intuitiveBlacklist[message.guild.id][message.author.id] = {}
    intuitiveBlacklist[message.guild.id][message.author.id]['message'] = []
    intuitiveBlacklist[message.guild.id][message.author.id]['message'].append(content)
  
  content = content.split()
  for x in content:
    if (message.author.bot): return
    elif x in checkBannedWords:
      await message.delete()
      return
  
  for x in checkBannedWords:
    def check(m): return m.author == message.author
    
    checkThePhrase = ''.join(intuitiveBlacklist[message.guild.id][message.author.id]['message'])
    if (message.author.bot): return
    elif x in checkThePhrase:
      amountToDelete = int(len(x))
      await message.channel.purge(limit=amountToDelete, check=check)
      intuitiveBlacklist[message.guild.id][message.author.id]['message'] = []
      await message.channel.send('***Message deleted due to a blacklisted word/phrase being detected***', delete_after=10)

  # End of Neo Blacklist code
  
  if message.content.startswith('^'):
    if f'{message.author.id} | {message.guild.id}' in useSpammyCharacters:
      allowMessage = False

    if allowMessage == False:
      pass
    else:
      await message.channel.send('^')
      useSpammyCharacters[f'{message.author.id} | {message.guild.id}'] = message.guild.id

      await asyncio.sleep(30)
      del useSpammyCharacters[f'{message.author.id} | {message.guild.id}']

  # Level Code
  allowPoints = True
  if message.author == client.user:
    return
  
  if f'{message.author.id} | {message.guild.id}' in usersToLevelUp:
    allowPoints = False
  
  await openLevelUser(message.author, message.guild)
  with open('levels.json','r') as f:
    users = json.load(f)

  levelThreshold = 15*users[str(message.guild.id)][str(message.author.id)]['Level']
  if allowPoints == True:
    await updateLevels(message.author, message.guild, random.randint(1, 4), 'XP')

    usersToLevelUp[f'{message.author.id} | {message.guild.id}'] = message.guild.id

    await asyncio.sleep(60)
    del usersToLevelUp[f'{message.author.id} | {message.guild.id}']

  global levelUpCheck
  if users[str(message.guild.id)][str(message.author.id)]['XP'] > levelThreshold:
    if f'{message.author.id} | {message.guild.id}' in levelUpCheck:
      pass
    else:
      newLevel = users[str(message.guild.id)][str(message.author.id)]['Level'] + 1
      await levelUpUser(message.author, message.guild)
      await message.channel.send(f'{message.author.mention} has leveled up to level **`{newLevel}`**. Keep it up!')
      levelUpCheck[f'{message.author.id} | {message.guild.id}'] = True

      await asyncio.sleep(60)
      del levelUpCheck[f'{message.author.id} | {message.guild.id}']

  # End of Level Code

  if message.content.startswith('no one cares'):
    agreedReplies=['agreed\nand I\'m a bot :skull:',
      'agreed',
      '^',
      'ok',
      f'based {message.author.mention}']
    await message.channel.send(f'{random.choice(agreedReplies)}')

  if message.content.startswith('Wow. There is no message to snipe buddy.'):
    await message.channel.send('ok')

async def levelUpUser(user, server):
  global levelUpCheck
  with open('levels.json','r') as f: users = json.load(f)

  if f'{user.id} | {server.id}' not in levelUpCheck:
    levelThreshold = 15*users[str(server.id)][str(user.id)]['Level']

    users[str(server.id)][str(user.id)]['XP'] -= levelThreshold
    users[str(server.id)][str(user.id)]['Level'] += 1

    with open('levels.json','w') as f: json.dump(users, f)
  
  return True

async def openLevelUser(user, server):
  with open('levels.json','r') as f: users = json.load(f)
  
  if str(server.id) in users:
    if str(user.id) in users[str(server.id)]: 
      return False
    else:
      users[str(server.id)][str(user.id)] = {}
      users[str(server.id)][str(user.id)]['Level'] = 1
      users[str(server.id)][str(user.id)]['XP'] = 0
  else:
    users[str(server.id)] = {}
    users[str(server.id)][str(user.id)] = {}
    users[str(server.id)][str(user.id)]['Level'] = 1
    users[str(server.id)][str(user.id)]['XP'] = 0
  
  with open('levels.json','w') as f: json.dump(users, f)
  return True

async def updateLevels(user, server=None, change=0, mode='Level'):
  with open('levels.json','r') as f: users = json.load(f)
  
  users[str(server.id)][str(user.id)][mode] += change

  with open('levels.json','w') as f: json.dump(users, f)
  
  bal = [users[str(server.id)][str(user.id)]["Level"], users[str(server.id)][str(user.id)]["XP"]]
  return bal

snipeCounter = {}
#client event that gets the snipe function's variables ready
@client.event
async def on_message_delete(message):
  global regularSnipeAuthor
  global regularSnipeImage
  global regularSnipeMessage
  global snipeMessage
  global snipeMessageAuthor
  global snipeMessage2
  global snipeMessageAuthor2
  global snipeMessage3
  global snipeMessageAuthor3
  global snipeCounter

  if message.guild.id not in snipeCounter:
    snipeCounter[message.guild.id] = 1
  
  regularSnipeAuthor[message.channel.id] = message.author
  regularSnipeMessage[message.channel.id] = message.content
  try:
    regularSnipeImage[message.channel.id] = await message.attachments[-1].to_file()
  except:
    pass
  
  if snipeCounter[message.guild.id] == 1:
    snipeMessage[message.channel.id] = message.content
    snipeMessageAuthor[message.channel.id] = message.author
    print(snipeMessage[message.channel.id])
    snipeCounter[message.guild.id] += 1
  elif snipeCounter[message.guild.id] == 2:
    snipeMessage2[message.channel.id] = message.content
    snipeMessageAuthor2[message.channel.id] = message.author
    snipeCounter[message.guild.id] += 1
    print(snipeMessage2[message.channel.id])
  elif snipeCounter[message.guild.id] == 3:
    snipeMessage3[message.channel.id] = message.content
    snipeMessageAuthor3[message.channel.id] = message.author
    print(snipeMessage3[message.channel.id])

    snipeCounter[message.guild.id] = 1
    print(f'New snipe val for {message.guild}: '+ str(snipeCounter[message.guild.id]))

  await asyncio.sleep(120)

  snipeCounter[message.guild.id] = 1
  del regularSnipeAuthor[message.channel.id]
  
  try:
    del regularSnipeImage[message.channel.id]
  except:
    pass

  del regularSnipeMessage[message.channel.id]
  del snipeMessageAuthor[message.channel.id]
  del snipeMessage[message.channel.id]
  del snipeMessageAuthor2[message.channel.id]
  del snipeMessage2[message.channel.id]
  del snipeMessageAuthor3[message.channel.id]
  del snipeMessage3[message.channel.id]

@client.event
async def on_ready():
  DiscordComponents(client)
  channel = client.get_channel(839960483398549514)
  with open('serverCount.json','r+') as f:
    serverCount = json.load(f)

  serverCount["server count"] = len(client.guilds)
  servers = serverCount["server count"]

  with open('serverCount.json','w') as f:
    serverCount = json.dump(serverCount, f)
  await client.change_presence(activity = discord.Streaming(name = f'☄️ {servers} Stars in the Sky ☄️', url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
  print(startupMsg.__doc__)
  await channel.send(startupMsg.__doc__, components = [
    [
      Button(style = ButtonStyle.blue, label = f"Servers with Comet: {servers}", disabled = True),
      Button(style = ButtonStyle.green, label = "Creator: Emmanuel Castillo", disabled = True)
    ]
  ])

@client.command(aliases = ['rev'])
async def reverse(ctx, *, msg): await ctx.reply(msg[::-1])

@client.command(pass_context=True)
async def rank(ctx, member: discord.Member=None, show=5):
  serverName = ctx.guild
  rankList = []
  if member == None: member = ctx.author
  with open('levels.json','r') as f: users = json.load(f)
  await openLevelUser(member, serverName)

  for user in ctx.guild.members:
    try:
      userBal = users[str(ctx.guild.id)][str(user.id)]['Level']
      levelBal = users[str(ctx.guild.id)][str(user.id)]['XP']
      valueToAppend = [user.name, userBal, levelBal]
      rankList.append(valueToAppend)
    except:
      x = 1
  print(rankList)
  rankList.sort(reverse=True, key=lambda rank: rank[2])
  rankList.sort(reverse=True, key=lambda rank: rank[1])
  if show > len(rankList):
    show = int(len(rankList))

  levelBal = users[str(ctx.guild.id)][str(member.id)]['XP'] 
  userBal = users[str(ctx.guild.id)][str(member.id)]['Level'] 
  print(rankList)
  counter = 1
  loopCount = 0
  userRank = 0
  rankDisplay = '```'
  for entry in rankList:
    if entry[0] == member.name:
      userRank = counter
    if loopCount < show:
      rankDisplay += f'{counter}. {entry[0]}:\nLevel: {entry[1]}, XP: {entry[2]}\n'
      counter += 1
      loopCount += 1

  rankDisplay += '```'
  levelThreshold = 10*1.5*userBal

  embed=discord.Embed(description=f"========= ***Rank {userRank}*** ==============", color=0x2f3136)
  embed.set_author(name="▞ Comet Rank System ▚")
  embed.set_thumbnail(url=member.avatar_url)
  embed.add_field(name="Level:", value=f"*__{userBal}__*", inline=True)
  embed.add_field(name="XP:", value=f"*__{levelBal}__*", inline=True)
  embed.add_field(name="XP Needed to Level Up:", value=f"*__{levelThreshold - levelBal}__*", inline=True)
  embed.add_field(name="Rank List:", value=rankDisplay, inline=False)
  embed.set_footer(text=f"▧ Rank for {member} ▧")
  await ctx.reply(embed=embed, mention_author=False)

@client.command(pass_context=True)
async def levels(ctx, number=5):
  serverName = ctx.guild.name
  with open('levels.json','r') as f:
    users = json.load(f)
  await openLevelUser(ctx.author, serverName)
  levelList = []

  levelChecker = f'{serverName} Level'

  for user in ctx.guild.members:
    print('hello')
  
  levelList = sorted(levelList, reverse=True)

  embed=discord.Embed(title=f"‣‣‣‣‣‣‣‣‣‣‣ Now Showing Top {number} Users in {serverName} ‣‣‣‣‣‣‣‣‣‣‣‣", color=0x34363b)
  index = 1
  for amt in level:
    id_ = level[amt]
    member = client.get_user(id_)
    name = member.name
    embed.add_field(name = f'{index}. {name}', value=f'{amt}', inline=False)
    if index == number:
      break
    else:
      index += 1

  embed.set_author(name="The ※ U S E R  L I S T ※")
  embed.set_thumbnail(url="https://images.vexels.com/media/users/3/135932/isolated/preview/5873339dddecea4a26d7366462d0eec6-checklist-file-icon-by-vexels.png")
  embed.set_footer(text="Comet Economy Alert")
  await ctx.send(embed=embed)

@client.command(aliases=['Solve'])
async def solve(ctx, v1: int=0, v2: int=0, v3: int=0, v4: int=0, v5: int=0, v6: int=0, v7: int=0):

  x = sp.Symbol('x')
  y = v1+v2*x+v3*x**2+v4*x**3+v5*x**4+v6*x**5+v7*x**6
  solve = f'{v1} + {v2}X + {v3}X^2 + {v4}X^3 + {v5}X^4 + {v6}X^5 + {v7}x^6'
  x = sp.solve(y)
  try:
    embed=discord.Embed(title=f"***Here are the solutions for __{solve}__***", description='***NOTE: Ignore the brackets. Those are because of the text color formatting***', color=0x2f3136)

    counter = 1
    for entry in x:
      entry = str(entry)
      if '**' in entry:
        entry = entry.replace('**', '^')
      if 'I' in entry:
        entry = entry.replace('I', 'i')
      thingToShow = f"```ini\n[ {entry} ]\n```"
      print
      embed.add_field(name = f'Solution #{counter}:', value=thingToShow, inline=False)
      counter += 1
  except:
    await ctx.send('***ERROR: Unknown entries***')
    return
  embed.set_author(name="Comet Calculator")
  await ctx.send(embed=embed)

# START OF THE ECONOMY SECTION
shopItems = [{'name':'Feet Pic','price':100,'description':'Someone\'s feet pics. Using them will give you a special surprise.'},
  {'name':'Comet Emotion Engine','price':10,'description':'The emotion engine ***Comet*** has. Gives a multiplier of 2*`amount you use`. Doesn\'t stack with other multipliers'},
  {'name':'Gun','price':1000,'description':'Used to shoot.'},
  {'name':'Laptop','price':500,'description':'Use it to surf the Web'},
  {'name':'Phone','price':500,'description':'The Castillo Phone 2XS Pro MAX. Use #phone to be able to scam people and do other things.'},
  {'name':'Padlock','price':2000,'description':'Protect yourself from being robbed. Do #use <amount> padlock to use it.'},
  {'name':'Fuck Card','price':2000,'description':'#fuck to use it. Tho why would you buy it you horny bastard.'}]

@client.command()
async def emo(ctx, *, member: discord.Member=None):
  try:
    asset = await ctx.message.attachments[0].save(ctx.message.attachments[0].filename)

    pfp = Image.open(ctx.message.attachments[0].filename)
  except:
    if member == None:
      member = ctx.author
    
    asset = member.avatar_url_as(size=512)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
  
  emoOverlay = Image.open('emoOverlay.png')
  pfp = pfp.resize((512,512))
  emoOverlay = emoOverlay.resize((512,512))

  pfp.paste(emoOverlay, (0, 0), emoOverlay)
  pfp.save('emoPic.png')

  await ctx.reply(file = discord.File('emoPic.png'), mention_author=False)
  try:
    os.remove(ctx.message.attachments[0].filename)
    os.remove('emoPic.png')
    os.system('touch emoPic.png')
  except:
    os.remove('emoPic.png')
    os.system('touch emoPic.png')

@client.command(aliases=['queer','gay','pride'])
async def lgbt(ctx, member: discord.Member=None, flag: str=None):
  try:
    asset = await ctx.message.attachments[0].save(ctx.message.attachments[0].filename)

    pfp = Image.open(ctx.message.attachments[0].filename)
  except:
    if member == None:
      member = ctx.author
    
    asset = member.avatar_url_as(size=512)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
  
  prideOverlays = ['/home/runner/CometBot/prideTemplates/prideHearts.png',
  '/home/runner/CometBot/prideTemplates/prideOverlay.png',
  '/home/runner/CometBot/prideTemplates/prideCornerOverlay.png']

  if flag != None:
    prideOverlay = Image.open(f'/home/runner/CometBot/prideTemplates/{flag}.png')
  else:
    prideOverlay = Image.open(random.choice(prideOverlays))
  
  pfp = pfp.resize((512,512))
  prideOverlay = prideOverlay.resize((512,512))

  pfp.paste(prideOverlay, (0, 0), prideOverlay)
  pfp.save('pridePic.png')

  await ctx.reply(file = discord.File('pridePic.png'), mention_author=False)

  try:
    os.remove(ctx.message.attachments[0].filename)
    os.remove('pridePic.png')
    os.system('touch pridePic.png')
  except:
    os.remove('pridePic.png')
    os.system('touch pridePic.png')

# Code made by KITECO on GitHub
# This version of their code was adapted for use in Discord
@client.command()
async def ascii(ctx, *, member: discord.Member=None):
  if member == None:
    member = ctx.author
  
  asset = member.avatar_url_as(size=64)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  pfp.save('pfp.png')

  image = Image.open('pfp.png')
  ASCII_CHARS = ["☐", "◲", "◰", "◳", "▽", "◁", "▨", "▧", "▣", "▩", "▤"]

  # resize image according to a new width
  def resize_image(image, new_width=40):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

  # convert each pixel to grayscale
  def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
  # convert pixels to a string of ascii characters
  def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

  try:
    image = Image.open("pfp.png")
  except:
    await ctx.send('RE-CREATE THE pfp.png FILE ASAP WHEREVER YOU\'RE HOSTING THE BOT')
    return
  async with ctx.typing():
    # convert image to ascii    
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+40)] for index in range(0, pixel_count, 40)])

    embed=discord.Embed(description=f"{ascii_image}", color=0x34363b)
    embed.set_footer(text=f"ᑌᑎIᑕOᗪE ᑭᗩIᑎTIᑎG Oᖴ {member.name}'ᔕ ᑭᖴᑭ")
  
  os.remove('pfp.png')
  os.system('touch pfp.png')
  await ctx.send(embed=embed)

@client.command(pass_context=True)
async def wanted(ctx, member:discord.Member=None):
  try:
    asset = await ctx.message.attachments[0].save(ctx.message.attachments[0].filename)

    pfp = Image.open(ctx.message.attachments[0].filename)
    nick = ctx.message.attachments[0].filename
  except:
    if member == None:
      member = ctx.author
    
    if member.name == None:
      nick = member.name
    else:
      nick = member.nick
  
    asset = member.avatar_url_as(size=256)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

  wanted = Image.open("wanted.png")
  draw = ImageDraw.Draw(wanted)
  font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 35)

  reward = ['Nothing','Amogus','$10 or even ¢1', '$0', '$100', '$500', '$1,000', '$5,000', '$10,000','$20,000','$25,000','$50,000','$60,000','$75,000','$85,000','$100,000','$150,000','$250,000','$1,000,000','My Heart \u2665']

  pfp = pfp.resize((305,305))
  draw.text((101,150), f"{nick}", font=font, fill=(23, 23, 80))
  wanted.paste(pfp, (101,190))
  draw.text((101,506), f"REWARD:", font=font, fill=(23, 23, 80))
  draw.text((101,540), f"{random.choice(reward)}", font=font, fill=(23, 23, 80))
  wanted.save('wantedPoster.png')

  await ctx.reply(file = discord.File('wantedPoster.png'), mention_author=False)

  try:
    os.remove(ctx.message.attachments[0].filename)
    os.remove('wantedPoster.png')
    os.system('touch wantedPoster.png')
  except:
    os.remove('wantedPoster.png')
    os.system('touch wantedPoster.png')

@client.command(pass_context=True)
async def arrest(ctx, member:discord.Member=None, *, reason=None):
  if member == None:
    member = ctx.author

  arrest = Image.open("arrestWarrant.png")
  draw = ImageDraw.Draw(arrest)
  font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 25)
  font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 13)
  font3 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 18)

  draw.text((30,240), f"{member.nick}", font=font1, fill=(23, 23, 80))
  draw.text((371,83), f"{ctx.guild.name} Server", font=font2, fill=(23, 23, 80))
  draw.text((244,452), f"{member.nick} ({member.name})", font=font2, fill=(23, 23, 80))
  draw.text((627,175), f"{member.id}", font=font2, fill=(23, 23, 80))
  draw.text((79,780), f"{datetime.today().strftime('%d-%m-%Y')}", font=font2, fill=(23, 23, 80))
  draw.text((36,616), f"{reason}", font=font3, fill=(23, 23, 80))
  arrest.save('arrest.png')

  await ctx.reply(file = discord.File('arrest.png'), mention_author=False)

@client.command(pass_context=True)
async def deathnote(ctx, member:discord.Member=None):
  if member == None:
    member = ctx.author
  
  wanted = Image.open("deathnote.jpg")
  font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 35)
  textToRotate=Image.new('L', (500,50))
  textDraw = ImageDraw.Draw(textToRotate)
  
  if member.nick == None:
    textDraw.text((0, 0), f"{member.name}",  font=font, fill=255)
  else:
    textDraw.text((0, 0), f"{member.nick}",  font=font, fill=255)

  w = textToRotate.rotate(17.5,  expand=1)
  wanted.paste(ImageOps.colorize(w, (0,0,0), (23,23,80)), (116,-10),  w)
  wanted.save('deathNote.jpg')

  await ctx.reply(file = discord.File('deathNote.jpg'), mention_author=False)

@client.command(aliases=['lead','Lead','Leaderboard','lb','ul'])
async def leaderboard(ctx, number=3):
  with open('bank.json','r') as f:
    users = json.load(f)
  total = []

  for user in ctx.guild.members:
    try:
      name = str(user.id)
      totalAmount = users[str(user.id)]['Wallet'] + users[str(user.id)]['Bank']
      thingToAppend = [user.name, totalAmount]
      total.append(thingToAppend)
    except:
      uselessVariable = 1

  total.sort(reverse=True, key=lambda totalThing: totalThing[1])

  embed=discord.Embed(title=f"‣‣‣‣‣‣‣‣‣‣‣ Top {number} Users of {ctx.guild.name} ‣‣‣‣‣‣‣‣‣‣‣‣", color=0x0502c5)

  index = 1
  if number > len(total):
    number = int(len(total))
  
  loopCount = 0
  rankDisplay = '```'
  for entry in total:
    if loopCount < number:
      rankDisplay += f'{index}. {entry[0]}:\nTotal Balance {entry[1]}\n'
      index += 1
      loopCount += 1

  rankDisplay += '```'
  embed.add_field(name = '--------------------------', value=f'{rankDisplay}', inline=False)

  embed.set_author(name="The ※ Rank System ※")
  embed.set_thumbnail(url="https://images.vexels.com/media/users/3/135932/isolated/preview/5873339dddecea4a26d7366462d0eec6-checklist-file-icon-by-vexels.png")
  embed.set_footer(text="Comet Economy Alert")
  await ctx.send(embed=embed)

@client.command(aliases=['lock'])
async def use(ctx, amount=1, *, itemName=None):
  with open('bank.json','r') as f:
    users = json.load(f)
  user = ctx.author

  bal = await updateBank(user)

  res = await useThis(ctx.author, itemName, amount)

  if not res[0]:
    if res[1] == 1:
      await ctx.reply('Item doesn\'t exist.', mention_author=False)
      return
    if res[1] == 2:
      await ctx.reply(f'You don\'t have {amount} {itemName}.', mention_author=False)
      return
    if res[1] == 3:
      await ctx.reply(f'You don\'t own {itemName}.', mention_author=False)
  
  if itemName == 'padlock':
    await updateBank(ctx.author, amount, 'Active Padlocks')
 
    print(bal[2])
    await ctx.reply(f'You have used {amount} padlocks.', mention_author=False)
  if itemName == 'Comet emotion engine':
    if bal[3] > 0:
      await updateBank(ctx.author, -1*bal[3], 'Coin Multiplier')

    await updateBank(ctx.author, 2*amount, 'Coin Multiplier')
 
    print(bal[2])
    await ctx.reply(f'You have used {amount} {itemName}s. Your Chem Coin (⌬) multiplier is now at {2*amount} when you beg for the next 5 minutes.', mention_author=False)
    await asyncio.sleep(300)
    await ctx.reply('Your multiplier ran out.', mention_author=False)
    await updateBank(ctx.author, -1*bal[3], 'Coin Multiplier')
  if itemName == 'feet pic':
    dies = bool(random.getrandbits(1))
    if dies:
      await updateBank(ctx.author, 1, 'Deaths')

      responses=['The photographer sees you had a feet pic of hers and snaps your neck. You die :man_facepalming:',
        'You saw the feet pic and liked it. Due to this, the image combusts on fire, burning you to a crisp in an instant.',
        'When you saw the feet pic it became sentient and stabbed you. You died.']
      await ctx.reply(f'{random.choice(responses)}', mention_author=False)
    else:
      await updateBank(ctx.author, 1, 'Deaths')

      responses=['You saw the picture and nothing happened.',
        'You saw the feet pic and liked it. The photographer of the feet pics looks at you in disgust. :sick:',
        'The feet pic desintegrated. You were unable to see its contents.']
      await ctx.reply(f'{random.choice(responses)}', mention_author=False)

@client.command(aliases=['gun'])
async def shoot(ctx, member:discord.Member):
  await openBankAccount(ctx.author)
  user = ctx.author
  gunCount = 0
  with open('bank.json','r') as f: users = json.load(f)
  
  for item in users[str(user.id)]['Inventory']:
    if item['Item'] == 'gun' and item['Amount'] > 0:
      shootPass = bool(random.getrandbits(1))
      if shootPass == True:
        victimDies = bool(random.getrandbits(1))
        if victimDies == True:
          responses = [f'You shot {member.mention} and they die from it.',
            f'You basically turn {member.mention} to swiss cheese with all the rounds you used. Now I feel bad for them.',
            f'You fatally shot {member.nick}. \nhttps://tenor.com/view/machine-gun-stationary-gun-rocket-gun-trevante-rhodes-the-predator-gif-11846844',
            f'What a mess. You shot {member.mention} to a pulp\nhttps://tenor.com/view/machine-gun-stationary-gun-rocket-gun-trevante-rhodes-the-predator-gif-11846844']
          await ctx.reply(f'{random.choice(responses)}', mention_author=False)
        elif victimDies == False:
          responses = [f'WTF. {member.mention} was shot in the chest thrice, but they walked away like it was nothing.',
            f'You shot {member.mention}, but they somehow survive the shot despite the wound being in the neck.',
            f'The shot landed in {member.mention}\'s head, but the thing is that ~~it~~ they managed to heal on time for it to not be lethal.']
          await ctx.reply(f'{random.choice(responses)}', mention_author=False)
      elif shootPass == False:
        shooterDies = bool(random.getrandbits(1))
        if shooterDies == True:
          responses = [f'You shot {member.mention}, but the bullet missed them and richocheted towards you causing your death.',
            'Your eyesight is so bad you accidentanly shot yourself and died. Sucks to be you.',
            f'{member.mention} parried the bullet towards you and ended hitting you in the brain, causing your death.',
            f'The bullet ended up fireing, but it became sentient and fell in love with {member.mention}. As a result, the bullet changed course and hit you instead, causing your death.']
          await ctx.reply(f'{random.choice(responses)}', mention_author=False)
        if shooterDies == False:
          responses = ['The bullet ricocheted and hit you. You didn\'t die',
            f'You tried to shoot {member.mention}, but turns out you brought a bubble gun instead. They live.',
            f'The gun gets jammed. This unfortunately means that {member.mention} still lives.',
            'The gun was listening to Gotye and disintegrated because it was emo. It\'s last words were `You\'re just somebody I used to know.` before turning to dust.']
          await ctx.reply(f'{random.choice(responses)}', mention_author=False)
      gunCount += 1
      print(gunCount)

  if gunCount == 0:
    for x in range(1):
      await ctx.send('You don\'t have a gun.')

@client.command(aliases=['CastiPhone'])
async def phone(ctx):
  await openBankAccount(ctx.author)
  user = ctx.author
  gunCount = 0
  with open('bank.json','r') as f:
    users = json.load(f)
  
  for item in users[str(user.id)]['Inventory']:
    if item['Item'] == 'phone' and item['Amount'] > 0:
      embed=discord.Embed(title="Phone Options", description=f"Hey {user.mention}, click one of the buttons to do an action before the phone's battery runs out in 20 seconds.", color=0x00ffee)
      embed.set_thumbnail(url="https://images.vexels.com/media/users/3/128754/isolated/preview/d7966cba43a9c647bb596a02c6756f3f-smart-phone-icon-by-vexels.png")
      embed.set_footer(text="Castillo Phone")
      embed1 = await ctx.send(embed=embed,
      components = [
        [
          Button(style = ButtonStyle.red, label = "Scam"),
          Button(style = ButtonStyle.blue, label = "TTS on Voice Channel"),
          Button(style = ButtonStyle.green, label = "DM a User")
        ]
      ])
    
      def check(buttonCheck):
        return buttonCheck.channel == ctx.channel

      try:
        buttonCheck = await client.wait_for("button_click", timeout=20, check=check)

        if buttonCheck.component.label == 'Scam':
          await ctx.send('Ping the user you want to scam.')
          try:
            def check(m):
              return m.author == ctx.author

            msg = await client.wait_for('message', timeout=20, check=check)
            try:
              prepare1 = msg.content.replace('<@!', '')
              prepare2 = prepare1.replace('>', '')
              finalPrepare = int(prepare2)
            except:
              prepare3 = prepare2.replace('<@', '')
              finalPrepare = int(prepare3)

            userToScam = client.get_user(finalPrepare)
            print(userToScam)

            await ctx.invoke(client.get_command('rob'), member=userToScam, scam=True, phoneRobber=ctx.author)
          except asyncio.TimeoutError:
            await ctx.send('The phone\'s battery ran out.')
        elif buttonCheck.component.label == 'TTS on Voice Channel':
          await ctx.reply('Input the text you want ***Comet*** to say.', mention_author=False)
          try:
            def check(m):
              return m.author == ctx.author

            msg = await client.wait_for('message', timeout=20, check=check)

            await ctx.invoke(client.get_command('tts'), text=msg.content)
            await ctx.invoke(client.get_command('leave'))

          except asyncio.TimeoutError:
            await ctx.send('The phone\'s battery ran out.')
        elif buttonCheck.component.label == 'DM a User':
          await ctx.reply('Ping the user you want to send the message to (Don\'t worry I\'ll delete the ping).', mention_author=False)
          try:
            def check(m):
              return m.author == ctx.author

            msg = await client.wait_for('message', timeout=20, check=check)

            try:
              prepare1 = msg.content.replace('<@!', '')
              prepare2 = prepare1.replace('>', '')
              finalPrepare = int(prepare2)
            except:
              prepare3 = prepare2.replace('<@', '')
              finalPrepare = int(prepare3)
            userToDM = client.get_user(finalPrepare)

            await msg.delete()

            await ctx.reply('Now type what you want to send to the user.', mention_author=False)

            try:
              def check(m):
                return m.author == ctx.author

              msgText = await client.wait_for('message', timeout=20, check=check)
              await userToDM.send(f'New DM from a user in **`{ctx.guild.name}`**\n**__{ctx.author.id}__**: {msgText.content}')

            except asyncio.TimeoutError:
              await ctx.send('Your Mobile data ran out. Thank the 5 GB Haley-Mobile Data Plan.')

          except asyncio.TimeoutError:
            await ctx.send('The phone\'s battery ran out.')
      
      except asyncio.TimeoutError:
        await ctx.reply('exited the Phone', mention_author=False)
      
      gunCount += 1
      print(gunCount)

  if gunCount == 0:
    for x in range(1):
      await ctx.send('You don\'t have a gun.')

@client.command(aliases=['fck'])
async def fuck(ctx, *, member:discord.Member):
  await openBankAccount(ctx.author)
  user = ctx.author
  fckCardCount = 0
  with open('bank.json','r') as f:
    users = json.load(f)
  
  for item in users[str(user.id)]['Inventory']:
    if item['Item'] == 'fuck card' and item['Amount'] > 0:

      res = await useThis(ctx.author, 'fuck card', 1)

      if not res[0]:
        if res[1] == 1:
          await ctx.reply('Item doesn\'t exist.', mention_author=False)
          return
        if res[1] == 2:
          await ctx.reply(f'You don\'t have enough fuck cards.', mention_author=False)
          return
        if res[1] == 3:
          await ctx.reply(f'You don\'t own a fuck card.', mention_author=False)
          return
      
      responses = [f'{ctx.author.mention} stop it. Stop this now and apologize to {member.mention} for tring to fuck them.',
        'You\'re down bad.',
        ':sick: WTF is wrong with you.']
      await ctx.reply(f'{random.choice(responses)}', mention_author=False)

      fckCardCount += 1

  if fckCardCount == 0:
    for x in range(1):
      await ctx.send('You don\'t have a fuck pass.')


@client.command(aliases=['bqlance','bal','Bal','Balance'], pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def balance(ctx, *, member:discord.Member=None):
  if (member == None):
    user = ctx.author
    await openBankAccount(user)
  else:
    user = member
    await openBankAccount(user)

  with open('bank.json','r') as f:
    users = json.load(f)
  walletBalance = users[str(user.id)]["Wallet"]
  bankBalance = users[str(user.id)]["Bank"]
  multBalance = users[str(user.id)]["Coin Multiplier"]
  deathBalance = users[str(user.id)]["Deaths"]
  
  
  embed=discord.Embed(title=f"{user}'s ({user.nick}) Balance", description=f"Deaths: **``{deathBalance}``**            Multiplier: **``{multBalance}``**\n=========================", color=0xffe252)
  embed.set_author(name="Bank of Comet")
  embed.set_thumbnail(url="https://lh3.googleusercontent.com/7Kj8VrtBcnZkkmwn72PeB1NjG7CoR1K66ID67t4J6BgL1kH16u909npQ3mP795LT8Ebv=s85")
  embed.add_field(name="Wallet", value=f"{walletBalance} ⌬", inline=True)
  embed.add_field(name="Bank", value=f"{bankBalance} ⌬", inline=True)
  embed.set_footer(text="Comet Bank Alert")
  await ctx.reply(embed=embed, mention_author=False)

@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
  await openBankAccount(ctx.author)
  user = ctx.author
  with open('bank.json','r') as f:
    users = json.load(f)
  
  bal = await updateBank(user)
  
  if bal[3] > 0:
    newMax = bal[3]*350
    earnings = random.randrange(newMax)
  else:
    earnings = random.randrange(350)

  users[str(user.id)]['Wallet'] += earnings

  with open('bank.json','w') as f:
    json.dump(users, f)

  embed=discord.Embed(title=f"Hey, {ctx.author}!", description=f"A random entity has given you {earnings} ⌬!", color=0x78e84f)
  embed.set_author(name="Bank of Comet")
  embed.set_footer(text="Comet Bank Alert")
  await ctx.reply(embed=embed, mention_author=False)

@client.command(aliases=['tienda', 'Shop', 'Tienda'])
async def shop(ctx):
  await openBankAccount(ctx.author)
  embed=discord.Embed(title="Here is the catalog:", color=0xe066f0)
  embed.set_author(name="⛯ Comet Shop ⛯")

  for item in shopItems:
    name = item['name']
    price = item['price']
    description = item['description']

    embed.add_field(name = name, value=f'{price} ⌬ | {description}')

  embed.set_thumbnail(url="https://lh3.googleusercontent.com/3fLpNye5bvKbPe-5RzlXqyvbVo_dqx4SsCJOTq_WRM-AIVOrzCGWXG5g6GSex4xEOd2Wng=s85")
  embed.set_footer(text="Comet Shop Alert")
  await ctx.reply(embed=embed, mention_author=False)

@client.command(aliases=['inv'])
async def inventory(ctx, *, member:discord.Member=None):
  if (member == None):
    user = ctx.author
    await openBankAccount(user)
  else:
    user = member
    await openBankAccount(user)

  with open('bank.json','r') as f:
    users = json.load(f)

  try:
    inventory = users[str(user.id)]['Inventory']
  except:
    inventory = []

  embed=discord.Embed(title=f"{user.nick}'s Inventory", description='	⋈	⋈	⋈	⋈	⋈	⋈	⋈	⋈	⋈	⋈	⋈	⋈	⋈	⋈	⋈	⋈', color=0x3092e8)

  for item in inventory:
    name = item["Item"]
    amount = item["Amount"]

    if amount < 1:
      print('no')
    else:
      embed.add_field(name = name, value = amount)
  
  embed.set_author(name="Comet Economy")
  embed.set_thumbnail(url="https://images.vexels.com/media/users/3/207218/isolated/preview/05344875a64f53258bdffa5259380e18-luggage-bag-colorful-icon-stroke-by-vexels.png")
  embed.set_footer(text="Comet Economy Alert")
  await ctx.reply(embed=embed, mention_author=False)

@client.command(aliases=['comprar','Comprar','Buy'])
@commands.cooldown(1, 30, commands.BucketType.user)
async def buy(ctx, amount=1, *, itemName):
  await openBankAccount(ctx.author)

  res = await buyThis(ctx.author, itemName, amount)

  if not res[0]:
    if res[1] == 1:
      await ctx.reply('Item doesn\'t exist.', mention_author=False)
      return
    if res[1] == 2:
      await ctx.reply('You can\'t afford this.', mention_author=False)
      return
    
  await ctx.reply(f'You have purchased {amount} {itemName}', mention_author=False)

@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def sell(ctx, amount=1, *, itemName):
  await openBankAccount(ctx.author)

  res = await sellThis(ctx.author, itemName, amount)

  if not res[0]:
    if res[1] == 1:
      await ctx.reply('Item doesn\'t exist.', mention_author=False)
      return
    if res[1] == 2:
      await ctx.reply(f'You don\'t have {amount} {itemName}.', mention_author=False)
      return
    if res[1] == 3:
      await ctx.reply(f'You don\'t own {itemName}.', mention_author=False)
      return
    
  await ctx.reply(f'You have sold {amount} {itemName}.', mention_author=False)

async def buyThis(user, itemName, amount):
  item = itemName.lower()
  name_ = None

  for item in shopItems:
    name = item['name'].lower()
    if name == itemName:
      name_ = name
      price = item['price']
      break
  
  if name_ == None:
    return [False, 1]
  
  cost = price*amount

  with open('bank.json','r') as f:
    users = json.load(f)
  
  bal = await updateBank(user)

  if bal[0] < 0:
    return[False, 0]
  
  try:
    index = 0
    t = None
    for thing in users[str(user.id)]['Inventory']:
      n = thing['Item']
      if n == itemName:
        oldAmount = thing['Amount']
        newAmount = oldAmount + amount
        users[str(user.id)]['Inventory'][index]['Amount'] = newAmount
        t = 1
        break
      index += 1
    if t == None:
      obj = {'Item':itemName, 'Amount':amount}
      users[str(user.id)]['Inventory'].append(obj)
    
  except:
    obj = {'Item':itemName, 'Amount':amount}
    users[str(user.id)]['Inventory'] = [obj]

  with open('bank.json','w') as f:
    json.dump(users, f)
  
  await updateBank(user, cost*-1, 'Wallet')
  return[True,'worked']

async def sellThis(user, itemName, amount, price=None):
  item = itemName.lower()
  name_ = None

  for item in shopItems:
    name = item['name'].lower()
    if name == itemName:
      name_ = name
      if price == None:
        price = item['price']
      break
  
  if name_ == None:
    return [False, 1]
  
  cost = (price/2)*amount

  with open('bank.json','r') as f:
    users = json.load(f)
  
  bal = await updateBank(user)

  if bal[0] < 0:
    return[False, 0]
  
  try:
    index = 0
    t = None
    for thing in users[str(user.id)]['Inventory']:
      n = thing['Item']
      if n == itemName:
        oldAmount = thing['Amount']
        newAmount = oldAmount - amount
        if newAmount < 0:
          return [False,2]
        users[str(user.id)]['Inventory'][index]['Amount'] = newAmount
        t = 1
        break
      index += 1
    if t == None:
      return [False, 3] 
  except:
    return [False, 3]

  with open('bank.json','w') as f:
    json.dump(users, f)
  
  await updateBank(user, cost, 'Wallet')
  return[True,'worked']

async def useThis(user, itemName, amount):
  item = itemName.lower()
  name_ = None

  for item in shopItems:
    name = item['name'].lower()
    if name == itemName:
      name_ = name
      break
  
  if name_ == None:
    return [False, 1]

  with open('bank.json','r') as f:
    users = json.load(f)
  
  bal = await updateBank(user)

  if bal[0] < 0:
    return[False, 0]
  
  try:
    index = 0
    t = None
    for thing in users[str(user.id)]['Inventory']:
      n = thing['Item']
      if n == itemName:
        oldAmount = thing['Amount']
        newAmount = oldAmount - amount
        if newAmount < 0:
          return [False,2]
        users[str(user.id)]['Inventory'][index]['Amount'] = newAmount
        t = 1
        break
      index += 1
    if t == None:
      return [False, 3] 
  except:
    return [False, 3]

  with open('bank.json','w') as f:
    json.dump(users, f)
  
  return[True,'worked']

@client.command(aliases=['with','withdaw','With','Withdraw'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def withdraw(ctx, amount=None):
  await openBankAccount(ctx.author)
  if amount == None:
    await ctx.reply('Please input a valid number', mention_author=False)
    return
  
  bal = await updateBank(ctx.author)

  amount = int(amount)
  if amount > bal[1]:
    await ctx.reply('You don\'t have enough funds to withdraw.', mention_author=False)
    return
  if amount < 0:
    await ctx.reply('Input a positive number or use #deposit instead', mention_author=False)
    return
  
  await updateBank(ctx.author, amount)
  await updateBank(ctx.author, -1*amount,'Bank')

  await ctx.reply(f'Successfuly withdrew {amount} ⌬ from your bank.', mention_author=False)

@client.command(aliases=['dep','add','Deposit','Dep'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def deposit(ctx, amount=None):
  await openBankAccount(ctx.author)
  if amount == None:
    await ctx.reply('Please input a valid number', mention_author=False)
    return
  
  bal = await updateBank(ctx.author)

  amount = int(amount)
  if amount > bal[0]:
    await ctx.reply('You don\'t have enough funds to deposit.', mention_author=False)
    return
  if amount < 0:
    await ctx.reply('Input a positive number or use #withdraw instead', mention_author=False)
    return
  
  await updateBank(ctx.author, -1*amount)
  await updateBank(ctx.author, amount,'Bank')

  await ctx.reply(f'Successfuly deposited {amount} ⌬ from your bank.', mention_author=False)

@client.command(aliases=['Send','give'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def send(ctx, member:discord.Member, amount=None):
  await openBankAccount(ctx.author)
  await openBankAccount(member)
  if amount == None:
    await ctx.reply('Please input a valid number', mention_author=False)
    return
  
  bal = await updateBank(ctx.author)

  amount = int(amount)
  if amount > bal[0]:
    await ctx.reply('You don\'t have enough funds to send.', mention_author=False)
    return
  if amount < 0:
    await ctx.reply('Input a positive number.', mention_author=False)
    return
  
  await updateBank(ctx.author, -1*amount, 'Wallet')
  await updateBank(member, amount,'Wallet')

  await ctx.reply(f'Successfuly sent {amount} ⌬ to {member.mention}.', mention_author=False)

@client.command(aliases=['robar','Rob'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def rob(ctx, member:discord.Member, scam=False, phoneRobber=None):
  if phoneRobber == None:
    await openBankAccount(ctx.author)
    bal = await updateBank(ctx.author)
  else:
    await openBankAccount(phoneRobber)
    bal = await updateBank(phoneRobber)
  
  print(scam)
    
  await openBankAccount(member)
  padlockRemove = False
  padlockFailure = False
  
  balToRob = await updateBank(member)

  if balToRob[0] < 5:
    await ctx.reply('Leave them alone they\'re broke af.', mention_author=False)
    return
  if bal[0] < 10:
    await ctx.reply('You need more money to rob someone.', mention_author=False)
    return
  if balToRob[2] > 0:
    padlockRemove = 1
    await updateBank(member, -1*padlockRemove,'Active Padlocks')
    padlockFailure = True
  
  robPass = bool(random.getrandbits(1))

  if padlockFailure == True:
    safetyLimit = int(bal[0]/2)
    earnings = random.randrange(3, safetyLimit)
    if scam == False:
      responsesToPadlock = [f'Oof. {member.mention} had a lock in their wallet, which somehow makes your scam fail. For this you pay {member.mention} {earnings} ⌬',
        f'Spoiler alert: {member.mention} had a padlock. You pay them {earnings} ⌬ for the pathetic excuse of a scam you did lmao.',
        f'{member.mention} has an enabled padlock, which costed you {earnings} ⌬.']
    elif scam == True:
      responsesToPadlock = [f'Oof. {member.mention} had a lock in their wallet, which menas your robbery failed. For this you pay {member.mention} {earnings} ⌬',
        f'Spoiler alert: {member.mention} had a padlock. You pay them {earnings} ⌬ for the pathetic excuse of a robbery you did lmao.',
        f'{member.mention} has an enabled padlock, which costed you {earnings} ⌬.']

    await updateBank(ctx.author, -1*earnings, 'Wallet')
    await updateBank(member, earnings,'Wallet')
    await ctx.reply(f'{random.choice(responsesToPadlock)}', mention_author=False)
  elif robPass == True:
    earnings = random.randrange(0, balToRob[0])
    if scam == False:
      responses = [f'You\'re on a roll! You\'ve robbed {earnings} ⌬ {member.mention}',
        f'Successfuly robbed {member.mention} of {earnings} ⌬.',
        f'With help of the *V O I D*, you managed to steal {earnings} ⌬ from {member.mention}',
        f'You finnesed {member.mention}, meaning you took {earnings} ⌬ from them.',
        f'{member.mention} was so stupid, they tried to use a dildo to fight back, but you just knocked them out. You stripped them of {earnings} ⌬.']
    elif scam == True:
      responses = [f'WTF. Your pathetic excuse of a scam worked. You scammed {member.mention} and got {earnings} ⌬ from it.',
        f'You scammed granny {member.mention} and got {earnings} ⌬.']
    await updateBank(ctx.author, earnings, 'Wallet')
    await updateBank(member, -1*earnings,'Wallet')
    await ctx.reply(f'{random.choice(responses)}', mention_author=False)
  else:
    safetyLimit = int(bal[0]/2)
    earnings = random.randrange(3, safetyLimit)
    if scam == False:
      responses = [f'{member.mention} ended up scamming your old prince phillip-looking-ass. They ended up robbing {earnings} ⌬ from you. Ironic.',
        f'The Nigerian Prince scam against {member.mention} failed. You payed them {earnings} ⌬ to keep them from calling the police.',
        f'You fool. When you were distracted, {member.mention} called the police on you. They arrived to where you were and arrested you. You end up paying them {earnings} ⌬ in bail, which they end up giving to {member.mention}.']
    elif scam == True:
      responses = [f'When you were about to rob {member.mention}, they fought back and neutralized you. they ended up robbing {earnings} ⌬ from you. Ironic.',
        f'Robbery against {member.mention} failed. You payed them {earnings} ⌬ in compensation.',
        f'You fool. When you were distracted, {member.mention} took your wallet and when it was your turn to rob them, you took your wallet instead of theirs. When you checked it, {earnings} ⌬ were gone from it.']

    await updateBank(ctx.author, -1*earnings, 'Wallet')
    await updateBank(member, earnings,'Wallet')
    await ctx.reply(f'{random.choice(responses)}', mention_author=False)

@client.command(aliases=['slot','Slots','Slot'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def slots(ctx, amount=0):
  await openBankAccount(ctx.author)
  
  if amount == 0:
    await ctx.reply('Please input a valid number', mention_author=False)
    return
  
  bal = await updateBank(ctx.author)

  amount = int(amount)
  if amount > bal[0]:
    await ctx.reply('You don\'t have enough money to gamble.', mention_author=False)
    return
  if amount < 0:
    await ctx.reply('Input a positive number.', mention_author=False)
    return
  
  slot=[]
  for x in range(3):
    a = random.choice([':neutral_face:', ':cold_face:',':regional_indicator_b:', ':blue_heart:'])
    slot.append(a)

  if (slot[1] == slot [2] and slot[0] == slot[1]):
    reward = int(2*amount)
    embed=discord.Embed(title="The slots have decided", description=f"You won {reward} ⌬.", color=0x76f60e)
    embed.set_author(name="Comet Casino")
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/RHapVuBKiqZpODpQ8hDua-xQw6G4dzQG5w1HlXztJRE3Zu3WlRnEFawjjfyQsqILBEltOw=s85")
    embed.add_field(name="The Slot Result:", value=f"{slot[0]} {slot[1]} {slot[2]}", inline=True)
    embed.set_footer(text="Comet Bank Alert")
    await ctx.reply(embed=embed, mention_author=False)
    await updateBank(ctx.author, reward, 'Wallet')
  if (slot[1] == slot [2]) or (slot[0] == slot[1]) or (slot[0] == slot[2]):
    reward = int(1.5*amount)
    embed=discord.Embed(title="The slots have decided", description=f"You won {reward} ⌬.", color=0x76f60e)
    embed.set_author(name="Comet Casino")
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/RHapVuBKiqZpODpQ8hDua-xQw6G4dzQG5w1HlXztJRE3Zu3WlRnEFawjjfyQsqILBEltOw=s85")
    embed.add_field(name="The Slot Result:", value=f"{slot}", inline=True)
    embed.set_footer(text="Comet Bank Alert")
    await ctx.reply(embed=embed, mention_author=False)
    await updateBank(ctx.author, reward, 'Wallet')
  else:
    embed=discord.Embed(title="The slots have decided", description=f"You lost {amount} ⌬.", color=0xd03939)
    embed.set_author(name="Comet Casino")
    embed.set_thumbnail(url="https://lh3.googleusercontent.com/RHapVuBKiqZpODpQ8hDua-xQw6G4dzQG5w1HlXztJRE3Zu3WlRnEFawjjfyQsqILBEltOw=s85")
    embed.add_field(name="The Slot Result:", value=f"{slot}", inline=True)
    embed.set_footer(text="Comet Bank Alert")
    await ctx.send(embed=embed)
    await updateBank(ctx.author, -1*amount, 'Wallet')

async def openBankAccount(user):
  with open('bank.json','r') as f:
    users = json.load(f)
  
  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]['Wallet'] = 0
    users[str(user.id)]['Bank'] = 0
    users[str(user.id)]['Active Padlocks'] = 0
    users[str(user.id)]['Coin Multiplier'] = 0
    users[str(user.id)]['Deaths'] = 0
  
  with open('bank.json','w') as f:
    json.dump(users, f)
  return True

async def updateBank(user, change=0, mode='Wallet'):
  with open('bank.json','r') as f:
    users = json.load(f)
  
  users[str(user.id)][mode] += change

  with open('bank.json','w') as f:
    json.dump(users, f)
  
  bal = [users[str(user.id)]['Wallet'], users[str(user.id)]['Bank'], users[str(user.id)]['Active Padlocks'], users[str(user.id)]['Coin Multiplier'], users[str(user.id)]['Deaths']]
  return bal

# END OF THE ECONOMY SECTION

@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def spam(ctx):
  randomSpamImages=['https://tenor.com/view/spammer-no-spamming-dora-gif-19107257',
    'https://media.tenor.co/videos/aca9f2dd590c64cdae67682493439e7f/mp4']
  await ctx.send(f'{random.choice(randomSpamImages)}')

@client.command(aliases=['dn'],pass_context=True)
async def devnote(ctx):
  randomDevNotes = ['Dev Note #1: Comet started off as a joke by <@588931051103977494>',
    'Dev Note #2: Comet\'s codename is Wolf Rayet. :star:',
    'Dev Note #3: The bot is written in Python. :snake:',
    'Dev Note #4: Comet\'s is open source',
    'Dev Note #5: Comet Music Player supports text search.',
    'Dev Note #6: Hangman on an embed was hell.',
    'Dev Note #7: Comet was originally made for one server, but the creator decided to make it open source and readily available.',
    'Dev Note #8: The first warning system for the bot sucked because no matter where you went the warnings given in one place trasferred to another and the full potential of the warning system could only have been seen in one server. 2.0.0 Aldebaran fixes that.',
    'Dev Note #9: #tts originally played a tts message in text channels. It was changed to a voice channel TTS because people exploited it.',
    'Dev Note #10: #tts has multi-language support. This means that the bot can read text in Mandarin, English, Spanish, Armenian, Russian, etc.',
    'Dev Note #11: The bot has a wikipedia search that is inaccurate because of the API scrambling up the search term.',
    'Dev Note #12: T̵h̶e̸ ̵b̵l̷a̶c̵k̵l̵i̷s̴t̵ ̸i̵s̵ ̷w̸a̶t̵c̶h̶i̵n̷g̵ ̷y̴o̴u̶ ̷:̷)̵']
  await ctx.send(f'{random.choice(randomDevNotes)}')

@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def bad(ctx, *, option):
  print(option)
  badGifs=['https://tenor.com/view/mods-mods-bad-dancing-eggserver-gif-17255736',
    'https://tenor.com/view/mods-are-asleep-mods-sleeping-post-chicken-mods-sleep-gif-21077535',
    'https://tenor.com/view/leave-server-server-discord-server-ihate-this-server-this-server-sucks-gif-20569666',
    'https://tenor.com/view/this-server-sucks-this-server-sucks-server-sucks-gif-20441118',
    'https://tenor.com/view/this-sucks-gif-18258057',
    'https://tenor.com/view/hate-gif-9315550',
    'https://tenor.com/view/lego-batman-just-saying-ihate-this-place-gif-7809561']
  await ctx.send(f'{random.choice(badGifs)}')

@client.command(description="Returns all commands available")
async def help(ctx, pg=1):
  embedCommands = 0
  embed=discord.Embed(title=f"List of all commands: Page {pg}", color=0x34363b)
  embed.set_author(name="Help Center")
  embed.set_thumbnail(url="https://images.vexels.com/media/users/3/153750/isolated/preview/1fb0b5422a7584ed0df14dfacdc68c64-internet-settings-colored-stroke-icon-by-vexels.png")
  embed.set_footer(text="Comet Alert")

  if pg == 2:
    embedCommands = 19
  if pg == 3:
    embedCommands = 37
  if pg == 4:
    embedCommands = 55
  if pg == 5:
    embedCommands = 69

  for command in client.commands:
    if embedCommands <= 18:
      embed.add_field(name=f'{command} | {command.aliases}', value=command.help, inline=True)
      embedCommands += 1
    elif embedCommands <= 36:
      embed.add_field(name=f'{command} | {command.aliases}', value=command.help, inline=True)
      embedCommands += 1
    elif embedCommands <= 54:
      embed.add_field(name=f'{command} | {command.aliases}', value=command.help, inline=True)
      embedCommands += 1
    else:
      embed.add_field(name=f'{command} | {command.aliases}', value=command.help, inline=True)
      embedCommands += 1
  
  await ctx.send(embed=embed)

@client.command(aliases=['weather','heavy weather'])
@commands.cooldown(1, 5, commands.BucketType.guild)
async def weatherReport(ctx):
  APIKEY = os.getenv('apiKey')
  api_key = APIKEY

  base_url = "http://api.openweathermap.org/data/2.5/weather?"

  def check(msg):
    return msg.author == ctx.author

  try:
    await ctx.send("`Input your city now:`")
    grabCity = await client.wait_for('message', check=check, timeout=15)
    city = grabCity.content

  except asyncio.TimeoutError:
    await ctx.send(f'**Y\'know** I don\'t have time for this, {ctx.author.mention}. Sorry.')
    return weatherReport

  complete_url = base_url + "appid=" + api_key + "&q=" + city

  response = requests.get(complete_url)

  cityList = response.json()

  if cityList["cod"] != "404":
    y = cityList["main"]

    current_temperature = y["temp"]

    current_pressure = y["pressure"]

    current_humidiy = y["humidity"]

    z = cityList["weather"]
    weather_description = z[0]["description"]

    tempToConvert = current_temperature
    celcisus_temp = tempToConvert - 273.15
    fahrenheit_temp = celcisus_temp * ( 9 / 5 ) + 32
  
    embed=discord.Embed(description=f"Temperature (in fahrenheit): __**{'{:.2f}'.format(fahrenheit_temp)}\u00b0**__\nAtmospheric pressure (in hPa unit): **__{str(current_pressure)}__**\nHumidity: **__{str(current_humidiy)}\u0025__**\nDescription: **__{str(weather_description)}__**", color=0x34363b)
    embed.set_thumbnail(url="https://png.pngtree.com/png-clipart/20190924/original/pngtree-planet-earth-icon-design-png-image_4804418.jpg")
    embed.set_author(name=f"Weather Report for {city.upper()} by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
  
  else:
    await ctx.send("`Your city of choice was not found.`")

@client.command(help='Use it with chat or server when they are dead.')
@commands.cooldown(1, 10, commands.BucketType.user)
async def dead(ctx, *, Type=None):
  if (str(type) == 'server'):
    deadServerPictures=['https://tenor.com/view/server-gif-18897740',
      'https://tenor.com/view/delete-server-gif-19419553']
    await ctx.channel.send(f'{random.choice(deadServerPictures)}')
  elif ((type == None) or (str(type) != 'server')):
    deadChatPictures = ['https://tenor.com/view/chat-dead-text-death-gif-19179369',
      'https://tenor.com/view/discord-dead-chat-dead-chat-minion-gif-20123384',
      'https://tenor.com/view/dead-chat-gif-18800792',
      'https://tenor.com/view/rip-chat-chat-dead-dead-chat-inactive-gif-18754855',
      'https://tenor.com/view/chat-dead-gif-18627672',
      'https://tenor.com/view/ded-chat-gif-18697462',
      'https://tenor.com/view/dead-chat-skull-gif-20745884',
      'https://tenor.com/view/among-ass-dead-chat-gif-19388942',
      'https://tenor.com/view/dead-chat-gif-20589759',
      'https://tenor.com/view/dead-chat-dead-chat-xd-gif-18811908',
      'https://tenor.com/view/dead-chat-gif-20279065',
      'https://tenor.com/view/chat-dead-dead-chat-xd-chat-dead-xd-dynamis-gif-19781344',
      'https://tenor.com/view/dead-chat-gif-20130964',
      'https://tenor.com/view/dead-chat-xd-gif-20055373',
      'https://tenor.com/view/dead-chat-xd-dead-chat-xd-gif-19751064',
      'https://tenor.com/view/among-us-sus-dead-chat-funny-gif-20236607']
    await ctx.channel.send(f'{random.choice(deadChatPictures)}')

@client.command(aliases=['wap','wet ass pussy','cardi b','Cardi B'], help='WAP command')
@commands.cooldown(1, 10, commands.BucketType.user)
async def WAP(ctx):
  WAPGifs=['https://tenor.com/view/cony-gif-18157436',
    'https://tenor.com/view/bloxton-bh-wap-willy-wonka-bloxton-hotels-gif-18343918',
    'https://tenor.com/view/coronavirus-cardi-b-virus-rap-laugh-gif-16654093',
    'https://tenor.com/view/wapwapwap-wap-wet-ass-pussy-pussy-sex-gif-18695914',
    'https://tenor.com/view/wap-wap-wap-wap-wap-wap-shower-showering-gif-19821044',
    'https://tenor.com/view/wap-twerking-gif-18115031',
    'https://tenor.com/view/whores-wap-cardi-b-theres-some-whores-in-this-house-gif-18753578']
  
  await ctx.send(f'{random.choice(WAPGifs)}')

@client.command(aliases=['slurAdd','addSlur'], pass_context=True)
@commands.has_permissions(kick_members=True)
async def addWord(ctx, *, wordToAdd):
  global bannedWords
  word = wordToAdd.lower()
  httpsResult = word.startswith('https')
  if httpsResult == True:
    print('punctuation removal skipped due to it being a link')
  else:
    word = word.translate(str.maketrans('', '', string.punctuation))
  
  with open("slurs.json", "r") as slurs:
    slurPrepare = json.load(slurs)
  print(ctx.guild.id)

  if str(ctx.guild.id) in slurPrepare:
    uselessVariable = 1
  else:
    slurPrepare[ctx.guild.id] = []
  
  slurPrepare[str(ctx.guild.id)].append(word)
    
  with open('slurs.json','w') as f:
    json.dump(slurPrepare, f)

  await ctx.send(f'Added {wordToAdd} to the blacklist.')

@client.command(aliases=['slurRemove','removeSlur','unslur'], pass_context=True)
@commands.has_permissions(kick_members=True)
async def removeWord(ctx, *, wordToRemove):
  global bannedWords
  word = wordToRemove.lower()
  httpsResult = word.startswith('https')
  if httpsResult == True:
    print('punctuation removal skipped due to it being a link')
  else:
    word = word.translate(str.maketrans('', '', string.punctuation))
  
  with open("slurs.json", "r") as slurs:
    slurPrepare = json.load(slurs)
  print(ctx.guild.id)

  if str(ctx.guild.id) in slurPrepare:
    pass
  else:
    slurPrepare[ctx.guild.id] = []
  
  slurPrepare[str(ctx.guild.id)].remove(word)
    
  with open('slurs.json','w') as f:
    json.dump(slurPrepare, f)
  
  await ctx.send(f'Removed {wordToRemove} from the blacklist.')
  return bannedWords

#Snipe commands
@client.command(aliases=['ssnipe','snipe+'],help='A super snipe command for snitches')
async def SuperSnipe(ctx, *, messageToRetrieve: int=1):
  channel = ctx.channel

  try:
    if messageToRetrieve < 0:
      await ctx.send('***Value too low. TF***')
    if messageToRetrieve == 1:
      embed = discord.Embed(title=f"{snipeMessageAuthor[channel.id]}", description=f'{snipeMessage[channel.id]}', color=0x2f3136)
      embed.set_author(name=f"Snipe Page 1: {channel.name}")
      embed.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/snipeIcon.png")
      embed.set_footer(text=f"Sniper: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    if messageToRetrieve == 2:
      embed = discord.Embed(title=f"{snipeMessageAuthor2[channel.id]}", description=f'{snipeMessage2[channel.id]}', color=0x2f3136)
      embed.set_author(name=f"Snipe Page 2: {channel.name}")
      embed.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/snipeIcon.png")
      embed.set_footer(text=f"Sniper: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    if messageToRetrieve == 3:
      embed = discord.Embed(title=f"{snipeMessageAuthor3[channel.id]}", description=f'{snipeMessage3[channel.id]}', color=0x25d9f8)
      embed.set_author(name=f"Snipe Page 3: {channel.name}")
      embed.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/snipeIcon.png")
      embed.set_footer(text=f"Sniper: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    mg = await ctx.send(embed=embed, components=[[
      Button(style = ButtonStyle.red, label = "1"),
      Button(style = ButtonStyle.blue, label = "2"),
      Button(style = ButtonStyle.green, label = "3"),
    ]])

    while True:
      def check(buttonCheck):
        return buttonCheck.channel == ctx.channel
      
      try:
        buttonCheck = await client.wait_for("button_click", check=check)

        await buttonCheck.respond(content='Changing Super Snipe Page')
        if buttonCheck.component.label == '1':
          embed2 = discord.Embed(title=f"{snipeMessageAuthor[channel.id]}", description=f'{snipeMessage[channel.id]}', color=0x2f3136)
          embed2.set_author(name=f"Snipe Page 1: {channel.name}")
          embed2.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/snipeIcon.png")
          embed2.set_footer(text=f"Sniper: {buttonCheck.user.name}#{buttonCheck.user.discriminator}", icon_url=buttonCheck.user.avatar_url)
          await mg.edit(embed=embed2)
        if buttonCheck.component.label == '2':
          embed2 = discord.Embed(title=f"{snipeMessageAuthor2[channel.id]}", description=f'{snipeMessage2[channel.id]}', color=0x2f3136)
          embed2.set_author(name=f"Snipe Page 2: {channel.name}")
          embed2.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/snipeIcon.png")
          embed2.set_footer(text=f"Sniper: {buttonCheck.user.name}#{buttonCheck.user.discriminator}", icon_url=buttonCheck.user.avatar_url)
          await mg.edit(embed=embed2)
        if buttonCheck.component.label == '3':
          embed2 = discord.Embed(title=f"{snipeMessageAuthor3[channel.id]}", description=f'{snipeMessage3[channel.id]}', color=0x2f3136)
          embed2.set_author(name=f"Snipe Page 3: {channel.name}")
          embed2.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/snipeIcon.png")
          embed2.set_footer(text=f"Sniper: {buttonCheck.user.name}#{buttonCheck.user.discriminator}", icon_url=buttonCheck.user.avatar_url)
          await mg.edit(embed=embed2)
      except:
        pass
  except:
    embed=discord.Embed(title=" ", color=0x34363b)
    embed.set_author(name=f"𝙉𝙤 𝙀𝙣𝙩𝙧𝙞𝙚𝙨 𝙍𝙚𝙘𝙤𝙧𝙙𝙚𝙙, {ctx.author.name}")
    await ctx.send(embed=embed)

@client.command(aliases=['retrieve','snitch','Snipe'], pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def snipe(ctx):
  channel = ctx.channel
  try:
    embed = discord.Embed(title=f"{regularSnipeAuthor[channel.id]}", description=f'{regularSnipeMessage[channel.id]}', color=0x2f3136)
    embed.set_footer(text=f"Sniper: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/snipeIcon.png")

    try:
      embed.set_image(url=f"attachment://{regularSnipeImage[channel.id].filename}")
    except: pass

    embed.set_author(name=f"Snipe: {channel.name}")
    try:
      await ctx.send(file=regularSnipeImage[channel.id], embed=embed)
    except:
      await ctx.send(embed=embed)
  except:
    embed=discord.Embed(title=" ", color=0x2f3136)
    embed.set_author(name=f"⚝ 𝙉𝙤 𝙀𝙣𝙩𝙧𝙮 𝙍𝙚𝙘𝙤𝙧𝙙𝙚𝙙, {ctx.author} ⚝")
    await ctx.send(embed=embed)

# Hello command
# First command in Comet
# @client.command(help='Hello command')
# @commands.cooldown(1, 10, commands.BucketType.user)
# async def hello(ctx):
#  await ctx.send('Hello human!')

#Spinning GIF code
@client.command(aliases=['spin'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def spanImages(ctx):
  randomSpinningImages=['https://media.discordapp.net/attachments/424269924349771786/820415854180565032/xqcSpinDiscord.gif',  'https://tenor.com/view/homer-simpson-twister-happy-spin-gif-13726615',
    'https://tenor.com/view/spinning-seal-water-funny-gif-5129604',
    'https://tenor.com/view/spin-dance-twirling-monkey-gif-9406313',
    'https://tenor.com/view/cat-spin-record-cute-gif-16753412',
    'https://tenor.com/view/doge-such-spin-spin-dizzy-doge-spin-gif-4981760',
    'https://tenor.com/view/fan-spinning-camera-go-pro-dizzy-gif-5297858']
  await ctx.send(f'{random.choice(randomSpinningImages)}')

# Would You Rather
@client.command(aliases=['wyr'])
@commands.cooldown(1, 3, commands.BucketType.user)
async def wouldyourather(ctx):
  wyrquestions = ['Would you rather have the ability to see 10 minutes into the future or 150 years into the future?','Would you rather have telekinesis (the ability to move things with your mind) or telepathy (the ability to read minds)?','Would you rather team up with Wonder Woman or Captain Marvel?','Would you rather find true love today or win the lottery next year?','Would you rather be in jail for five years or be in a coma for a decade?','Would you rather be chronically under-dressed or overdressed?','Would you rather have everyone you know be able to read your thoughts or for everyone you know to have access to your Internet history?','Would you rather lose your sight or your memories?','Would you rather have universal respect or unlimited power?','Would you rather give up air conditioning and heating for the rest of your life or give up the Internet for the rest of your life?','Would you rather swim in a pool full of Nutella or a pool full of maple syrup?','Would you rather labor under a hot sun or extreme cold?',' Would you rather stay in during a snow day or build a fort?','Would you rather have a personal maid or a personal chef?','you r a penis','Would you rather be 11 feet tall or nine inches tall?','Would you rather communicate only in emoji or never be able to text at all ever again?','Would you rather be royalty 1,000 years ago or an average person today?',' Would you rather lounge by the pool or on the beach?','Would you rather wear the same socks for a month or the same underwear for a week?','Would you rather cuddle a koala or pal around with a panda?','Would you rather always be 10 minutes late or always be 20 minutes early?','Would you rather spend a week in the forest or a night in a real haunted house?','Would you rather find a rat in your kitchen or a roach in your bed?','Would you rather have a pause or a rewind button in your life?','Would you rather smash dababy or steven','Would you rather drink from a toilet or pee in a litter box?','Would you rather be forced to live the same day over and over again for a full year, or take 3 years off the end of your life?','Would you rather get a paper cut every time you turn a page or bite your tongue every time you eat?','Would you rather oversleep every day for a week or not get any sleep at all for four days?','Would you rather die in 20 years with no regrets or live to 100 with a lot of regrets?','Would you rather get trapped in the middle of a food fight or a water balloon fight?']
  await ctx.channel.send(f'{random.choice(wyrquestions)}')

#Random camera GIF code
@client.command(aliases=['caughtin4k'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def caught(ctx):
  randomCameras = ['https://tenor.com/view/extremely-rabbit-sticker-photo-photography-camera-gif-10133190',
    'https://tenor.com/view/camera-photo-photography-gif-6008441',
    'https://tenor.com/view/picture-accidental-selfie-camera-fail-grandma-pictures-photography-gif-10048935',
    'https://tenor.com/view/national-camera-day-camera-shot-selfie-gif-12084418']
  await ctx.channel.send(f'{random.choice(randomCameras)}')

#8ball code
@client.command(aliases=['8ball', 'truther'], help='A sassy 8Ball. Also known as truther\nUse #8ball or #truther to use it!')
async def _8ball(ctx, *, question):
  responses = ['Certain. Its only a matter of time now',
    'It is decidedly so :smiley:',
    '¡Sin duda!',
    'Definitely yes. Don\'t worry about it!',
    'No. JK, you can rely on it with your life!',
    'From the looks of it, yes!', 'From what I see, yes!',
    'Probably',
    'Good chance it\'s yes...',
    'Yes :smiley:',
    'Signs are pointing to yes...',
    'The reply I have is hazy af. Try again or ask a different question :|',
    'Too busy breaking my own code. Try saying that again :no_mouth:',
    'I\'m not telling you that rn :no_mouth:',
    'I\'m too busy to predict rn. Try again l8r :rage:',
    'Concentrate porque ahorita se estas sonando como un troglodita...:rage:',
    'Don\'t try to count on this.',
    'I\'m telling you, it\'s a NO! :{',
    'Sources close to me have spoken. They say ***N O P E***',
    'Forecast is bad for this one...\u047e',
    'I\'m very doubtful about this one...\u047c']

  await ctx.send(f'The question was: {question}\n:8ball: My answer is: {random.choice(responses)}')

@client.command(aliases=['delete', 'delet', 'clear','del'], help='Clear command obviously.')
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def purge(ctx, maxamount=30):
  await ctx.message.delete()
  await ctx.channel.purge(limit=maxamount)
  await ctx.channel.send(f'Deleted **{maxamount}** messages.', delete_after=5)

@client.command(aliases=['dababy', 'dacar'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def dababyCommand(ctx):
  daBabyGIFs=['https://tenor.com/view/dababy-rapper-hip-hop-rap-digibyte-gif-17582117',
    'https://tenor.com/view/lets-go-im-ready-its-time-lets-get-it-bop-live-gif-15820219',
    'https://tenor.com/view/da-baby-baby-db-dance-smile-gif-15748120',
    'https://tenor.com/view/da-baby-lets-go-lets-goo-lets-gooo-lets-goooo-gif-16298213',
    'https://tenor.com/view/da-baby-suge-jonathan-lyndale-kirk-gif-15028096',
    'https://tenor.com/view/da-baby-bop-dance-charlotte-groove-gif-16081053',
    'https://tenor.com/view/dababy-convertable-gif-20206040',
    'https://tenor.com/view/dababy-gif-20863730',
    'https://tenor.com/view/dababy-gif-20861878',
    'https://tenor.com/view/bpm-dababy-stfu-gif-20869699']
  await ctx.channel.send(f'{random.choice(daBabyGIFs)}')

# Gives a random fact - super simple
# By Garen
@client.command(aliases=['rf', 'randomfact'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def Arandomfack(ctx):
  fct = randfacts.getFact()
  await ctx.send(fct)

@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def crusader(ctx):
  crusaderGifs=['https://tenor.com/view/unacceptable-knight-lock-and-load-cocks-gun-gif-17380126',
    'https://tenor.com/view/deus-vult-crusades-shake-triggered-intensifies-gif-16436511',
    'https://tenor.com/view/meme-soniknowreligionisimportant-crusader-dues-vult-gif-11697017',
    'https://tenor.com/view/crusade-cyber-fashwave-crusader-glitch-gif-19022516',
    'https://tenor.com/view/crusader-shocked-shotgun-gif-17982096',
    'https://tenor.com/view/crusader-uno-reverse-crusader-uno-reverse-uno-crusader-uno-reverse-red-eyes-gif-17741833']
  await ctx.send(f'{random.choice(crusaderGifs)}')

# This game was possible thanks to Garen
# tic tac toe
player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":purple_square:", ":purple_square:", ":purple_square:",
                 ":purple_square:", ":purple_square:", ":purple_square:",
                 ":purple_square:", ":purple_square:", ":purple_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress you whore!")

@client.command(pass_context=True)
@commands.cooldown(1, 3, commands.BucketType.user)
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":purple_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the #tictactoe command.")

def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

# End of the #tictactoe game by garen

@client.command(aliases=['Hangman', 'hangma'], help='hangman duh')
@commands.cooldown(1, 10, commands.BucketType.user)
async def hangman(ctx):
  tries = 0
  guess = None
  wonHangman = False
  hiddenWord=[]
  
  randomEmojis=[':smiley:',':cry:',':rofl:',':cold_face:',':neutral_face:',':grimacing:']
  hangmanPoses = ['==========\n\u2225||        ||\u2225\n\u2225||        ||\u2225\n\u2225\n\u2225\n\u2225\n\u2225\n++++++++++++++++',
    f'==========\n\u2225||--------||\u2225\n\u2225||--------||\u2225\n\u2225||--------||{random.choice(randomEmojis)}\n\u2225\n\u2225\n\u2225',
    f'==========\n\u2225||--------||\u2225\n\u2225||--------||\u2225\n\u2225||--------||{random.choice(randomEmojis)}\n\u2225||--------||\u2225\n\u2225\n\u2225\n++++++++++++++++',
    f'==========\n\u2225||--------||\u2225\n\u2225||--------||\u2225\n\u2225||--------||{random.choice(randomEmojis)}\n\u2225||--------||--|--\n\u2225\n\u2225\n\u2225\n++++++++++++++++',
    f'==========\n\u2225||--------||\u2225\n\u2225||--------||\u2225\n\u2225||--------||{random.choice(randomEmojis)}\n\u2225||--------||--|--\n\u2225||----------||\u2225\n\u2225\n\u2225\n++++++++++++++++',
    f'==========\n\u2225||--------||\u2225\n\u2225||--------||\u2225\n\u2225||--------||{random.choice(randomEmojis)}\n\u2225||--------||--|--\n\u2225||----------||\u2225\n\u2225||---------||/\\ \n\u2225\n++++++++++++++++']
  
  getWordList = urllib.request.urlopen("https://www.mit.edu/~ecprice/wordlist.10000")
  prepWordList = getWordList.read()
  words = prepWordList.splitlines()

  prepareWord = str(random.choice(words))
  while '\'' in prepareWord:
    prepareWord = prepareWord.replace('\'', '')
  
  prepareWord = prepareWord.replace('b','')

  word = list(prepareWord)
  hangmanEmbed = discord.Embed(description=hangmanPoses[tries], color=0x34363b)
  hangmanEmbed.set_author(name='Hangman by E.C.H.', icon_url=ctx.author.avatar_url)
  
  for character in word:
    hiddenWord.append('_')
    print(hiddenWord)
  
  while not wonHangman:
    print(word)

    def check(message):
      return message.author == ctx.author and message.channel == ctx.channel
    
    try:
      await ctx.send(embed=hangmanEmbed)
      await ctx.send(f"Put your guess before 15 seconds pass by.\n``The word is: {' '.join(hiddenWord)}``")
      grabUserInput = await client.wait_for('message', check=check, timeout=15)
      guess = grabUserInput.content

    except asyncio.TimeoutError:
      await ctx.send('**PLEEASE** if you\'re going to play **__FUCKING HANGMAN__** respond to it quickly :neutral_face:')
      guess = None
      tries = 0
      return hangman
    
    if guess in word:
      hangmanEmbed = discord.Embed(color=0x4dff82,description=hangmanPoses[tries])
      hangmanEmbed.set_author(name='You guessed a letter correctly 😁', icon_url=ctx.author.avatar_url)
      for i in range( len(word) ):
        print(i)
        character = word[i]
        if character == guess:
          hiddenWord[i] = word[i]
          word[i] = "_"
    else:
      tries += 1
      triesLeft = 6 - tries

      if tries < 6:
        hangmanEmbed = discord.Embed(color=0xff0033, description=hangmanPoses[tries])
        hangmanEmbed.set_author(name=f'Try that again. You got {triesLeft} tries left.', icon_url=ctx.author.avatar_url)
      if tries > 5:
        await ctx.send(f'**You lost**. Try again.\nThe word was **__{prepareWord}__**')
        tries = 0
        return hangman

    if all("_" == char for char in word):
      await ctx.send(f'**YOU WON**. The word was indeed **__`{prepareWord}`__**')
      wonHangman = True

@client.command(aliases=['zalgo','cursedtext'], help='Z̵̤ͫ A̋ͨ͝ L̬ͣ͡ G͊ͤ͜ Ö͕́̀')
@commands.cooldown(1, 10, commands.BucketType.guild)
async def makeZalgo(ctx, *, textToZalgofy: str):
  print(textToZalgofy)
  def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))
  
  chunks = list(chunkstring(textToZalgofy, 5))
  print(chunks)
  zalgoList = []
  for c in chunks:
    zalgofiedChunk = zalgo.zalgo().zalgofy(c)
    print(zalgofiedChunk)
    zalgoList.append(zalgofiedChunk)
  finalText = ''.join(zalgoList)
  await ctx.send(f'`{finalText}`')

@client.command(aliases=['rdit','Edit','stevenImproveUrSpelling', 'garentoo'], help='Edit command for snitches')
async def edit(ctx):
  try:
    embed=discord.Embed(title=f"Author: {regEditMessageAuthor[ctx.channel.id]}", color=0x2f3136)
    embed.set_author(name="Messaged Edited in {}".format(ctx.channel.name))
    embed.add_field(name="Before:", value=f"{regBeforeMessage[ctx.channel.id]}", inline=False)
    embed.add_field(name="After:", value=f"{regAfterMessage[ctx.channel.id]}", inline=True)
    await ctx.send(embed=embed)
  except:
    embed=discord.Embed(title=" ", color=0x0603bf)
    embed.set_author(name=f"⚝ 𝙉𝙤 𝙀𝙣𝙩𝙧𝙮 𝙍𝙚𝙘𝙤𝙧𝙙𝙚𝙙, {ctx.author} ⚝")
    await ctx.send(embed=embed)

def checkQueue1(id, server):
  ID = id
  theGuild = server
  FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

  if queues[id] != []:
    voiceChannel = discord.utils.get(client.voice_clients, guild=server)
    player = queues[id][0]
    del queues[id][0]
    del queueTitles[id][0]
    video, source, hours, mins, seconds = search(player)

    voiceChannel.play(discord.FFmpegPCMAudio(source, **FFMPEG_OPTS), after=lambda e: checkQueue2(ID, theGuild))

def checkQueue2(id, server):
  ID = id
  theGuild = server
  FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
  
  if queues[id] != []:
    voiceChannel = discord.utils.get(client.voice_clients, guild=server)
    player = queues[id][0]
    del queues[id][0]
    del queueTitles[id][0]
    video, source, hours, mins, seconds = search(player)

    voiceChannel.play(discord.FFmpegPCMAudio(source, **FFMPEG_OPTS), after=lambda e: checkQueue2(ID, theGuild))

@client.command(aliases=['r'])
async def remove(ctx, entry: int=1):
  entryToRemove = int(entry - 1)
  entryRemoved = queueTitles[ctx.guild.id][entryToRemove]
  del queues[ctx.guild.id][entryToRemove]
  del queueTitles[ctx.guild.id][entryToRemove]

  await ctx.reply(f'𝙍𝙚𝙢𝙤𝙫𝙚𝙙 ***__{entryRemoved}__*** 𝙛𝙧𝙤𝙢 𝙩𝙝𝙚 𝙦𝙪𝙚𝙪𝙚 :)')

@client.command(aliases=['p','P','Play'])
async def play(ctx, *, url : str):
  print(url)
  httpsResult = url.startswith('https')
  if (ctx.author.voice):
    voiceChannel = discord.utils.get(client.voice_clients, guild=ctx.guild)
    FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if voiceChannel == None:
      channel = ctx.message.author.voice.channel
      voice = await channel.connect()
    else:
      voice = voiceChannel
    
    async with ctx.typing():
      if httpsResult == False:
        newUrl=url.replace(' ', '+')
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+newUrl)
        videoIDs = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        thumbnail = f"https://img.youtube.com/vi/{videoIDs[0]}/maxresdefault.jpg"
        song = str("https://www.youtube.com/watch?v=" + videoIDs[0])
        print(song)
      else:
        song = url
        songID = parse_qs(urlparse(song).query)['v'][0]
        thumbnail = f'https://img.youtube.com/vi/{songID}/maxresdefault.jpg'
    
      API_KEY=os.getenv("ytKey")
      def VideoDetails():
        global views
        global title
        global likes

        if "youtube" in videoUrl:
          videoId = videoUrl[len("https://www.youtube.com/watch?v="):]
        else:
	        videoId = videoUrl

        youtube = build('youtube','v3', developerKey=API_KEY)

        videoRequest=youtube.videos().list(
	        part='snippet,statistics',
	        id=videoId
        )

        videoResponse = videoRequest.execute()

        title = videoResponse['items'][0]['snippet']['title']
        likes = videoResponse['items'][0]['statistics']['likeCount']
        views = videoResponse['items'][0]['statistics']['viewCount']
        return (likes, title, views)
    
      print(f'{title}+{views}+{likes}')
      videoUrl = song
      VideoDetails()

      try:
        video, source, hours, mins, seconds = search(song)
      except:
        await ctx.reply('Invalid Link')
        return

      embed=discord.Embed(title=f"𝙋𝙇𝘼𝙔𝙄𝙉𝙂: {title}", url=f"{song}", description="◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍", color=0xf23136)
      embed.set_author(name="Comet Music Player", icon_url="https://cometbot.emmanuelch.repl.co/static/photoToRender/playIcon.png")
      embed.set_thumbnail(url=thumbnail)
      embed.add_field(name="Likes:", value=f"{likes}", inline=True)
      embed.add_field(name="Views:", value=f"{views}", inline=True)
      embed.add_field(name="Requested by:", value=f"{ctx.author.mention}", inline=True)
      embed.add_field(name="Channel:", value=f"{ctx.message.author.voice.channel}", inline=True)
      embed.add_field(name="Length:", value=f"{hours} Hours, {mins} Minutes, {seconds} seconds", inline=True)
      embed.set_footer(text="Comet Alert")
    try:
      server = ctx.message.guild
      player = discord.FFmpegPCMAudio(source, **FFMPEG_OPTS)

      voice.play(player, after=lambda e: checkQueue1(server.id, server))
      voice.is_playing()

      players[server.id] = source
      await ctx.reply(embed=embed)
    except:
      await ctx.invoke(client.get_command('queue'), url=song)
  else:
    await ctx.send("You need to be in a voice channel to run this command")

@client.command(aliases=['ql','QueueList'])
async def queueList(ctx):
  counter = 1
  queueList ="**```"
  guild = ctx.guild
  theQueue = [queueTitles[guild.id][i:i + 3] for i in range(0, len(queueTitles[guild.id]), 3)]
  print(theQueue)

  for item in queueTitles[guild.id]:
    queueList += f"{counter}. {item}\n"
    counter += 1
  queueList += "```**"

  embed=discord.Embed(title="⛧ Ｃｕｒｒｅｎｔ Ｑｕｅｕｅ ⛧:", description=f"{queueList}", color=0x8a84e1)
  embed.set_author(name="⛆ ⚝ Ｃｏｍｅｔ Ｍｕｓｉｃ Ｐｌａｙｅｒ ⚝ ⛆")
  embed.set_footer(text="☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
  await ctx.send(embed=embed)

@client.command(aliases=['q','Queue'])
async def queue(ctx, *, url: str):
  print(url)
  httpsResult = url.startswith('https')
  if (ctx.author.voice):
    async with ctx.typing():
      if httpsResult == False:
        newUrl=url.replace(' ', '+')
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+newUrl)
        videoIDs = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        thumbnail = f"https://img.youtube.com/vi/{videoIDs[0]}/hqdefault.jpg"
        song = str("https://www.youtube.com/watch?v=" + videoIDs[0])
        print(song)
      else:
        song = url
        songID = parse_qs(urlparse(song).query)['v'][0]
        thumbnail = f'https://img.youtube.com/vi/{songID}/maxresdefault.jpg'

      API_KEY=os.getenv("ytKey")
      def VideoDetails():
        global views
        global title
        global likes

        if "youtube" in videoUrl:
          videoId = videoUrl[len("https://www.youtube.com/watch?v="):]
        else:
	        videoId = videoUrl

        youtube = build('youtube','v3', developerKey=API_KEY)

        videoRequest=youtube.videos().list(
	        part='snippet,statistics',
	        id=videoId
        )

        videoResponse = videoRequest.execute()

        title = videoResponse['items'][0]['snippet']['title']
        likes = videoResponse['items'][0]['statistics']['likeCount']
        views = videoResponse['items'][0]['statistics']['viewCount']
        return (likes, title, views)
    
      print(f'{title}+{views}+{likes}')
      videoUrl = song
      VideoDetails()

      try:
        video, source, hours, mins, seconds = search(song)
      except:
        await ctx.reply('Invalid Link')
        return
  
      embed=discord.Embed(title=f"🆀🆄🅴🆄🅴🅳: {title}", url=f"{song}", description="◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍ -- ◍", color=0xf23136)
      embed.set_author(name="Comet Music Player", icon_url="https://cometbot.emmanuelch.repl.co/static/photoToRender/playIcon.png")
      embed.set_thumbnail(url=thumbnail)
      embed.add_field(name="Likes:", value=f"{likes}", inline=True)
      embed.add_field(name="Views:", value=f"{views}", inline=True)
      embed.add_field(name="Requested by:", value=f"{ctx.author.mention}", inline=True)
      embed.add_field(name="Channel:", value=f"{ctx.message.author.voice.channel}", inline=True)
      embed.add_field(name="Length:", value=f"{hours} Hours, {mins} Minutes, {seconds} seconds", inline=True)
      embed.set_footer(text="Comet Alert")

    await ctx.reply(embed=embed)  
    
    guild = ctx.guild

    if guild.id in queues:
      queues[guild.id].append(song)
      queueTitles[guild.id].append(title)
    else:
      queues[guild.id] = []
      queues[guild.id].append(song)
      queueTitles[guild.id] = []
      queueTitles[guild.id].append(title)
  else:
    await ctx.send("You need to be in a voice channel to run this command")

@client.command(aliases=['die'])
async def leave(ctx):
  if (ctx.voice_client):
    voiceChannel = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await ctx.guild.voice_client.disconnect()
    embed=discord.Embed(title=f"Requested by {ctx.author.name}",description=f"Comet left {ctx.message.author.voice.channel}.", color=0xe29797)
    embed.set_author(name="Comet Music Player", icon_url='https://cometbot.emmanuelch.repl.co/static/photoToRender/leaveIcon.png')
    await ctx.reply(embed=embed)
  else:
    await ctx.send("Im not in a voice channel.")

@client.command(pass_context = True, aliases=['stop'])
async def pause(ctx):
  voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
  if voice.is_playing():
    embed=discord.Embed(title="Music Paused", color=0x2432ff)
    embed.set_author(name="Comet Music Player", icon_url='https://cometbot.emmanuelch.repl.co/static/photoToRender/pauseIcon.png')
    await ctx.reply(embed=embed)
    voice.pause()
  else:
    await ctx.send("No audio is playing in the voice channel at the moment!")

@client.command(pass_context = True)
async def resume(ctx): 
  voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
  if voice.is_paused():
    embed=discord.Embed(title="Music Resumed", color=0xff2600)
    embed.set_author(name="Comet Music Player", icon_url='https://cometbot.emmanuelch.repl.co/static/photoToRender/playIcon.png')
    await ctx.reply(embed=embed)
    voice.resume()
  else:
    await ctx.send("No song is paused at the moment!")

@client.command(pass_context = True)
async def skip(ctx):
  voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
  voice.stop()
  await ctx.send('Song is now skipped')

# Topic Starter Code
# Note: Some of these were added by other people
# so they may seem weird af
@client.command(aliases=['topic','topis','stopic','Topic','stoc'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def questions(ctx):
  randomquestions = ['When will you see them again?','What do you do to get rid of stress?','What is something you are obsessed with?','What three words best describe you?','What would be your perfect weekend?','What’s your favorite number? Why?','What are you going to do this weekend?','What’s the most useful thing you own?','What’s your favorite way to waste time?','What do you think of tattoos? Do you have any?',' Do you have any pets? What are their names?','What did you do last weekend?','What is something popular now that annoys you?','What did you do on your last vacation?','What’s the best / worst thing about your work/school?','If you had intro music, what song would it be? Why?','If you opened a business, what kind of business would it be?','Have you ever given a presentation in front of a large group of people? How did it go?','What is the strangest dream you have ever had?','What is a controversial opinion you have?','Who in your life brings you the most joy?',' Who had the biggest impact on the person you have become?',' What is the most annoying habit someone can have?','Where is the most beautiful place you have been?',' Where do you spend most of your free time/day?','Who was your best friend in elementary school?','How often do you stay up past 3 a.m.?','What is the worst fucking animal?','Which recent news story is the most interesting?','Where is the worst place you have been stuck for a long time?',' If you had to change your name, what would your new name be?','What is something that really annoys you but doesn’t bother most people?','What word or saying from the past do you think should come back?',' If you could learn the answer to one question about your future, what would the question be?','Has anyone ever saved your life?','What trends did you follow when you were younger?','What do you fear is hiding in the dark?','What year did you peak?? What do you think will be the best period of your entire life?','What is the silliest fear you have?','What are some things you want to accomplish before you die?','What smell brings back great memories?','What are you best at?','What makes you nervous?','What weird/useless talent do you have?','What was the best birthday wish or gift you’ve ever received?','What cartoons did you watch as a child?','What’s the funniest TV series you have seen?',' If you could bring back one TV show that was canceled, which one would you bring back?','What’s your favorite genre of movie?','Which do you prefer? The Office? Or Friends :face_vomiting:??','What’s the worst movie you have seen ','Do you like horror movies? Why or why not?','When was the last time you went to a movie theater?',' What was the last song you listened to?','Do you like classical music?','Are there any songs that always bring a tear to your eye?','Which do you prefer, popular music or relatively unknown music?','What are the three best apps on your phone?','How many apps do you have on your phone?','An app mysteriously appears on your phone that does something amazing. What does it do?', 'How often do you check your phone?','What do you wish your phone could do?','Why does anybody still buy Apple products? Why don’t more people realize Apple has what’s called “planned obsolescence”?', 'What is the most annoying thing about your phone?','How do you feel if you accidentally leave your phone at home?','Who are some of your favorite athletes?','Which sports do you like to play','What is the hardest sport to excel at?','What is the fanciest restaurant you have eaten at?','What is the worst restaurant you have ever eaten at?',' If you opened a restaurant, what kind of food would you serve?',' What is the most disgusting thing you have heard happened at a restaurant?','Where would you like to travel next?','What is the longest plane trip you have taken?','Have you traveled to any different countries? Which ones?','What is the worst hotel you have stayed at? How about the best hotel?','Will technology save the human race or destroy it?','What sci-fi movie or book would you like the future to be like?','What is your favorite shirt?','What is a fashion trend you are really glad went away?','What is/was your favorite pair of shoes?','What personal goals do you have?',' What do you like to do during summer?',' What’s the best thing to do on a cold winter day?','What is your favorite thing to eat or drink in winter?','What is your favorite holiday?','If you had to get rid of a holiday, which would you get rid of? Why?','What is your favorite type of food?','What foods do you absolutely hate?','What food looks disgusting but tastes delicious?',' If your life was a meal, what kind of meal would it be?','What would you want your last meal to be if you were on death row?', 'What is the spiciest thing you have ever eaten?',' You find a remote that can rewind, fast forward, stop, and start time. What do you do with it?','What word do you always mispronounce?','If you had a giraffe that you needed to hide, where would you hide it?','What was the scariest movie you’ve seen?','What is your stance on floorboards?','When you scream into the void, does it answer with jazz?','When the time comes, will you jump?','What is your favorite video game?','Other than anime, what is your favorite medium?','Do you ever wonder, and then you stop?','Look into my eyes. What do you see?','When the clock ends, the countdown begins.','How many people have you inadvertently killed? 0? 1? 5?',':copyright: 2021 Emmanuel.','According to all known laws of aviation,there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway, because bees don\'t care what humans think is impossible.','Try redoing the command. It did not run correctly. Were I Emmanuel, I would tell you to do it again. But for a bot, that doesn’t make much sense, I think.','Hello, learned and astonishingly attractive pupils. My name is John Green and I want to welcome you to Crash Course World History.','That would be funny, I think.','Tyklo jedno w glowie mam...',' Do YOU see Swiper?','Ayo anybody else down bad?','Devnote #19: Nobody has figured out just how many of the topic questions are literally just memes; at least, not yet.','What is your favorite shade of piss? Favorite taste?','If someone pushed you off a building, would you enjoy it?','Where is a good place to hide a deceased friend of yours? Who would you hang out with?','What celebrity has the most fashionable feet pics?','Time, Doctor Freeman? Is it really that time again?','What is the answer to the riddle of the rocks?','When I say “run”, what do you think of doing?','Giraffes are like airline food. What’s the deal with them? Do you agree?','What’s the deal with airline food?','Which is more anticipated? Jojo Season 6: Stone Ocean? Or Half-Life 3?','Deja vu! I’ve just been to this place before, higher up the beat but I know it’s my time to go-o!','Get your credit card, if you wanna see me','Who is your favorite Tom Brady?','Have you watched “The Burdening of Will Montgomery”?','Who made the sky? Was it me?','You may consume three beans, but no more. They will know if you consume more.','They surpass me, for I cannot tessellate.','Did you change your diaper today?','Do you fucking want me to go back to how I used to be? How you take fucking advantage of how nice I am now?','Why are you so lazy?','When will you decide to get off your ass for once?','How often do you use reddit?','Who is your crush?','Do you have a brother named Alec?','Do you have a sister named Juliana?','Who has the largest cock?','Do women exist? Do birds?','Why are so many of these questions so worthless?', 'In your opinion, how much faster should the server completely descend into sarcasm?', 'There’s no message to snipe buddy.', '^', 'Who has touched you the most? Physically? Metaphysically?','What do you do with it?', 'Who will win the race?','Who really gets you going?', 'Isn\’t it usually noon by now?', 'Where are your parents?', 'Today I will affect the trout population.','Today I will drive the trout population extinct.', 'Today I will leave the trout population unchanged.', 'All we had to do was follow the damn train, <@438154309872386068>', 'Did you know? Garen\’s real name is Jetsiky. Allegedly.', 'What word or phrase, like “causality” or “vernacular” or “in any case” do you try to use in more sentences than you probably should?', 'Dev Note#2: The creator is too lazy to add sex bot.', 'Dev note #4: guacamole ___ penis', 'Guys Ik Char\’s crush. It\’s: ____', 'Dev Note #3: I don’t care what any of them say. The N-Word will never be funny.',  'Isn’t it usually noon by now?', 'My favorites are green and purple strictly non-convex polyhedra. What about you?', 'My email is emmanuel@aol.com. Dont judge, it\’s from 2003.', 'What are the worst fanbases?', 'Y’know how some days you just feel baggier than a nutsack?', 'What did you want to be when you grew up when you were 5? How about when you were 6? 7? 8? 9? 10? 11? What made you change your plans so often?', 'What were your parents doing during 9/11?', 'Where do you see yourself in 24 hours?', 'If you could choose only one type of boots to wear for the rest of your life, why would it be Uggs?', 'What combination of Nike shoes and socks do you most frequently wear between the months of December and April?', 'How old is your sister?', 'By any chance, do you know of any elementary schools within 500 meters?', 'Where is your family now?', 'In your time of need, where was everybody?', 'How will you be judged?', 'Where is your solace?', 'Excuse my ignorance, but what exactly is moss?', 'Object, dost thou observe time in the past or present?', 'When comes after this? What discord server will be next?', 'yo\’re*', 'Marlon was here', 'Who is your least favorite person?', 'What part of a kid’s movie completely scarred you?', 'Toilet paper, over or under?', 'Toilet paper, over or under?','Where is the weirdest place you\’ve ever shat in?', 'I drink to forget.', 'Hey baby, come back to my place and I\’ll show you ______', '______ really gets me going', 'May the ______ be with you.', 'MAGA! Just kidding, I\’m not a cultist.','Should we normalize watching adult content with our parents?', 'You guys really need to find your own things to talk about, but I\’ll help you get started. What the fuck is cheese?','No topic could be generated. Please try again!', 'The G-Man provides a Xen sample. What do you do?', 'Mention the person with the least friends.', 'I\’m not like other girls!']
  await ctx.channel.send(f'{random.choice(randomquestions)}')

@client.command(aliases=['gareb', 'garen',])
@commands.cooldown(1, 10, commands.BucketType.user)
async def garebmomen(ctx):
  garebgif = ['https://giphy.com/gifs/moment-garen-6mUigoKNZskgyYpzjw','https://tenor.com/view/cat-spin-gif-19628827', 'https://tenor.com/view/deffi-pegou-garen-demacia-twirling-spinning-fujiwara-gif-17776151']
  await ctx.channel.send(f'{random.choice(garebgif)}')

@client.command(aliases=['E man', 'Eman','Emmanuel','emmanuel'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def eman(ctx):
  randomEman = ['https://giphy.com/gifs/gay-emmanuel-L8haSJadlzRrT5UP92',
    'https://tenor.com/view/emmanuel-zavala-cod-pp-small-cod-heck-fuck-bitch-gif-20893989',
    'https://tenor.com/view/discord-emanuel-emmanuel-baseball-champ-gif-20154485']
  await ctx.channel.send(f'{random.choice(randomEman)}')

@client.command(aliases=['user-info'],pass_context=True)
async def userinfo(ctx, *, user: discord.Member=None):
    if user == None:
      user = ctx.author
    date_format = "%a, %d %b %Y %I:%M %p"
    print(user.joined_at.strftime(date_format))
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)

@client.command(aliases=['say'], help='TTS Command')
async def tts(ctx, *, text=None):
  # USE GOOGLETRANS V 3.1.0a0
  # To install it use pip3 install googletrans==3.1.0a0
  # Poetry doesn't have 3.1.0a0 if you use Replit

  if not text:
    # We have nothing to speak
    await ctx.send(f"Hey {ctx.author.mention}, I need to know what to say please.")
    return
  async with ctx.typing():
    embed=discord.Embed(title="Comet TTS Options", description="Click one of the buttons in this message to choose a language. You have 5 seconds before it defaults to english.",color=0x2f3136)
    embed.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/ttsIcon.png")
    embed1 = await ctx.send(embed=embed,
      components = [
        [
          Button(style = ButtonStyle.blue, label = "English (en)"),
          Button(style = ButtonStyle.blue, label = "Spanish (es)"),
          Button(style = ButtonStyle.red, label = "Armenian (hy)"),
          Button(style = ButtonStyle.red, label = "Korean (ko)"),
          Button(style = ButtonStyle.green, label = "Tagalog (Filipino) (tl)")
        ],
        [
          Button(style = ButtonStyle.green, label = "Russian (ru)"),
          Button(style = ButtonStyle.red, label = "Chinese (Mandarin/Taiwan) (zh-TW)"),
          Button(style = ButtonStyle.blue, label = "German (de)"),
          Button(style = ButtonStyle.blue, label = "French (fr)")
        ]
      ])

    def check(buttonCheck):
      return buttonCheck.channel == ctx.channel

    try:
      buttonCheck = await client.wait_for("button_click", timeout=5, check=check)

      await buttonCheck.respond(content = f'{buttonCheck.component.label} Selected')
      if buttonCheck.component.label == 'Spanish (es)':
        translator = Translator()
        result = translator.translate(text, dest='es')
        print(result.text)
        language = 'es'
        tts = gTTS(text=result.text, lang=language)
        language = 'Spanish'
      elif buttonCheck.component.label == 'Armenian (hy)':
        translator = Translator()
        result = translator.translate(text, dest='hy')
        language = 'hy'
        tts = gTTS(text=result.text, lang=language)
        language = 'Armenian'
      elif buttonCheck.component.label == 'English (en)':
        translator = Translator()
        result = translator.translate(text, dest='en')
        language = 'en'
        tts = gTTS(text=result.text, lang=language)
        language = 'English'
      elif buttonCheck.component.label == 'Korean (ko)':
        translator = Translator()
        result = translator.translate(text, dest='ko')
        language = 'ko'
        tts = gTTS(text=result.text, lang=language)
        language = 'Korean'
      elif buttonCheck.component.label == 'Tagalog (Filipino) (tl)':
        translator = Translator()
        result = translator.translate(text, dest='tl')
        language = 'tl'
        tts = gTTS(text=result.text, lang=language)
        language = 'Tagalog (Filipino)'
      elif buttonCheck.component.label == 'Russian (ru)':
        translator = Translator()
        result = translator.translate(text, dest='ru')
        language = 'ru'
        tts = gTTS(text=result.text, lang=language)
        language = 'Russian'
      elif buttonCheck.component.label == 'Chinese (Mandarin/Taiwan) (zh-TW)':
        translator = Translator()
        result = translator.translate(text, dest='zh-TW')
        language = 'Chinese (Mandarin/Taiwan)'
        tts = gTTS(text=result.text, lang='zh-TW')
      elif buttonCheck.component.label == 'German (de)':
        translator = Translator()
        result = translator.translate(text, dest='de')
        language = 'de'
        tts = gTTS(text=result.text, lang=language)
        language = 'German'
      elif buttonCheck.component.label == 'French (fr)':
        translator = Translator()
        result = translator.translate(text, dest='fr')
        language = 'fr'
        tts = gTTS(text=result.text, lang=language)
        language = 'French'
      else:
        await ctx.send('Defaulted to English')
        tts = gTTS(text=text, lang='en')
        language = 'English'
      
    except asyncio.TimeoutError:
      await ctx.send('Defaulted to English')
      tts = gTTS(text=text, lang='en')
      language = 'English'
    
    voiceChannel = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voiceChannel == None:
      channel = ctx.message.author.voice.channel
      voice = await channel.connect()
    else:
      uselessVariable = 1
    
    tts.save("text.mp3")
    with audioread.audio_open('text.mp3') as f:
      totalsec = f.duration
      hours, mins, seconds = howLong(int(totalsec))
    
    embed2=discord.Embed(title="TTS Notification",description="Successfully set up.", color=0x2f3136)
    embed2.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/ttsIcon.png")
    try:
      embed2.add_field(name="Text:", value=f"{result.text}", inline=True)
    except:
      embed2.add_field(name="Text:", value=f"{text}", inline=True)
    embed2.add_field(name="Language:", value=f"```{language}```",inline=False)
    embed2.add_field(name="Duration:", value=f"```{hours} Hours: {mins} Minutes: {seconds} Seconds```", inline=False)
    
  await embed1.edit(embed=embed2, components=[
    [
      Button(style = ButtonStyle.blue, label = "☁  ☁  ☀  ☁ Done  ☁  ☁  ☁  ☁  ☁", disabled=True),
      Button(style = ButtonStyle.blue, label = "☁  ☁  ☁  ☁  ☁  ☁  ☁  ☁", disabled=True)
    ]
  ])
    
  try:
    guild = ctx.message.guild
    player = voice.play(discord.FFmpegPCMAudio("text.mp3"))
    counter = 0

    players[guild.id] = player
    while counter <= totalsec:
      await asyncio.sleep(1)
      counter += 1
    await voice.disconnect()

  except TypeError as e:
    await ctx.send(f"TypeError exception:\n`{e}`")

@client.command(help="Play with #rps")
async def rps(ctx):
  rpsGame = ['rock', 'paper', 'scissors']

async def openWarnUser(member, server):
  with open('warns.json', 'r') as warnings:
    warns = json.load(warnings)
  
  if str(server.id) in warns:
    if str(member.id) in warns[str(server.id)]:
      return False
    else:
      warns[str(server.id)][str(member.id)] = {}
      warns[str(server.id)][str(member.id)]["Warning Count"] = 0
      warns[str(server.id)][str(member.id)]["Reason"] = []
  else:
    warns[str(server.id)] = {}
    warns[str(server.id)][str(member.id)] = {}
    warns[str(server.id)][str(member.id)]["Warning Count"] = 0
    warns[str(server.id)][str(member.id)]["Reason"] = []

  with open('warns.json','w') as warnings:
    json.dump(warns, warnings)
  return True

async def openSetupAccount(server):
  with open('setup.json', 'r') as setup:
    setting = json.load(setup)
  
  if str(server.id) in setting:
    return False
  else:
    setting[str(server.id)] = {}
    setting[str(server.id)]["Admin Role"] = ''
    setting[str(server.id)]["Role 1"] = ''
    setting[str(server.id)]["Role 2"] = ''
    setting[str(server.id)]["Role 1 Warns"] = 3
    setting[str(server.id)]["Role 2 Warns"] = 6
    setting[str(server.id)]["Admin Role Warns"] = 3
    setting[str(server.id)]["Receive Bot Notifications"] = 'False'
    setting[str(server.id)]["Notification Channel"] = 0

  with open('setup.json','w') as setup:
    json.dump(setting, setup)
  return True

@client.command(aliases=['sU','Setup'])
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(administrator=True)
async def setup(ctx, *, setupOption: str='warning'):
  await openSetupAccount(ctx.guild)
  if setupOption == 'notif' or setupOption == 'notification' or setupOption == 'n':
    await ctx.reply('𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐂𝐨𝐦𝐞𝐭 𝐍𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐒𝐞𝐭𝐮𝐩. 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐮𝐬𝐞𝐝 𝐭𝐨 𝐬𝐞𝐭 𝐮𝐩 𝐛𝐨𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬 𝐢𝐧 𝐚 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐨𝐟 𝐭𝐡𝐢𝐬 𝐬𝐞𝐫𝐯𝐞𝐫. 𝐌𝐚𝐤𝐞 𝐬𝐮𝐫𝐞 𝐭𝐨 𝐡𝐚𝐯𝐞 𝐭𝐡𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐈𝐃 𝐨𝐟 𝐭𝐡𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐲𝐨𝐮 𝐚𝐫𝐞 𝐠𝐨𝐢𝐧𝐠 𝐭𝐨 𝐮𝐬𝐞 𝐟𝐨𝐫 𝐛𝐨𝐭 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬 𝐨𝐧 𝐡𝐚𝐧𝐝 𝐭𝐨 𝐦𝐚𝐤𝐞 𝐭𝐡𝐢𝐬 𝐩𝐫𝐨𝐜𝐞𝐬𝐬 𝐟𝐚𝐬𝐭𝐞𝐫.')

    await ctx.reply('𝐄𝐧𝐭𝐞𝐫 𝐭𝐡𝐞 𝐈𝐃 𝐨𝐟 𝐭𝐡𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐰𝐞𝐫𝐞 𝐂𝐨𝐦𝐞𝐭 𝐰𝐢𝐥𝐥 𝐬𝐞𝐧𝐝 𝐧𝐨𝐭𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧𝐬 𝐭𝐨:')
    try:
      purpose = await client.wait_for("message", check=check, timeout=30)
      await purpose.add_reaction('✅')
      adminRole = purpose.content
    except asyncio.TimeoutError:
      await ctx.send("𝙎𝙚𝙩𝙪𝙥 𝙩𝙞𝙢𝙚𝙙 𝙤𝙪𝙩. 𝙉𝙤 𝙘𝙝𝙖𝙣𝙜𝙚𝙨 𝙬𝙚𝙧𝙚 𝙨𝙖𝙫𝙚𝙙.")
      return
    pass
  if setupOption == 'warning':
    adminRole = ''
    role1 = ''
    role2 = ''
    adminWarn = 3
    role1Warn = 3
    role2Warn = 6
    
    with open('setup.json', 'r') as settings:
      serverSetup = json.load(settings)
    
    def check(purpose):
      return purpose.author == ctx.author and purpose.channel == ctx.channel
    
    await ctx.send('𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙩𝙝𝙚 𝘾𝙊𝙈𝙀𝙏 𝙒𝙖𝙧𝙣𝙞𝙣𝙜 𝙎𝙮𝙨𝙩𝙚𝙢 𝙎𝙚𝙩𝙪𝙥. 𝙔𝙊𝙐 𝙈𝙐𝙎𝙏 𝙞𝙣𝙥𝙪𝙩 𝙩𝙝𝙚 𝘼𝙙𝙢𝙞𝙣 𝙧𝙤𝙡𝙚 𝙣𝙖𝙢𝙚 𝙙𝙪𝙚 𝙩𝙤 𝙩𝙝𝙚 𝙛𝙖𝙘𝙩 𝙩𝙝𝙖𝙩 𝘾𝙤𝙢𝙚𝙩 𝙥𝙞𝙣𝙜𝙨 𝙩𝙝𝙚 𝙧𝙤𝙡𝙚 𝙬𝙝𝙚𝙣 𝙖 𝙪𝙨𝙚𝙧 𝙝𝙖𝙨 𝙜𝙖𝙩𝙝𝙚𝙧𝙚𝙙 𝙚𝙣𝙤𝙪𝙜𝙝 𝙬𝙖𝙧𝙣𝙞𝙣𝙜𝙨.\n\n𝙄𝙛 𝙮𝙤𝙪 𝙖𝙧𝙚 𝙤𝙣𝙡𝙮 𝙜𝙤𝙞𝙣𝙜 𝙩𝙤 𝙗𝙚 𝙪𝙨𝙞𝙣𝙜 𝙤𝙣𝙚 𝙧𝙤𝙡𝙚, 𝙞𝙣𝙥𝙪𝙩 𝙩𝙝𝙖𝙩 𝙧𝙤𝙡𝙚 𝙖𝙨 𝙢𝙖𝙣𝙮 𝙩𝙞𝙢𝙚𝙨 𝙖𝙨 𝙞𝙩\'𝙨 𝙣𝙚𝙘𝙚𝙨𝙨𝙖𝙧𝙮 𝙬𝙝𝙚𝙣 𝙮𝙤𝙪 𝙜𝙚𝙩 𝙖𝙨𝙠𝙚𝙙 𝙩𝙤 𝙞𝙣𝙥𝙪𝙩 𝙖 𝙧𝙤𝙡𝙚. 𝙏𝙝𝙚 𝙨𝙖𝙢𝙚 𝙖𝙥𝙥𝙡𝙞𝙚𝙨 𝙛𝙤𝙧 𝙩𝙝𝙚 𝙬𝙖𝙧𝙣𝙞𝙣𝙜 𝙩𝙝𝙧𝙚𝙨𝙝𝙤𝙡𝙙.\n𝘼𝙡𝙨𝙤 𝙣𝙤𝙩𝙚 𝙩𝙝𝙖𝙩 𝙞𝙛 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙤𝙣𝙚 𝙧𝙤𝙡𝙚 𝙩𝙤 𝙝𝙖𝙫𝙚 𝙖 𝙝𝙞𝙜𝙝𝙚𝙧 𝙬𝙖𝙧𝙣 𝙩𝙝𝙧𝙚𝙨𝙝𝙤𝙡𝙙 𝙩𝙝𝙖𝙣 𝙖𝙣𝙤𝙩𝙝𝙚𝙧, 𝙮𝙤𝙪 𝙣𝙚𝙚𝙙 𝙩𝙤 𝙞𝙣𝙥𝙪𝙩 𝙩𝙝𝙖𝙩 𝙧𝙤𝙡𝙚 𝙁𝙄𝙍𝙎𝙏 𝙩𝙤 𝙥𝙧𝙚𝙫𝙚𝙣𝙩 𝙞𝙨𝙨𝙪𝙚𝙨. 𝙏𝙝𝙞𝙨 𝙙𝙤𝙚𝙨 𝙣𝙤𝙩 𝙖𝙥𝙥𝙡𝙮 𝙩𝙤 𝙩𝙝𝙚 𝙖𝙙𝙢𝙞𝙣 𝙧𝙤𝙡𝙚.')

    await ctx.reply('⋙ 𝙏𝙮𝙥𝙚 𝙩𝙝𝙚 𝙖𝙙𝙢𝙞𝙣 𝙧𝙤𝙡𝙚 𝙖𝙣𝙙 𝙩𝙮𝙥𝙚 𝙩𝙝𝙚 𝙬𝙖𝙧𝙣𝙞𝙣𝙜𝙨 𝙛𝙤𝙧 𝙩𝙝𝙖𝙩 𝙧𝙤𝙡𝙚.⋘')
    try:
      purpose = await client.wait_for("message", check=check, timeout=30)
      await purpose.add_reaction('✅')
      adminRole = purpose.content
    except asyncio.TimeoutError:
      await ctx.send("𝙎𝙚𝙩𝙪𝙥 𝙩𝙞𝙢𝙚𝙙 𝙤𝙪𝙩. 𝙉𝙤 𝙘𝙝𝙖𝙣𝙜𝙚𝙨 𝙬𝙚𝙧𝙚 𝙨𝙖𝙫𝙚𝙙.")
      return
    
    await ctx.reply('⋙ 𝙉𝙤𝙬 𝙩𝙮𝙥𝙚 𝙩𝙝𝙚 𝙛𝙞𝙧𝙨𝙩 𝙧𝙤𝙡𝙚 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙩𝙤 𝙖𝙙𝙙 𝙖 𝙨𝙥𝙚𝙘𝙞𝙖𝙡 𝙬𝙖𝙧𝙣𝙞𝙣𝙜 𝙘𝙤𝙪𝙣𝙩 𝙛𝙤𝙧. ⋘')
    try:
      purpose = await client.wait_for("message", check=check, timeout=30)
      await purpose.add_reaction('✅')
      role1 = purpose.content
    except asyncio.TimeoutError:
      await ctx.send("𝙎𝙚𝙩𝙪𝙥 𝙩𝙞𝙢𝙚𝙙 𝙤𝙪𝙩. 𝙉𝙤 𝙘𝙝𝙖𝙣𝙜𝙚𝙨 𝙬𝙚𝙧𝙚 𝙨𝙖𝙫𝙚𝙙.")
      return
    
    await ctx.reply('⋙ 𝙉𝙤𝙬 𝙩𝙮𝙥𝙚 𝙩𝙝𝙚 𝙨𝙚𝙘𝙤𝙣𝙙 𝙧𝙤𝙡𝙚 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙩𝙤 𝙖𝙙𝙙 𝙖 𝙨𝙥𝙚𝙘𝙞𝙖𝙡 𝙬𝙖𝙧𝙣𝙞𝙣𝙜 𝙘𝙤𝙪𝙣𝙩 𝙛𝙤𝙧. ⋘\n⋙  ⋘')
    try:
      purpose = await client.wait_for("message", check=check, timeout=30)
      await purpose.add_reaction('✅')
      role2 = purpose.content
    except asyncio.TimeoutError:
      await ctx.send("𝙎𝙚𝙩𝙪𝙥 𝙩𝙞𝙢𝙚𝙙 𝙤𝙪𝙩. 𝙉𝙤 𝙘𝙝𝙖𝙣𝙜𝙚𝙨 𝙬𝙚𝙧𝙚 𝙨𝙖𝙫𝙚𝙙.")
      return
    
    await ctx.reply('⋙ 𝙁𝙞𝙣𝙖𝙡𝙡𝙮 𝙞𝙣𝙥𝙪𝙩 𝙩𝙝𝙚 𝙬𝙖𝙧𝙣𝙞𝙣𝙜 𝙩𝙝𝙧𝙚𝙨𝙝𝙤𝙡𝙙𝙨 𝙛𝙤𝙧 𝙖𝙡𝙡 𝙩𝙝𝙧𝙚𝙚 𝙧𝙤𝙡𝙚𝙨. 𝘿𝙤 𝙞𝙩 𝙞𝙣 𝙩𝙝𝙚 𝙛𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜 𝙛𝙤𝙧𝙢𝙖𝙩 (𝙬/𝙤 𝙩𝙝𝙚 𝙥𝙖𝙧𝙚𝙣𝙩𝙝𝙚𝙨𝙚𝙨 𝙤𝙗𝙫𝙞𝙤𝙪𝙨𝙡𝙮): (𝙖𝙙𝙢𝙞𝙣 𝙧𝙤𝙡𝙚\'𝙨 𝙩𝙝𝙧𝙚𝙨𝙝𝙤𝙡𝙙) (𝙧𝙤𝙡𝙚 1\'𝙨 𝙩𝙝𝙧𝙚𝙨𝙝𝙤𝙡𝙙) (𝙧𝙤𝙡𝙚 2\'𝙨 𝙩𝙝𝙧𝙚𝙨𝙝𝙤𝙡𝙙) ⋘')
    try:
      purpose = await client.wait_for("message", check=check, timeout=30)
      await purpose.add_reaction('✅')
      prepareThresholds = purpose.content.split()
      adminWarn = int(prepareThresholds[0])
      role1Warn = int(prepareThresholds[1])
      role2Warn = int(prepareThresholds[2])
    except asyncio.TimeoutError:
      await ctx.send("𝙎𝙚𝙩𝙪𝙥 𝙩𝙞𝙢𝙚𝙙 𝙤𝙪𝙩. 𝙉𝙤 𝙘𝙝𝙖𝙣𝙜𝙚𝙨 𝙬𝙚𝙧𝙚 𝙨𝙖𝙫𝙚𝙙.")
      return

    serverSetup[str(ctx.guild.id)]["Role 1"] = role1
    serverSetup[str(ctx.guild.id)]["Role 2"] = role2
    serverSetup[str(ctx.guild.id)]["Admin Role"] = adminRole
    serverSetup[str(ctx.guild.id)]["Role 1 Warns"] = role1Warn
    serverSetup[str(ctx.guild.id)]["Role 2 Warns"] = role2Warn
    serverSetup[str(ctx.guild.id)]["Admin Role Warns"] = adminWarn
    with open('setup.json', 'w') as s:
      json.dump(serverSetup, s)
    
    await ctx.reply(f'𝙎𝙚𝙩𝙪𝙥 𝙛𝙤𝙧 {ctx.guild.name} 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙘𝙤𝙢𝙥𝙡𝙚𝙩𝙚𝙙. 𝙏𝙝𝙚 𝙖𝙙𝙢𝙞𝙣 𝙧𝙤𝙡𝙚 𝙞𝙨 ***{serverSetup[str(ctx.guild.id)]["Admin Role"]}*** 𝙬𝙞𝙩𝙝 𝙖 ***{serverSetup[str(ctx.guild.id)]["Admin Role Warns"]}*** 𝙬𝙖𝙧𝙣𝙞𝙣𝙜 𝙩𝙝𝙧𝙚𝙨𝙝𝙤𝙡𝙙, 𝙩𝙝𝙚 𝙛𝙞𝙧𝙨𝙩 𝙧𝙤𝙡𝙚 𝙞𝙨 {serverSetup[str(ctx.guild.id)]["Role 1"]} 𝙬𝙞𝙩𝙝 𝙖 ***{serverSetup[str(ctx.guild.id)]["Role 1 Warns"]}*** 𝙬𝙖𝙧𝙣𝙞𝙣𝙜 𝙩𝙝𝙧𝙚𝙨𝙝𝙤𝙡𝙙, 𝙖𝙣𝙙 𝙛𝙞𝙣𝙖𝙡𝙡𝙮 𝙧𝙤𝙡𝙚 𝙩𝙬𝙤 𝙞𝙨 {serverSetup[str(ctx.guild.id)]["Role 2 Warns"]} 𝙬𝙞𝙩𝙝 𝙖 ***{serverSetup[str(ctx.guild.id)]["Role 2 Warns"]}*** 𝙬𝙖𝙧𝙣𝙞𝙣𝙜 𝙩𝙝𝙧𝙚𝙨𝙝𝙤𝙡𝙙. 𝙏𝙝𝙖𝙣𝙠 𝙮𝙤𝙪 𝙛𝙤𝙧 𝙪𝙨𝙞𝙣𝙜 𝙘𝙤𝙢𝙚𝙩 𝙖𝙨 𝙛𝙤𝙧 𝙮𝙤𝙪𝙧 𝙢𝙤𝙙𝙚𝙧𝙖𝙩𝙞𝙤𝙣 𝙣𝙚𝙚𝙙𝙨!')
  

@client.command(aliases=['Warn'])
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(kick_members=True, administrator=True)
async def warn(ctx, member: discord.Member, *, reason=None):
  with open('setup.json', 'r') as settings:
    serverSetup = json.load(settings)
  
  if member == None:
    member = ctx.author
  await openWarnUser(member, ctx.guild)
  
  if member.id == ctx.author.id:
    embed=discord.Embed(title="⛧ 𝙔𝙤𝙪 𝙘𝙖𝙣'𝙩 𝙪𝙨𝙚 𝙞𝙩 𝙤𝙣 𝙮𝙤𝙪𝙧𝙨𝙚𝙡𝙛 ⛧", color=0xff1414)
    embed.set_author(name="⛆ 𝘾𝙤𝙢𝙚𝙩 ⚝ 𝙒𝙖𝙧𝙣𝙞𝙣𝙜 𝙎𝙮𝙨𝙩𝙚𝙢 ⚝ ⛆")
    await ctx.send(embed=embed)
    return
  
  with open('warns.json', 'r') as warnings:
    warns = json.load(warnings)
  
  dateToAdd = datetime.today().strftime('%m/%d/%Y')
  reasonToAdd = f'{reason} | {dateToAdd}'
  warns[str(ctx.guild.id)][str(member.id)]["Warning Count"] += 1
  warns[str(ctx.guild.id)][str(member.id)]["Reason"].append(str(reasonToAdd))

  with open('warns.json','w') as warnings:
    json.dump(warns, warnings)
  
  timesWarned = int(warns[str(ctx.guild.id)][str(member.id)]["Warning Count"])

  if str(ctx.guild.id) in serverSetup:
    adminRole = discord.utils.get(ctx.guild.roles, name=serverSetup[str(ctx.guild.id)]["Admin Role"])
    role1 = discord.utils.get(ctx.guild.roles, name=serverSetup[str(ctx.guild.id)]["Role 1"])
    role2 = discord.utils.get(ctx.guild.roles, name=serverSetup[str(ctx.guild.id)]["Role 2"])
    adminWarn = serverSetup[str(ctx.guild.id)]["Admin Role Warns"]
    role1Warn = serverSetup[str(ctx.guild.id)]["Role 1 Warns"]
    role2Warn = serverSetup[str(ctx.guild.id)]["Role 2 Warns"]

    for role in member.roles:
      if role == adminRole and timesWarned > adminWarn:
        await ctx.send(f'𝙎𝙤𝙧𝙧𝙮 𝙩𝙤 𝙗𝙤𝙩𝙝𝙚𝙧 𝙮𝙤𝙪 {adminRole.mention}, 𝙗𝙪𝙩 𝙖 𝙢𝙚𝙢𝙗𝙚𝙧 ***({member.mention})*** 𝙝𝙖𝙨 𝙜𝙖𝙩𝙝𝙚𝙧𝙚𝙙 𝙚𝙣𝙤𝙪𝙜𝙝 𝙬𝙖𝙧𝙣𝙨 𝙩𝙤 𝙜𝙚𝙩 𝙩𝙝𝙚𝙞𝙧 𝙢𝙤𝙙𝙚𝙧𝙖𝙩𝙤𝙧/𝙖𝙙𝙢𝙞𝙣 𝙨𝙩𝙖𝙩𝙪𝙨 𝙧𝙚𝙢𝙤𝙫𝙚𝙙. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙙𝙞𝙨𝙘𝙪𝙨𝙨 𝙩𝙝𝙞𝙨 𝙩𝙤 𝙛𝙞𝙜𝙪𝙧𝙚 𝙤𝙪𝙩 𝙬𝙝𝙖𝙩 𝙩𝙤 𝙙𝙤.')
        break
      if role == role1 and timesWarned > role1Warn:
        await ctx.send(f'𝙎𝙤𝙧𝙧𝙮 𝙩𝙤 𝙗𝙤𝙩𝙝𝙚𝙧 𝙮𝙤𝙪  {adminRole.mention}, 𝙗𝙪𝙩 𝙖 𝙢𝙚𝙢𝙗𝙚𝙧 ({member.mention}) 𝙝𝙖𝙨 𝙚𝙣𝙤𝙪𝙜𝙝 𝙬𝙖𝙧𝙣𝙨 𝙩𝙤 𝙜𝙚𝙩 𝙠𝙞𝙘𝙠𝙚𝙙/𝙗𝙖𝙣𝙣𝙚𝙙 𝙛𝙧𝙤𝙢 {ctx.guild.name}.')
        break
      if role == role2 and timesWarned > role2Warn:
        await ctx.send(f'Sorry to bother you {adminRole.mention}, but a member ({member.mention}) has enough warns to get kicked/banned from {ctx.guild.name}.')
        break
  else:
    await ctx.reply('⚝ __𝙒𝘼𝙍𝙉𝙄𝙉𝙂__ ⚝: 𝙋𝙡𝙚𝙖𝙨𝙚 𝙘𝙤𝙢𝙥𝙡𝙚𝙩𝙚 𝙩𝙝𝙚 𝙒𝘼𝙍𝙉𝙄𝙉𝙂 𝙎𝙔𝙎𝙏𝙀𝙈 𝙎𝙚𝙩𝙪𝙥 𝙖𝙨 𝙨𝙤𝙤𝙣 𝙖𝙨 𝙥𝙤𝙨𝙨𝙞𝙗𝙡𝙚! 𝙔𝙤𝙪 𝙘𝙖𝙣 𝙙𝙤 𝙩𝙝𝙞𝙨 𝙗𝙮 𝙧𝙪𝙣𝙣𝙞𝙣𝙜 `#𝙨𝙚𝙩𝙪𝙥`.')
  
  embed=discord.Embed(title=f"☾ {ctx.guild.name} ☽", description="/ / / / / / / / / / / **__Warned__** / / / / / / / / / / / / / / /", color=0x009dff)
  embed.set_author(name="⛆ 𝘾𝙤𝙢𝙚𝙩 ⚝ 𝙒𝙖𝙧𝙣𝙞𝙣𝙜 𝙎𝙮𝙨𝙩𝙚𝙢 ⚝ ⛆")
  embed.set_thumbnail(url=member.avatar_url)
  embed.add_field(name="Warned User:", value=member.mention, inline=True)
  embed.add_field(name="Moderator:", value=ctx.author.mention, inline=True)
  embed.add_field(name="Reason:", value=reason, inline=False)
  embed.set_footer(text="☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄")
  await ctx.reply(embed=embed)
  await member.send(embed=embed)

def substringInList(listToScan, substring):
  for i, s in enumerate(listToScan):
    if substring in s:
      return i
  return -1

@client.command(aliases=['un','Unwarn','UnWarn'])
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(kick_members=True, administrator=True)
async def unwarn(ctx, member: discord.Member, *, reason='None'):
  if member == None:
    member = ctx.author
  
  if member.id == ctx.author.id:
    embed=discord.Embed(title="⛧ 𝙔𝙤𝙪 𝙘𝙖𝙣'𝙩 𝙪𝙨𝙚 𝙞𝙩 𝙤𝙣 𝙮𝙤𝙪𝙧𝙨𝙚𝙡𝙛 ⛧", color=0xff1414)
    embed.set_author(name="⛆ 𝘾𝙤𝙢𝙚𝙩 ⚝ 𝙒𝙖𝙧𝙣𝙞𝙣𝙜 𝙎𝙮𝙨𝙩𝙚𝙢 ⚝ ⛆")
    await ctx.send(embed=embed)
    return
  
  await openWarnUser(member, ctx.guild)
  with open('warns.json', 'r') as warnings:
    warns = json.load(warnings)
  
  oldestWarning = substringInList(warns[str(ctx.guild.id)][str(member.id)]["Reason"], reason)

  warns[str(ctx.guild.id)][str(member.id)]["Warning Count"] -= 1
  del warns[str(ctx.guild.id)][str(member.id)]["Reason"][int(oldestWarning)]

  with open('warns.json','w') as warnings:
    json.dump(warns, warnings)
  
  embed=discord.Embed(title=f"☾ {ctx.guild.name} ☽", description="/ / / / / / / / / / **__Unwarned__** / / / / / / / / / / / / / / /", color=0x009dff)
  embed.set_author(name="⛆ 𝘾𝙤𝙢𝙚𝙩 ⚝ 𝙒𝙖𝙧𝙣𝙞𝙣𝙜 𝙎𝙮𝙨𝙩𝙚𝙢 ⚝ ⛆")
  embed.set_thumbnail(url=member.avatar_url)
  embed.add_field(name="Unwarned User:", value=member.mention, inline=True)
  embed.add_field(name="Moderator:", value=ctx.author.mention, inline=True)
  embed.set_footer(text="☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄")
  await ctx.reply(embed=embed)
  await member.send(embed=embed)

@client.command(aliases=['iw','Infractions','warnsFor'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def infractions(ctx, member: discord.Member=None, *, reason=None):
  if member == None:
    member = ctx.author
  
  await openWarnUser(member, ctx.guild)
  with open('warns.json', 'r') as warnings:
    warns = json.load(warnings)
  warnList = '**``'
  
  warnCount = warns[str(ctx.guild.id)][str(member.id)]["Warning Count"]
  warnings = warns[str(ctx.guild.id)][str(member.id)]["Reason"]

  for warn in warnings:
    warnList += f'{warn} \n'
  warnList += '``**'

  embed=discord.Embed(title=f"☾ {ctx.guild.name} ☽", description=f"/ / / / / / / / / / / / **__Infractions__** / / / / / / / / / / /\n𝙒𝙖𝙧𝙣𝙞𝙣𝙜 𝘾𝙤𝙪𝙣𝙩: *__{warnCount}__*\n\n▷ ▷ ▷ ▷ ▷ ▷ ▷ __𝙒𝙖𝙧𝙣𝙞𝙣𝙜 𝙇𝙞𝙨𝙩__ ▷ ▷ ▷ ▷ ▷ ▷ ▷\n{warnList}", color=0x009dff)
  embed.set_author(name="⛆ 𝘾𝙤𝙢𝙚𝙩 ⚝ 𝙒𝙖𝙧𝙣𝙞𝙣𝙜 𝙎𝙮𝙨𝙩𝙚𝙢 ⚝ ⛆")
  embed.set_thumbnail(url=member.avatar_url)
  embed.add_field(name="User:", value=member.mention, inline=True)
  embed.set_footer(text="☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄ ☄")
  await ctx.reply(embed=embed)

def wikipediaSummary(arg):
  result = wikipedia.summary(arg, sentences=6, chars=1000, auto_suggest=True, redirect=True)
  return result

@client.command(pass_context=True)
async def wikisearch(ctx, *, search):
  try:
    result = wikipediaSummary(search)
    title = wikipedia.suggest(search)
  except wikipedia.exceptions.DisambiguationError:
    await ctx.reply('𝙎𝙚𝙖𝙧𝙘𝙝 𝙧𝙚𝙨𝙪𝙡𝙩𝙨 𝙞𝙣 𝙢𝙪𝙡𝙩𝙞𝙥𝙡𝙚 𝙧𝙚𝙨𝙪𝙡𝙩𝙨. 𝙏𝙧𝙮 𝙗𝙚𝙞𝙣𝙜 𝙢𝙤𝙧𝙚 𝙨𝙥𝙚𝙘𝙞𝙛𝙞𝙘...')
    return
  except wikipedia.exceptions.PageError:
    await ctx.reply('𝙎𝙚𝙖𝙧𝙘𝙝 𝙧𝙚𝙨𝙪𝙡𝙩 𝙣𝙤𝙩 𝙛𝙤𝙪𝙣𝙙. 𝙏𝙧𝙮 𝙬𝙧𝙞𝙩𝙞𝙣𝙜 𝙞𝙩 𝙙𝙞𝙛𝙛𝙚𝙧𝙚𝙣𝙩𝙡𝙮...')
    return
  embed=discord.Embed(title=title, description=result, color=0xc884e1)
  embed.set_author(name="⚝ 𝙒𝙞𝙠𝙞𝙥𝙚𝙙𝙞𝙖 𝙎𝙚𝙖𝙧𝙘𝙝 ⚝")
  embed.set_footer(text="⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙⋙")
  await ctx.send(embed=embed)

# All the error handles
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = 'Please wait another **{:.2f}** before using the command again.'.format(error.retry_after)
    embed=discord.Embed(title="Command On Cooldown", description=msg, color=0x2723fb)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/plantsvszombies/images/c/c7/Time_Traveler2.png/revision/latest?cb=20200317010014")
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
    return
  if isinstance(error, commands.MissingPermissions):
    ctx.channel.delete()
    embed=discord.Embed(title="Permission Denied", description="You don't have the permissions to run the command.", color=0xff0000)
    embed.set_author(name="STOP", icon_url="https://images.vexels.com/media/users/3/193117/isolated/preview/391dc07c463639a67dcb5d471d068bff-stop-covid-badge-by-vexels.png")
    embed.set_thumbnail(url="https://images.vexels.com/media/users/3/136933/isolated/preview/12e4ab9fce4498ed36b9f1d162678300-stop-button-icon-by-vexels.png")
    embed.add_field(name="People who have permissions to run it:", value="Mods", inline=False)
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
    return
  else:
    raise error

TOKEN = os.getenv('token')
dontDieOnMe()
client.run(TOKEN)