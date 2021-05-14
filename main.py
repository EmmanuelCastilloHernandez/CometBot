# Comet's code
# This program was made by Emmanuel Castillo
# Student at NHHS in NH, CA, USA

# Developers:

# Emmanuel Castillo
# GitHub: EmmanuelCastilloHernandez
# Discord: eta_c4rinae#7810
# Email: emmanuelino2@gmail.com

# Garen Gevoryan
# Discord: Warlex#7860

# Importing libraries used in the bot
import asyncio
from datetime import datetime
import discord
from discord.ext import commands
from discord.utils import get
from dontDie import dontDieOnMe
from gtts import gTTS
import math
from googletrans import Translator
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import *
# import numpy as np
# from numpy import *
from PIL import Image, ImageFont, ImageDraw, ImageOps
from io import BytesIO
import random
from random import randint
from replit import db
import os
import youtube_dl
import ffmpeg
import re
import urllib
import randfacts
import requests, json
import string
from discord.ext.commands import Bot
import time

from zalgo_text import zalgo

# This step is only needed if you use poetry in Replit
os.system('pip3 uninstall -y googletrans')
os.system('pip3 install googletrans==3.1.0a0')

# Snipe variables
regularSnipeAuthor = None
regularSnipeMessage = None
snipeMessage = None
snipeMessageAuthor = None
snipeMessage2 = None
snipeMessageAuthor2 = None
snipeMessage3 = None
snipeMessageAuthor3 = None
snipeCounter = 1
editMessageAuthor = None
beforeMessage = None
afterMessage = None
users = None
reactionMessage = None

# Comet audio player Queue

# NOTE: This is the list used by the blacklist to see if a message contains a slur
# This is to help keep slurs at bay
# NOTE: Contains GIFs to be blacklisted
with open("slurs.txt", "r") as slurs:
  bannedWordsPrepare = slurs.readlines()

bannedWords=[]  
bannedWords=[l.replace("\n", "") for l in bannedWordsPrepare]

#prefix for the bot
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
client = commands.Bot(command_prefix="#", intents=intents)
client.remove_command('help')

@client.event
async def on_member_join(member):
  channel = client.get_channel(777364217673678858)
  methuDetect = client.get_user(member.id)

  if methuDetect == 713566308695932950:
    embed=discord.Embed(title=f"{member.name} TRIED TO COME BACK", color=0xc53302)
    embed.set_author(name="UNWANTED USER DETECTED")
    embed.add_field(name="Hi Methu,", value="If you're seeing this, it's because the bot caught you trying to slip back into a server you were barred from entering. You are banned from entering again because you asked two underaged girls to show you their boobs as part of a $5 bet by dav#0560. You don't go and ask for boob pics from girls you 13-year old pervert. Get a life and learn some basic manners because you are going to be in some serious problems in the future, you sellout.", inline=True)
    embed.set_footer(text="Unapologetically, the Developer")

    await member.send(embed=embed)
    await member.ban()
    await channel.send(embed=embed)

@client.event
async def on_raw_reaction_add(payload):
  upEmoji = client.get_emoji(800206782042734612)
  downEmoji = client.get_emoji(800206712606949416)
  print(payload.emoji)
  if payload.emoji.name == "💀":
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    reaction = get(message.reactions, emoji=payload.emoji.name)
    if reaction and reaction.count > 5:
      await message.add_reaction('💀')
  elif payload.emoji == upEmoji:
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    reaction = get(message.reactions)
    print(reaction)
    print(reaction.count)
    if reaction and reaction.count > 3:
      await message.add_reaction('<:up:800206782042734612>')
  elif payload.emoji == downEmoji:
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    reaction = get(message.reactions)
    print(reaction)
    print(reaction.count)
    if reaction and reaction.count > 3:
      await message.add_reaction('<:down:800206712606949416>')
    if reaction and reaction.count > 5:
      await message.add_reaction('<:deletethis:839716370212192258>')

@client.event
async def on_message_edit(before, after):
  global editMessageAuthor
  global beforeMessage
  global afterMessage
  if before.content != after.content:
    editMessageAuthor = before.author
    beforeMessage = before.content
    afterMessage = after.content

    await asyncio.sleep(10)

    editMessageAuthor = None
    beforeMessage = None
    afterMessage = None

# This executes when a message is sent
@client.event
async def on_message(message):

  # Neo Blacklist Code
  content = str(message.content)
  httpsResult = content.startswith('https')
  emojiResult = content.startswith('<a:')
  if emojiResult == True or httpsResult == True:
    print('hello')
  else:
    content = content.translate(str.maketrans('', '', string.punctuation))
  print(content)
  content = content.lower()
  content = content.split()
  print(content)
  
  for x in content:
    if (message.author.bot):
      return
    elif x in bannedWords:
      print('Emmanuel Castillo')
      await message.delete()
  
  # End of Neo Blacklist code

  if message.author == client.user:
    return
  
  serverName = message.guild.name
  with open('levels.json','r') as f:
    users = json.load(f)
  await openLevelUser(message.author, serverName)
  awardLevelPoints = random.randint(1, 3)

  levelBal = users[str(message.author.id)][f'{message.guild.name} XP']
  userBal = users[str(message.author.id)][f'{message.guild.name} Level']

  levelThreshold = 10*1.5*userBal
  await updateLevels(message.author, awardLevelPoints, serverName, f'{message.guild.name} XP')

  if levelBal >= levelThreshold:
    await updateLevels(message.author, 1, serverName, f'{message.guild.name} Level')
    await updateLevels(message.author, -1*levelBal, serverName, f'{message.guild.name} XP')
    userBal = users[str(message.author.id)][f'{message.guild.name} Level']
    await message.channel.send(f'{message.author.mention} has leveled up to level {userBal+1}! Congrats.')
  
  # Bot responds with ^ when someone says ^
  if message.content.startswith('^'):
    await message.channel.send('^')
  
  if message.content.startswith('no one cares'):
    agreedReplies=['agreed\nand I\'m a bot :skull:',
      'agreed',
      '^',
      'ok',
      f'based {message.author.mention}']
    await message.channel.send(f'{random.choice(agreedReplies)}')
  
  if message.content.startswith('Wow. There is no message to snipe buddy.'):
    await message.channel.send('ok')

  await client.process_commands(message)

async def openLevelUser(user, server):
  with open('levels.json','r') as f:
    users = json.load(f)
  
  if str(user.id) in users:
    if f'{server} Level' in users[str(user.id)]: 
      return False
    else:
      users[str(user.id)][f'{server} Level'] = 1
      users[str(user.id)][f'{server} XP'] = 0
  else:
    users[str(user.id)] = {}
    users[str(user.id)][f'{server} Level'] = 1
    users[str(user.id)][f'{server} XP'] = 0
  
  with open('levels.json','w') as f:
    json.dump(users, f)
  return True

async def updateLevels(user, change=0, server=None, mode='Wallet'):
  with open('levels.json','r') as f:
    users = json.load(f)
  
  users[str(user.id)][mode] += change

  with open('levels.json','w') as f:
    json.dump(users, f)
  
  bal = [users[str(user.id)][f'{server} Level'], users[str(user.id)][f'{server} XP']]
  return bal

#client event that gets the snipe function's variables ready
@client.event
async def on_message_delete(message):
  global regularSnipeAuthor
  global regularSnipeMessage
  global snipeMessage
  global snipeMessageAuthor
  global snipeMessage2
  global snipeMessageAuthor2
  global snipeMessage3
  global snipeMessageAuthor3
  global snipeCounter

  regularSnipeAuthor = message.author
  regularSnipeMessage = message.content
  if snipeCounter == 1:
    snipeMessage = message.content
    snipeMessageAuthor = message.author
    snipeCounter += 1

  elif snipeCounter == 2:
    snipeMessage2 = message.content
    snipeMessageAuthor2 = message.author
    snipeCounter += 1

  elif snipeCounter == 3:
    snipeMessage3 = message.content
    snipeMessageAuthor3 = message.author

    snipeCounter = 1
    print('New snipe val: '+ str(snipeCounter))

  await asyncio.sleep(120)

  snipeCounter = 1
  snipeMessage = None
  snipeMessageAuthor = None
  snipeMessage2 = None
  snipeMessageAuthor2 = None
  snipeMessage3 = None
  snipeMessageAuthor3 = None
  regularSnipeAuthor = None
  regularSnipeMessage = None

@client.event
async def on_ready():
  await client.change_presence(activity = discord.Streaming(name = '♥ Sugar Crash ♥', url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
  print('Ready for deployment. \nThank you for using Comet')

@client.command(pass_context=True)
async def rank(ctx, member: discord.Member=None):
  serverName = ctx.guild.name
  if member == None:
    member = ctx.author
  with open('levels.json','r') as f:
    users = json.load(f)
  await openLevelUser(member, serverName)

  levelBal = users[str(member.id)][f'{serverName} XP']
  userBal = users[str(member.id)][f'{serverName} Level']

  levelThreshold = 10*1.5*userBal

  embed=discord.Embed(title=f"▧ Rank for {member} ▧", description="=============================")
  embed.set_author(name="▞ Comet Rank System ▚")
  embed.set_thumbnail(url=member.avatar_url)
  embed.add_field(name="Level:", value=f"*__{userBal}__*", inline=True)
  embed.add_field(name="XP:", value=f"*__{levelBal}__*", inline=True)
  embed.add_field(name="XP Needed to Level Up:", value=f"*__{levelThreshold - levelBal}__*", inline=True)
  embed.set_footer(text="Comet Alert")
  await ctx.reply(embed=embed, mention_author=False)

@client.command(pass_context=True)
async def levels(ctx, number=5):
  serverName = ctx.guild.name
  with open('levels.json','r') as f:
    users = json.load(f)
  await openLevelUser(ctx.author, serverName)
  level = {}
  levelList = []

  levelChecker = f'{serverName} Level'

  for user in users:
    name = int(user)
    userBal = users[user][levelChecker]
    level[userBal] = name
    levelList.append(userBal)
  
  levelList = sorted(levelList, reverse=True)

  embed=discord.Embed(title=f"‣‣‣‣‣‣‣‣‣‣‣ Now Showing Top {number} Users in {serverName} ‣‣‣‣‣‣‣‣‣‣‣‣", color=0x0502c5)
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


# @client.command(aliases=['graph','showMe','plot'])
# async def graphFunction(ctx, type, val1=0, val2=0, val3=0, val4=0):
#  v1 = int(val1)
#  v2 = int(val2)
#  v3 = int(val3)
#  v4 = int(val3)
#
#  x = linspace(-5,5,5000)
#  if (str(type) == 'linear' or str(type) == 'l'):
#    if v1 == 0:
#      y=v2*x
#    else:
#      y = v1+v2*x
#    graphEquation = f'{v2}X+{v1}'
#  if (str(type) == 'quadratic' or str(type) == 'q'):
#    if v1 == 0:
#      y = v2*x+v3*x**2
#    elif (v2 == 0 and v1 == 0):
#      y = v3*x**2
#    elif v2 == 0:
#      y = v1+v3*x**2
#    else:
#      y = v1+v2*x+v3*x**2
#    graphEquation = f'{v3}X^2+{v2}X+{v1}'
#  if (str(type) == 'cubic' or str(type) == 'c'):
#    if v1 == 0:
#      y = v2*x+v3*x**2+v4*x**3
#    if v2 == 0:
#      y = v2*x+v3*x**2+v4*x**3
#    if v3 == 0:
#      y = v2*x+v3*x**2+v4*x**3
#    if v4 == 0:
#      y = v2*x+v3*x**2+v4*x**3
#    
#    y = v1+v2*x+v3*x**2+v4*x**3
#    graphEquation = f'{v4}X^3+{v3}X^2+{v2}X+{v1}'
#  
#  plt.plot(x,y)
#  plt.xlabel("X-axis")
#  plt.ylabel("Y-axis")
#  plt.grid(axis='both', color = 'green', linestyle = '--', linewidth = 0.5)
#  plt.axhline(0, color='red')
#  plt.axvline(0, color='red')
#  plt.title(graphEquation)
#  plt.savefig('plot.png')
#  chart = file=discord.File("/home/runner/Comet/plot.png")
#  embed=discord.Embed(title=f"Here is your graph for {graphEquation}", color=0x00ffee)
#  embed.set_image(url="attachment://plot.png")
#  embed.set_author(name="Comet Calculator")
#  await ctx.send(embed=embed, file=chart)
#  plt.clf()

# START OF THE ECONOMY SECTION
shopItems = [{'name':'Feet Pic','price':100,'description':'Someone\'s feet pics. Using them will give you a special surprise.'},
  {'name':'Comet Emotion Engine','price':10,'description':'The emotion engine ***Comet*** has. Gives a multiplier of 2*`amount you use`. Doesn\'t stack with other multipliers'},
  {'name':'Gun','price':1000,'description':'Used to shoot.'},
  {'name':'Laptop','price':500,'description':'Use it to surf the Web'},
  {'name':'Phone','price':500,'description':'The Castillo Phone 2XS Pro MAX. Use #phone to be able to scam people and do other things.'},
  {'name':'Padlock','price':2000,'description':'Protect yourself from being robbed. Do #Padlock to use it.'},
  {'name':'Fuck Card','price':2000,'description':'#fuck to use it. Tho why would you buy it you horny bastard.'}]

@client.command(pass_context=True)
async def wanted(ctx, member:discord.Member=None):
  if member == None:
    member = ctx.author

  wanted = Image.open("wanted.png")
  draw = ImageDraw.Draw(wanted)
  font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 35)

  asset = member.avatar_url_as(size=256)
  data = BytesIO(await asset.read())
  pfp = Image.open(data)
  reward = ['Nothing','Amogus','$10 or even ¢1', '$0', '$100', '$500', '$1,000', '$5,000', '$10,000','$20,000','$25,000','$50,000','$60,000','$75,000','$85,000','$100,000','$150,000','$250,000','$1,000,000','My Heart \u2665']

  pfp = pfp.resize((305,305))
  draw.text((101,150), f"{member.nick}", font=font, fill=(23, 23, 80))
  wanted.paste(pfp, (101,190))
  draw.text((101,506), f"REWARD:", font=font, fill=(23, 23, 80))
  draw.text((101,540), f"{random.choice(reward)}", font=font, fill=(23, 23, 80))
  wanted.save('wantedPoster.png')

  await ctx.reply(file = discord.File('wantedPoster.png'), mention_author=False)

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
  textDraw.text((0, 0), f"{member.nick}",  font=font, fill=255)
  w = textToRotate.rotate(17.5,  expand=1)
  wanted.paste(ImageOps.colorize(w, (0,0,0), (23,23,80)), (116,-10),  w)
  wanted.save('deathNote.jpg')

  await ctx.reply(file = discord.File('deathNote.jpg'), mention_author=False)

@client.command(aliases=['lead','Lead','Leaderboard','lb','ul'])
async def leaderboard(ctx, number=3):
  with open('bank.json','r') as f:
    users = json.load(f)
  leaderboard = {}
  total = []

  for user in users:
    name = int(user)
    totalAmount = users[user]['Wallet'] + users[user]['Bank']
    leaderboard[totalAmount] = name
    total.append(totalAmount)
  
  total = sorted(total, reverse=True)

  embed=discord.Embed(title=f"‣‣‣‣‣‣‣‣‣‣‣ Now Showing {number} Users of The Economy ‣‣‣‣‣‣‣‣‣‣‣‣", color=0x0502c5)
  index = 1
  for amt in leaderboard:
    id_ = leaderboard[amt]
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
  with open('bank.json','r') as f:
    users = json.load(f)
  
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
          responses = ['The bullet richcheted and hit you. You didn\'t die',
            f'Instead of shooting {member.mention} , you go || . . . || them. Horny bastard.',
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
      embed=discord.Embed(title="Phone Options", description=f"Hey {user.mention}, react to this message to choose an option. You have 30 seconds.", color=0x00ffee)
      embed.set_thumbnail(url="https://images.vexels.com/media/users/3/128754/isolated/preview/d7966cba43a9c647bb596a02c6756f3f-smart-phone-icon-by-vexels.png")
      embed.add_field(name="Scam", value="🧡", inline=True)
      embed.add_field(name="VC TTS", value="💛", inline=True)
      embed.add_field(name="Send a DM to a User", value="💙", inline=True)
      embed.set_footer(text="Comet Phone Alert")
      embed1 = await ctx.send(embed=embed)
      await embed1.add_reaction('🧡')
      await embed1.add_reaction('💛')
      await embed1.add_reaction('💙')
    
      def check(reaction, user):
        return user == ctx.author and (str(reaction.emoji) == '🧡' or str(reaction.emoji) == '💛' or str(reaction.emoji) == '💙')

      try:
        reaction, user = await client.wait_for('reaction_add', timeout=20.0, check=check)

        if str(reaction.emoji) == '🧡':
          await ctx.send('Ping the user you want to scam.')
          try:
            def check(m):
              return m.author == ctx.author

            msg = await client.wait_for('message', timeout=20, check=check)
            prepare1 = msg.content.replace('<@!', '')
            prepare2 = prepare1.replace('>', '')
            finalPrepare = int(prepare2)

            userToScam = client.get_user(finalPrepare)
            print(userToScam)

            await ctx.invoke(client.get_command('rob'), member=userToScam, scam=True, phoneRobber=ctx.author)
          except asyncio.TimeoutError:
            await ctx.send('The phone\'s battery ran out.')
        if str(reaction.emoji) == '💛':
          await ctx.reply('Input the text you want ***Comet*** to say.', mention_author=False)
          try:
            def check(m):
              return m.author == ctx.author

            msg = await client.wait_for('message', timeout=20, check=check)

            await ctx.invoke(client.get_command('repeat'), text=msg.content)
            await ctx.invoke(client.get_command('leave'), yes=True)

          except asyncio.TimeoutError:
            await ctx.send('The phone\'s battery ran out.')
        if str(reaction.emoji) == '💙':
          await ctx.reply('Ping the user you want to send the message to (Don\'t worry I\'ll delete the ping).', mention_author=False)
          try:
            def check(m):
              return m.author == ctx.author

            msg = await client.wait_for('message', timeout=20, check=check)

            prepare1 = msg.content.replace('<@!', '')
            prepare2 = prepare1.replace('>', '')
            finalPrepare = int(prepare2)
            userToDM = client.get_user(finalPrepare)

            await msg.delete()

            await ctx.reply('Now type what you want to send to the user.', mention_author=False)

            try:
              def check(m):
                return m.author == ctx.author

              msgText = await client.wait_for('message', timeout=20, check=check)
              await userToDM.send(f'New DM from a user in **`{ctx.guild.name}`**\n**__{ctx.author.id}__**: {msgText.content}')

            except asyncio.TimeoutError:
              await ctx.send('Your Mobile data ran out. Thank the 5 GB Haley-Mobile Data Plab.')

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
          await ctx.reply(f'You don\'t have fuck cards.', mention_author=False)
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

@client.command(pass_context=True)
async def OverthrowMods(ctx):
  await ctx.send('Overthrow the mods.')

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
    embed.add_field(name="The Slot Result:", value=f"{slot}", inline=True)
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
    'Dev Note #5: Hardest thing to create in the bot was the warning system.',
    'Dev Note #6: Comet Music Player supports text search',
    'Dev Note #7: Hangman on an embed was hell.',]
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
  embed=discord.Embed(title="List of all commands: Page 1", color=0xfff024)
  embed.set_author(name="Help Center")
  embed.set_thumbnail(url="https://images.vexels.com/media/users/3/153750/isolated/preview/1fb0b5422a7584ed0df14dfacdc68c64-internet-settings-colored-stroke-icon-by-vexels.png")
  embed.set_footer(text="Comet Alert")
  
  embed2=discord.Embed(title="List of all commands: Page 2", color=0xfff024)
  embed2.set_thumbnail(url="https://images.vexels.com/media/users/3/153750/isolated/preview/1fb0b5422a7584ed0df14dfacdc68c64-internet-settings-colored-stroke-icon-by-vexels.png")
  embed2.set_footer(text="Comet Alert")

  embed3=discord.Embed(title="List of all commands: Page 3", color=0xfff024)
  embed3.set_thumbnail(url="https://images.vexels.com/media/users/3/153750/isolated/preview/1fb0b5422a7584ed0df14dfacdc68c64-internet-settings-colored-stroke-icon-by-vexels.png")
  embed3.set_footer(text="Comet Alert")

  embed4=discord.Embed(title="List of all commands: Page 4", color=0xfff024)
  embed4.set_thumbnail(url="https://images.vexels.com/media/users/3/153750/isolated/preview/1fb0b5422a7584ed0df14dfacdc68c64-internet-settings-colored-stroke-icon-by-vexels.png")
  embed4.set_footer(text="Comet Alert")

  for command in client.commands:
    if embedCommands <= 18:
      embed.add_field(name=f'{command} | {command.aliases}', value=command.help, inline=True)
      embedCommands += 1
    elif embedCommands <= 36:
      embed2.add_field(name=f'{command} | {command.aliases}', value=command.help, inline=True)
      embedCommands += 1
    elif embedCommands <= 54:
      embed3.add_field(name=f'{command} | {command.aliases}', value=command.help, inline=True)
      embedCommands += 1
    else:
      embed3.add_field(name=f'{command} | {command.aliases}', value=command.help, inline=True)
      embedCommands += 1
  
  if pg == 1:
    await ctx.send(embed=embed)
  if pg == 2:
    await ctx.send(embed=embed2)
  if pg == 3:
    await ctx.send(embed=embed3)
  if pg == 4:
    await ctx.send(embed=embed3)

@client.command(aliases=['weather','heavy weather'])
@commands.cooldown(1, 5, commands.BucketType.guild)
async def weatherReport(ctx):
  APIKEY = os.getenv('apiKey')
  api_key = APIKEY

  base_url = "http://api.openweathermap.org/data/2.5/weather?"

  try:
    await ctx.send("`Input your city now:`")
    grabCity = await client.wait_for('message', check=None, timeout=15)
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
    # temperature in celsius stored in variable `celsius_temp`
    celcisus_temp = tempToConvert - 273.15
    # convert celsius to fahrenheit stored in variable `fahrenheit_temp`
    fahrenheit_temp = celcisus_temp * ( 9 / 5 ) + 32

    fahrenheit_temp = math.floor(fahrenheit_temp)
  
    embed=discord.Embed(description=f"Temperature (in fahrenheit): __**{str(fahrenheit_temp)}\u00b0**__\nAtmospheric pressure (in hPa unit): **__{str(current_pressure)}__**\nHumidity: **__{str(current_humidiy)}\u0025__**\nDescription: **__{str(weather_description)}__**", color=0x13f6e7)
    embed.set_thumbnail(url="https://png.pngtree.com/png-clipart/20190924/original/pngtree-planet-earth-icon-design-png-image_4804418.jpg")
    embed.set_author(name=f"Weather Report for {city.upper()} by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
  
  else:
    await ctx.send("`Your city of choice was not found.`")

@client.command(help='Use it with chat or server when they are dead.')
@commands.cooldown(1, 10, commands.BucketType.user)
async def dead(ctx, *, type=None):
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
      'https://tenor.com/view/dead-chat-gif-18792024',
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
  
  with open("slurs.txt", "r+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    file_object.write(f'{word}')

  with open("slurs.txt", "r") as slurs:
    bannedWordsPrepare = slurs.readlines()

  bannedWords = []
  bannedWords=[l.replace("\n", "") for l in bannedWordsPrepare]
  print(bannedWords)
  await ctx.send(f'Added {wordToAdd} to the blacklist.')
  return bannedWords

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
  
  with open("slurs.txt", "r+") as f:
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i != str(word):
            f.write(i)
    f.truncate()

  with open("slurs.txt", "r") as slurs:
    bannedWordsPrepare = slurs.readlines()

  bannedWords=[]  
  bannedWords=[l.replace("\n", "") for l in bannedWordsPrepare]
  print(bannedWords)
  await ctx.send(f'Removed {wordToRemove} from the blacklist.')
  return bannedWords

@client.command(help='Use when the server failed')
@commands.cooldown(1, 10, commands.BucketType.user)
async def failed(ctx, *, type):
  if (str(type) == 'server'):
    pictures = ['https://tenor.com/view/reaction-mrw-ihave-failed-you-obi-wan-kenobi-gif-4991213',
      'https://tenor.com/view/you-failed-gif-15415391',
      'https://tenor.com/view/failed-rayya-gif-18980198',
      'https://tenor.com/view/adventure-time-ice-king-ifailed-failure-upset-gif-4910391',
      'https://tenor.com/view/ifailed-iko-uwais-kai-jin-wu-assassins-failure-gif-18615922']
    await ctx.send(f'The server be like: {random.choice(pictures)}')

#Snipe command
@client.command(help='A super snipe command for snitches')
@commands.cooldown(1, 10, commands.BucketType.user)
async def SuperSnipe(ctx, *, messageToRetrieveA=1):
  messageToRetrieve = int(messageToRetrieveA)
  
  if snipeMessage == None:
    print('hale bopp')
    if snipeMessage2 == None:
      print('android')
      if snipeMessage3 == None:
        print('egg')
        await ctx.channel.send(f'No snipable message, {ctx.author.mention}.')
  else:
    print('takis')
    if messageToRetrieve == 1:
      print('nuttala')
      embed = discord.Embed(description=f'{snipeMessage}')
      embed.set_footer(
        text=
        f"Messaged sniped by {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=ctx.author.avatar_url)
      embed.set_author(name=f'Sniped from {snipeMessageAuthor}')
      await ctx.channel.send(embed=embed)
    if messageToRetrieve == 2:
      print('frosting')
      embed2 = discord.Embed(description=f'{snipeMessage2}')
      embed2.set_footer(
        text=
        f"Messaged sniped by {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=ctx.author.avatar_url)
      embed2.set_author(name=f'Sniped from {snipeMessageAuthor2}')
      await ctx.channel.send(embed=embed2)
    if messageToRetrieve == 3:
      print('candy')
      embed3 = discord.Embed(description=f'{snipeMessage3}')
      embed3.set_footer(
        text=
        f"Messaged sniped by {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=ctx.author.avatar_url)
      embed3.set_author(name=f'Sniped from {snipeMessageAuthor3}')
      await ctx.channel.send(embed=embed3)
    
  await ctx.send(f'{ctx.author.mention} is a snitch! Please use the other command like everyone else.')
  await ctx.send(f'Fuck off {ctx.author.mention}')
  
@client.command(aliases=['retrieve','snitch','Snipe'], pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def snipe(ctx):
  if regularSnipeMessage == None:
    await ctx.send(f'There\'s no retrievable message, {ctx.author.mention}')
  else:
    embed = discord.Embed(description=f'{regularSnipeMessage}')
    embed.set_footer(
      text=
      f"Messaged sniped by {ctx.author.name}#{ctx.author.discriminator}",
      icon_url=ctx.author.avatar_url)
    embed.set_author(name=f'Sniped from {regularSnipeAuthor}')
    await ctx.channel.send(embed=embed)

# Hello command
# First command in Comet
# @client.command(help='Hello command')
# @commands.cooldown(1, 10, commands.BucketType.user)
# async def hello(ctx):
#  await ctx.send('Hello human!')

# NOTE: Some commands of people are made at their request and with consent to use their pics
@client.command(aliases=['Charleze','Charcheese','Charlie','Charfeces','charleze','charcheese','charfeces','charlie'],help='Char Command')
@commands.cooldown(1, 5, commands.BucketType.user)
async def char(ctx):
  charGifs=['https://tenor.com/view/full-house-kiss-kisses-i-love-you-char-char-blow-kiss-gif-15543988',
    'https://tenor.com/view/munch-munchies-thumper-bambie-char-gif-15543996','https://tenor.com/view/hug-virtual-hug-hug-sent-sending-virtual-hug-from-char-gif-17840781',
    'https://tenor.com/view/angela-balagtas-angela-jelay-jelay-balagtas-angela-julia-balagtas-selfie-gif-17838206',
    'https://tenor.com/view/char-blythe-andrea-gold-squad-the-gold-squad-gif-16006749',
    '/home/runner/Comet/weirdPics/charPic1.png',
    '/home/runner/Comet/weirdPics/charPic2.png',
    '/home/runner/Comet/weirdPics/charPic3.png',
    '/home/runner/Comet/weirdPics/charPic4.png',
    '/home/runner/Comet/weirdPics/charPic5.png',
    '/home/runner/Comet/weirdPics/charPic6.png',
    '/home/runner/Comet/weirdPics/charPic7.png',
    '/home/runner/Comet/weirdPics/charPic8.png',
    '/home/runner/Comet/weirdPics/charPic9.png',
    '/home/runner/Comet/weirdPics/charPic10.png',
    '/home/runner/Comet/weirdVidsOfEvery1/charVid1.mov']

  CharThingToShow = random.choice(charGifs)
  
  check = os.path.isfile(CharThingToShow)
  print(check)
  if check == False:
    await ctx.channel.send(f'{CharThingToShow}')
  else:
    await ctx.send(file=discord.File(CharThingToShow))

@client.command(aliases=['stee','Steven','steveb','stevem'], help='steven command')
@commands.cooldown(1, 5, commands.BucketType.user)
async def steven(ctx):
  stevenStuff = ['https://tenor.com/view/steven-silly-face-gif-12456502',
    'https://tenor.com/view/yes-steven-gif-13773302',
    'https://tenor.com/view/steven-when-steven-when-someone-makes-aminor-mistake-steven-when-minor-steven-yo-gif-20131094',
    'https://tenor.com/view/cookie-monster-little-steven-when-you-hear-gif-16781451',
    'https://tenor.com/view/steven-stephen-hotchkin-steven-hotchkin-steven-funny-stephen-funny-gif-20220390',
    'https://tenor.com/view/steven-where-is-steven-looking-for-steven-gorilla-kang-beomhyun-gif-14392204',
    'https://tenor.com/view/stupid-dumb-pointing-steven-gif-17317236',
    'https://tenor.com/view/steven-steven-universe-steven-name-name-cartoon-network-gif-14838515',
    'https://tenor.com/view/big-floppa-floppa-nle-glopnar-prozhony-new-rapper-gif-19385404',
    'https://tenor.com/view/big-floppa-gif-21174492',
    'https://tenor.com/view/floppa-gargantious-floppa-big-floppa-diives-roblox-r-gif-21118626',
    'https://tenor.com/view/floppa-chris-gif-20982019',
    'https://tenor.com/view/floppa-gif-20953803',
    'https://tenor.com/view/floppa-floppa-planet-planet-gregory-big-floppa-gif-20806372',
    'https://tenor.com/view/flop-rotation-floppa-big-floppa-gif-20538168',
    '/home/runner/Comet/weirdVidsOfEvery1/stevenVid1.mov']

  stevenThingToShow = random.choice(stevenStuff)
  
  check = os.path.isfile(stevenThingToShow)
  print(check)
  if check == False:
    await ctx.channel.send(f'{stevenThingToShow}')
  else:
    await ctx.send(file=discord.File(stevenThingToShow))  

@client.command(help='Charboo of course!')
@commands.cooldown(1, 10, commands.BucketType.user)
async def charboo(ctx):
  await ctx.channel.send('https://tenor.com/view/flairwars-charboo-charboo2-gif-18874808')

@client.command(aliases=['shit'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def shitServer(ctx, choice):
  shitServerReplies=['Correct.',
    f'Shit server, shit mods, and shitty bot, amiright {ctx.author.mention}',
    'ok.',
    'yes']
  if (str(choice) == 'server'):
    await ctx.send(f'{random.choice(shitServerReplies)}')
  if (str(choice) == 'reasoning'):
    await ctx.channel.send('Shit reasoning')

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
@commands.cooldown(1, 10, commands.BucketType.user)
async def _8ball(ctx, *, question):
  responses = ['Certain. Its only a matter of time now',
    'It is decidedly so :smiley:', '¡Sin duda!',
    'Definitely yes. Don\'t worry about it!',
    'No. JK, you can rely on it with your life!',
    'From the looks of it, yes!', 'From what I see, yes!', 'Probably'
    'Good chance it\'s yes...', 'Yes :smiley:',
    'Signs are pinting to yes...',
    'The reply I have is hazy af. Try again or ask a different question :|',
    'Mx. Person try asking that again :|. You were mumbling...',
    'I\'m not telling you that rn :no_mouth:',
    'I\'m too busy to predict rn. Try again l8r :rage:',
    'Concentrate porque ahorita se estas sonando como un trogodita...:rage:',
    'Don\'t try to count on this.', 'I\'m telling you, it\'s a NO! :{',
    'Sources close to me have spoken. They say \u041f\u047a\u20b1\u20ac',
    'Forecast is bad for this one...\u047e',
    'I\'m very doubtful about this one...\u047c']
  await ctx.send(f'The question was: {question}\n:8ball: My answer is: {random.choice(responses)}')

@client.command(aliases=['delete', 'delet'], help='Clear command obviously.')
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def clear(ctx, maxamount=15):
  await ctx.channel.purge(limit=maxamount)
  await ctx.channel.send(f'Deleted **{maxamount}** messages.')

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
@client.command(aliases=['rf', 'randomfact'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def Arandomfack(ctx):
  fct = randfacts.getFact()
  await ctx.channel.send(fct)

@client.command(aliases=['furry','furryalert'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def crusader(ctx):
  crusaderGifs=['https://tenor.com/view/unacceptable-knight-lock-and-load-cocks-gun-gif-17380126',
    'https://tenor.com/view/deus-vult-crusades-shake-triggered-intensifies-gif-16436511',
    'https://tenor.com/view/meme-soniknowreligionisimportant-crusader-dues-vult-gif-11697017',
    'https://tenor.com/view/crusade-cyber-fashwave-crusader-glitch-gif-19022516',
    'https://tenor.com/view/crusader-shocked-shotgun-gif-17982096',
    'https://tenor.com/view/crusader-uno-reverse-crusader-uno-reverse-uno-crusader-uno-reverse-red-eyes-gif-17741833']
  await ctx.send(f'{random.choice(crusaderGifs)}')

@client.command(aliases=['sussy', 'susie', 'amogus', 'amongus'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def sus(ctx):
  susGifs = ['https://media.tenor.co/videos/528c8fefa503d1411656267c91a93f43/mp4',
    'https://tenor.com/view/you-got-it-snowing-dentist-mexico-minion-gif-19502972',
    'https://tenor.com/view/among-us-red-sus-suspect-among-gif-19597730',
    'https://tenor.com/view/among-us-impostor-imposter-digibyte-twerk-gif-19659754',
    'https://tenor.com/view/grinch-when-the-imposter-is-sus-among-us-grinch-meme-among-us-meme-gif-19566326',
    'https://tenor.com/view/sus-heart-sus-locket-sus-heart-gif-20749877',
    'https://tenor.com/view/looking-mad-sus-sus-mad-sus-inam-sus-inam-gif-20656225',
    'https://tenor.com/view/sus-gif-20628699',
    'https://tenor.com/view/among-us-mungus-neck-neck-break-neck-snap-gif-18599860']
  await ctx.channel.send(f'{random.choice(susGifs)}')

# This function is responsible for warning people
@client.command(aliases=['givewarning', 'givewarn'], help='Warn command for mods.', pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(kick_members=True, administrator=True)
async def warn(ctx, user: discord.Member, *, reason=None):
  userCheck = str(user)
  admin = get(ctx.guild.roles, name='Admin')
  coolerppl = get(ctx.guild.roles, name='cooler people')
  owner = get(ctx.guild.roles, name='creator, not tyler')

  if "warnings" in db.keys():
    warnings = db["warnings"]
    warnings.append(f'{user}')
    db["warnings"] = warnings
    print(db["warnings"])
    await ctx.channel.send(f'I have warned {user} for {reason}')

    resultado = len(list(filter(lambda x: userCheck in x, db["warnings"])))

    for role in user.roles:
      if (str(role.name) == str(coolerppl)):
        if resultado >= 12:
          await ctx.channel.send(f'Your time is **fucking** up, {user}! Mods have been notified. You better hope you dont get kicked.')
          await ctx.channel.send( f'Hey {admin.mention}, {user} has gotten enough warnings to get themselves kicked/ban. Decide their fate.')
      elif (str(role.name) != str(coolerppl)):
        if resultado >= 9:
          await ctx.channel.send(f'Your time is up, {user}! Mods have been notified. Start saying goodbye to everyone here.')
          await ctx.channel.send(f'Hey {admin.mention}, {user} has gotten enough warnings to get themselves kicked/ban. Decide their fate.')
      elif (str(role.name) == str(admin)):
        if resultado >=4:
          await ctx.channel.send(f'Hey {owner.metion}, {user} has gotten enough warnings to get their mod taken away')


  else:
    db["warnings"] = [user]
    db["warnings"] = warnings
    print(db["warnings"])

    resultado = len(list(filter(lambda x: userCheck in x, db["warnings"])))

    for role in user.roles:
      if (str(role.name) == str(coolerppl)):
          if resultado >= 12:
            await ctx.channel.send(f'Your time is **fucking** up, {user}! Mods have been notified. You better hope you dont get kicked.')
            await ctx.channel.send(f'Hey {admin.mention}, {user} has gotten enough warnings to get themselves kicked/ban. Decide their fate.')
          elif (str(role.name) != str(coolerppl)):
            if resultado >= 9:
              await ctx.channel.send(f'Your time is up, {user}! Mods have been notified. Start saying goodbye to everyone here.')
              await ctx.channel.send( f'Hey {admin.mention}, {user} has gotten enough warnings to get themselves kicked/ban. Decide their fate.')

  warnmessage = f'`YOU` have been given a warning in **{ctx.guild.name}** for {reason}.'
  await user.send(warnmessage)
  return reason


@client.command(aliases=['takewarn', 'unwarn'], help='Remove a warn')
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(kick_members=True, administrator=True)
async def removewarn(ctx, *, user: discord.Member, reason=None):
  warnings = db["warnings"]
  userAndReason = f'{user} {reason}'
  print(userAndReason)
  print(db["warnings"])

  if reason == None:
    warnings.remove(f'{user}')
  else:
    warnings.remove(userAndReason)

  db["warnings"] = warnings
  await ctx.channel.send(f'Removed one single warning from {user}. Now begone :|')

@client.command(aliases=['mywarns', 'warningsfor', 'infraction', 'warnsfor', 'warns'], help='Lists all your warnings.')
@commands.cooldown(1, 5, commands.BucketType.user)
async def infractions(ctx, *, user: discord.Member):
  warnings = db["warnings"]
  print(warnings)

  usertotrack = str(user)

  res = len(list(filter(lambda x: usertotrack in x, db["warnings"])))
  print(res)

  db["warnings"] = warnings
  await ctx.channel.send(f'{user} has been warned ' + str(res) + ' times. What a hag. :cold_face:!')

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
    if ctx.channel.id == 736621294799552542:
      message = ctx.message
      await message.delete()

      errorEmbed=discord.Embed(title="Command Not Allowed", description=f"{ctx.author.mention}, this command (**{message.content}**) is not allowed here. Try in a separate channel.", color=0xff0000)
      errorEmbed.set_thumbnail(url="https://media.discordapp.net/attachments/736621294799552542/833749796602642492/unknown.png?width=586&height=586")
      errorEmbed.add_field(name="Examples of Channels Where it Works:", value="spam, botcommands", inline=False)
      errorEmbed.set_footer(text="Comet Alert")
      return await ctx.send(embed=errorEmbed, delete_after=10)

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
    if ctx.channel.id == 736621294799552542:
      message = ctx.message
      await message.delete()

      errorEmbed=discord.Embed(title="Command Not Allowed", description=f"{ctx.author.mention}, this command (**{message.content}**) is not allowed here. Try in a separate channel.", color=0xff0000)
      errorEmbed.set_thumbnail(url="https://media.discordapp.net/attachments/736621294799552542/833749796602642492/unknown.png?width=586&height=586")
      errorEmbed.add_field(name="Examples of Channels Where it Works:", value="spam, botcommands", inline=False)
      errorEmbed.set_footer(text="Comet Alert")
      return await ctx.send(embed=errorEmbed, delete_after=10)

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

@client.command(aliases=['Hangman', 'hangma'], help='hangman duh')
@commands.cooldown(1, 10, commands.BucketType.user)
async def hangman(ctx):
  if ctx.channel.id == 736621294799552542:
    message = ctx.message
    await message.delete()

    errorEmbed=discord.Embed(title="Command Not Allowed", description=f"{ctx.author.mention}, this command (**{message.content}**) is not allowed here. Try in a separate channel.", color=0xff0000)
    errorEmbed.set_thumbnail(url="https://media.discordapp.net/attachments/736621294799552542/833749796602642492/unknown.png?width=586&height=586")
    errorEmbed.add_field(name="Examples of Channels Where it Works:", value="spam, botcommands", inline=False)
    errorEmbed.set_footer(text="Comet Alert")
    return await ctx.send(embed=errorEmbed, delete_after=10)
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
  words = ['captain','Comet', 'slower', 'proton', 'minecraft', 'fake', 'coldplay','avicii', 'spam','fortnite', 'megillah', 'chemistry', 'exist', 'fox']
  
  prepareWord = random.choice(words)

  word = list(prepareWord)
  hangmanEmbed = discord.Embed(description=hangmanPoses[tries])
  hangmanEmbed.set_author(name='Hangman by E.C.H.', icon_url=ctx.author.avatar_url)
  
  for character in word:
    hiddenWord.append('_')
    print(hiddenWord)
  
  while not wonHangman:
    print(word)
    try:
      await ctx.send(embed=hangmanEmbed)
      await ctx.send(f"Put your guess before 15 seconds pass by.\n``The word is: {' '.join(hiddenWord)}``")
      grabUserInput = await client.wait_for('message', check=None, timeout=15)
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

    if all("_" == char for char in word) or word == guess:
      await ctx.send(f'**YOU WON**. The word was indeed **__`{prepareWord}`__**')
      wonHangman = True

@client.command(aliases=['zalgo','cursedtext'], help='Z̵̤ͫ A̋ͨ͝ L̬ͣ͡ G͊ͤ͜ Ö͕́̀')
@commands.cooldown(1, 10, commands.BucketType.guild)
async def makeZalgo(ctx, *, textToZalgofy):
  finalText = zalgo.zalgo().zalgofy(textToZalgofy)
  await ctx.send(f'`{finalText}`')

@client.command(help='Edit command for snitches')
@commands.cooldown(1, 10, commands.BucketType.guild)
async def edit(ctx):
  embed=discord.Embed(title=f"Author: {editMessageAuthor}", color=0x61ffd2)
  embed.set_author(name="Messaged Edited")
  embed.add_field(name="Before:", value=f"{beforeMessage}", inline=False)
  embed.add_field(name="After:", value=f"{afterMessage}", inline=True)
  await ctx.send(embed=embed)
  await ctx.send(f'SNITCH {ctx.author.mention}')

# Muisc Player Code
@client.command(pass_context = True)
async def play(ctx, *, url : str):
  if (ctx.author.voice):
    voice2 = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice2 == None:
      channel = ctx.message.author.voice.channel
      voice = await channel.connect()
    else:
      print('hello')

    # Downloading the Youtube video
    ydl_opts = {
      'format': 'best audio',
      'postprocesssors':[{
        'key': 'FFmpegExtractAudio',
        'prefferedcodec': 'mp3',
        'prefferedquality':'192',
      }],
    }
    
    try:
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
      for file in os.listdir('./'):
        if file.endswith('.mp3') or file.endswith('.webm') or file.endswith('.m4a'):
          os.rename(file, 'song.mp3')
    except youtube_dl.utils.DownloadError:
      embed=discord.Embed(title="Comet Music Player", description="Now processing your request. This may take a bit because of it having to be downloaded.", color=0xe29797)
      embed.set_thumbnail(url='https://images.vexels.com/media/users/3/136461/isolated/preview/d8279505f7fa8e7cd761c755be58f0b7-colorful-music-note-icon-by-vexels.png')
      embed.add_field(name="Requested by:", value=f"{ctx.author.mention}", inline=True)
      embed.add_field(name="Channel:", value=f"{ctx.message.author.voice.channel}", inline=True)
      embed.set_footer(text="Comet Alert")
      await ctx.reply(embed=embed)

      os.system(f"youtube-dl --extract-audio --audio-format mp3 ytsearch:\'{url}\'")
      for file in os.listdir('./'):
        if file.endswith('.mp3') or file.endswith('.webm'):
          os.rename(file, 'song.mp3')
    
    embed=discord.Embed(title="Comet Music Player", description=f"Now Playing: **{url}**.", color=0xe29797)
    embed.set_thumbnail(url="https://images.vexels.com/media/users/3/161756/isolated/preview/ea4532cd7cfb79ce0cab3f663f19aef9-heartbeat-with-music-notes-by-vexels.png")
    embed.add_field(name="Requested by:", value=f"{ctx.author.mention}", inline=True)
    embed.add_field(name="Channel:", value=f"{ctx.message.author.voice.channel}", inline=True)
    embed.set_footer(text="Comet Alert")
    await ctx.reply(embed=embed)

    audio_source = discord.FFmpegPCMAudio('song.mp3')
    player = voice.play(audio_source)
    player.start()

  else:
    await ctx.send("You need to be in a voice channel to run this command")

@client.command(pass_context = True)
async def leave(ctx, musicCommand=False):
  if (ctx.voice_client):
    print(musicCommand)
    await ctx.guild.voice_client.disconnect()
    embed=discord.Embed(title=f"Requested by {ctx.author.name}",description=f"Comet left {ctx.message.author.voice.channel}.", color=0xe29797)
    embed.set_author(name="Comet VC")
    if musicCommand == True:
      print('Dialogue Skipped')
    else:
      await ctx.reply(embed=embed)
  else:
    if musicCommand == True:
      print('Dialogue Skipped')
    else:
      await ctx.send("Im not in a voice channel.")

@client.command(pass_context = True, aliases=['stop'])
async def pause(ctx):
  voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
  if voice.is_playing():
    embed=discord.Embed(title="Music Paused", color=0x2432ff)
    embed.set_author(name="Comet Music Player")
    await ctx.reply(embed=embed)
    voice.pause()
  else:
    await ctx.send("No audio is playing in the voice channel at the moment!")

@client.command(pass_context = True)
async def resume(ctx): 
  voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
  if voice.is_paused():
    embed=discord.Embed(title="Music Resumed", color=0xff2600)
    embed.set_author(name="Comet Music Player")
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
  randomquestions = ['When will you see them again?','What do you do to get rid of stress?','What is something you are obsessed with?','What three words best describe you?','What would be your perfect weekend?','What’s your favorite number? Why?','What are you going to do this weekend?','What’s the most useful thing you own?','What’s your favorite way to waste time?','What do you think of tattoos? Do you have any?',' Do you have any pets? What are their names?','What did you do last weekend?','What is something popular now that annoys you?','What did you do on your last vacation?','What’s the best / worst thing about your work/school?','If you had intro music, what song would it be? Why?','What were you really into, other than Annette, when you were a kid?','If you opened a business, what kind of business would it be?','Have you ever given a presentation in front of a large group of people? How did it go?','What is the strangest dream you have ever had?','What is a controversial opinion you have?','Who in your life brings you the most joy?',' Who had the biggest impact on the person you have become?',' What is the most annoying habit someone can have?','Where is the most beautiful place you have been?',' Where do you spend most of your free time/day?','Who was your best friend in elementary school?','How often do you stay up past 3 a.m.?','What is the worst fucking animal?','Which recent news story is the most interesting?','Where is the worst place you have been stuck for a long time?',' If you had to change your name, what would your new name be?','What is something that really annoys you but doesn’t bother most people?','What word or saying from the past do you think should come back?',' If you could learn the answer to one question about your future, what would the question be?','Has anyone ever saved your life?','What benefit do you bring to the group when you hang out with friends? It’s none, isn’t that right, Chris?','What trends did you follow when you were younger?','What do you fear is hiding in the dark?','What year did you peak?? What do you think will be the best period of your entire life?','What is the silliest fear you have?','What are some things you want to accomplish before you die?','What smell brings back great memories?','What are you best at?','What makes you nervous?','What weird/useless talent do you have?','What was the best birthday wish or gift you’ve ever received?','What cartoons did you watch as a child?','What’s the funniest TV series you have seen?',' If you could bring back one TV show that was canceled, which one would you bring back?','What’s your favorite genre of movie?','Which do you prefer? The Office? Or Friends :face_vomiting:??','What’s the worst movie you have seen ','Do you like horror movies? Why or why not?','When was the last time you went to a movie theater?',' What was the last song you listened to?','Do you like classical music?','Are there any songs that always bring a tear to your eye?','Which do you prefer, popular music or relatively unknown music?','What are the three best apps on your phone?','How many apps do you have on your phone?','An app mysteriously appears on your phone that does something amazing. What does it do?', 'How often do you check your phone?','What do you wish your phone could do?','Why does anybody still buy Apple products? Why don’t more people realize Apple has what’s called “planned obsolescence”?', 'What is the most annoying thing about your phone?','How do you feel if you accidentally leave your phone at home?','Who are some of your favorite athletes?','Which sports do you like to play','What is the hardest sport to excel at?','What is the fanciest restaurant you have eaten at?','What is the worst restaurant you have ever eaten at?',' If you opened a restaurant, what kind of food would you serve?',' What is the most disgusting thing you have heard happened at a restaurant?','Where would you like to travel next?','What is the longest plane trip you have taken?','Have you traveled to any different countries? Which ones?','What is the worst hotel you have stayed at? How about the best hotel?','Will technology save the human race or destroy it?','What sci-fi movie or book would you like the future to be like?','What is your favorite shirt?','What is a fashion trend you are really glad went away?','What is/was your favorite pair of shoes?','What personal goals do you have?',' What do you like to do during summer?',' What’s the best thing to do on a cold winter day?','What is your favorite thing to eat or drink in winter?','What is your favorite holiday?','If you had to get rid of a holiday, which would you get rid of? Why?','What is your favorite type of food?','What foods do you absolutely hate?','What food looks disgusting but tastes delicious?',' If your life was a meal, what kind of meal would it be?','What would you want your last meal to be if you were on death row?', 'What is the spiciest thing you have ever eaten?',' You find a remote that can rewind, fast forward, stop, and start time. What do you do with it?','What word do you always mispronounce?','If you had a giraffe that you needed to hide, where would you hide it?','What was the scariest movie you’ve seen?','What is your stance on floorboards?','When you scream into the void, does it answer with jazz?','H̵́́o̷̒͘w̴̷̆͗͋̒d̸͌͆ò̶͝ ̶̄̈ẏ̸̃o̸̖͆u̶̾̓ ̶̅͛e̵̍́s̵̓́c̴̎̚a̸͗̑p̴̦͝é̷̉?̸̉̏','When the time comes, will you jump?','What is your favorite video game?','Other than anime, what is your favorite medium?','Do you ever wonder, and then you stop?','Look into my eyes. What do you see?','When the clock ends, the countdown begins.','How many people have you inadvertently killed? 0? 1? 5?',':trans:',':copyright: 2021 Emmanuel.','According to all known laws of aviation,there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway, because bees don\'t care what humans think is impossible.','Try redoing the command. It did not run correctly. Were I Emmanuel, I would tell you to do it again. But for a bot, that doesn’t make much sense, I think.','Hello, learned and astonishingly attractive pupils. My name is John Green and I want to welcome you to Crash Course World History.','That would be funny, I think.','Tyklo jedno w glowie mam...',' Do YOU see Swiper?','Ayo anybody else down bad?','This ni99a out here tryna cop a fit :laughing:','Devnote #19: Nobody has figured out just how many of the topic questions are literally just memes; at least, not yet.','What is your favorite shade of piss? Favorite taste?','If someone pushed you off a building, would you enjoy it?','Where is a good place to hide a deceased friend of yours? Who would you hang out with?','What celebrity has the most fashionable feet pics?','Time, Doctor Freeman? Is it really that time again?','What is the answer to the riddle of the rocks?','When I say “run”, what do you think of doing?','Giraffes are like airline food. What’s the deal with them? Do you agree?','What’s the deal with airline food?','Which is more anticipated? Jojo Season 6: Stone Ocean? Or Half-Life 3?','Deja vu! I’ve just been to this place before, higher up the beat but I know it’s my time to go-o!','Get your credit card, if you wanna see me','Who is your favorite Tom Brady?','Have you watched “The Burdening of Will Montgomery”?','Who made the sky? Was it me?','You may consume three beans, but no more. They will know if you consume more.','They surpass me, for I cannot tessellate.','Did you change your diaper today?','Annette, please, this isn\'t a joke, come out here to California. I\'m sorry.','Do you fucking want me to go back to how I used to be? How you take fucking advantage of how nice I am now?','Why are you so lazy?','When will you decide to get off your ass for once?','How often do you use reddit?','Who is your crush?','Do you have a brother named Alec?','Do you have a sister named Juliana?','Who has the largest cock?','Do women exist? Do birds?','Why are so many of these questions so worthless?', 'In your opinion, how much faster should the server completely descend into sarcasm?', 'There’s no message to snipe buddy.', '^', 'Who has touched you the most? Physically? Metaphysically?','What do you do with it?', 'Who will win the race?','Who really gets you going?', 'Isn\’t it usually noon by now?', 'Where are your parents?', 'Today I will affect the trout population.','Today I will drive the trout population extinct.', 'Today I will leave the trout population unchanged.', 'All we had to do was follow the damn train, <@438154309872386068>', 'Did you know? Garen\’s real name is Jetsiky. Allegedly.', 'What word or phrase, like “causality” or “vernacular” or “in any case” do you try to use in more sentences than you probably should?', 'Dev Note#2: The creator is too lazy to add sex bot.', 'Dev note #4: guacamole ___ penis', 'Guys Ik Char\’s crush. It\’s: ____', 'Dev Note #3: I don’t care what any of them say. The N-Word will never be funny.',  'Isn’t it usually noon by now?', 'My favorites are green and purple strictly non-convex polyhedra. What about you?', 'My email is emmanuel@aol.com. Dont judge, it\’s from 2003.', 'What are the worst fanbases?', 'Y’know how some days you just feel baggier than a nutsack?', 'What did you want to be when you grew up when you were 5? How about when you were 6? 7? 8? 9? 10? 11? What made you change your plans so often?', 'What were your parents doing during 9/11?', 'Where do you see yourself in 24 hours?', 'If you could choose only one type of boots to wear for the rest of your life, why would it be Uggs?', 'What combination of Nike shoes and socks do you most frequently wear between the months of December and April?', 'How old is your sister?', 'By any chance, do you know of any elementary schools within 500 meters?', 'Where is your family now?', 'In your time of need, where was everybody?', 'How will you be judged?', 'Where is your solace?', 'Excuse my ignorance, but what exactly is moss?', 'Object, dost thou observe time in the past or present?', 'When comes after this? What discord server will be next?', 'yo\’re*', 'Marlon was here', 'Who is your least favorite person?', 'What part of a kid’s movie completely scarred you?', 'Toilet paper, over or under?', 'Toilet paper, over or under?','Where is the weirdest place you\’ve ever shat in?', 'I drink to forget.', 'Hey baby, come back to my place and I\’ll show you ______', '______ really gets me going', 'May the ______ be with you.', 'Everyone in this server is Naturally Intelligent, Gorgeous, Generous, Exemplary, & Radiant!', 'MAGA! Just kidding, I\’m not a cultist.','Should we normalize watching adult content with our parents?', 'You guys really need to find your own things to talk about, but I\’ll help you get started. What the fuck is cheese?', 'https://mee6.xyz/leaderboard/736621294350499931','No topic could be generated. Please try again!','Avery stop stalking Annette lmao you don\’t even know her.', 'The G-Man provides a Xen sample. What do you do?', 'Dev note #6: the warning system took a whole week to make, only for it to not be used :neutral_face:', 'Mention the person with the least friends. Chris does not count.', 'I\’m not like other girls!','GO fuck yourself <@542494714478460956>.']
  await ctx.channel.send(f'{random.choice(randomquestions)}')

@client.command(aliases=['gareb', 'garen',])
@commands.cooldown(1, 10, commands.BucketType.user)
async def garebmomen(ctx):
  garebgif = ['https://giphy.com/gifs/moment-garen-6mUigoKNZskgyYpzjw','https://tenor.com/view/cat-spin-gif-19628827', 'https://tenor.com/view/deffi-pegou-garen-demacia-twirling-spinning-fujiwara-gif-17776151']
  await ctx.channel.send(f'{random.choice(garebgif)}')

@client.command(aliases = ['edga', 'ed', 'edgar'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def edgarmomen(ctx):
  edgagif = ['https://giphy.com/gifs/i-love-you-edgar-qu7EeVd5LK3s3slvyv', 'https://tenor.com/view/edgar-come-back-girl-crying-window-gif-12404499', 'https://tenor.com/view/eggdar-gif-19467171', 'https://tenor.com/view/hellevator-game-show-edgar-get-him-crazy-gif-6169730', 'https://tenor.com/view/vfht-gifsbyme-gifsbydivinity-chippy-the-dog-birthday-gif-16097911']
  await ctx.channel.send(f'{random.choice(edgagif)}')

@client.command(aliases=['E man', 'Eman','Emmanuel','emmanuel'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def eman(ctx):
  randomEman = ['https://giphy.com/gifs/gay-emmanuel-L8haSJadlzRrT5UP92',
    'https://tenor.com/view/emmanuel-zavala-cod-pp-small-cod-heck-fuck-bitch-gif-20893989',
    'https://tenor.com/view/discord-emanuel-emmanuel-baseball-champ-gif-20154485']
  await ctx.channel.send(f'{random.choice(randomEman)}')

@client.command(aliases=['av', 'Avery','avery'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def aversmomen(ctx):
  avbgif = ['https://tenor.com/view/redneck-country-no-nope-gif-4614286','https://tenor.com/view/yes-baby-goal-funny-face-celebrate-gif-16848638', 'https://tenor.com/view/avery-astra-valorant-chair-guyinthechair-gif-20760456', 'https://tenor.com/view/avery-raffy-rafael-devers-red-sox-gif-18741127', 'https://tenor.com/view/jackson-avery-greys-stephanieedwards-couples-gif-12262978','https://tenor.com/view/jackson-avery-greys-stephanieedwards-couples-gif-12262978', 'https://tenor.com/view/avery-worm-funny-gif-18294107', 'https://media.discordapp.net/attachments/686294287851323433/821635269266243584/avery.gif', 'https://tenor.com/view/avery-gif-19302101', '/home/runner/Comet/weirdVidsOfEvery1/averyVid1.mp4']
  
  AveryThingToShow = random.choice(avbgif)
  
  check = os.path.isfile(AveryThingToShow)
  print(check)
  if check == False:
    await ctx.channel.send(f'{AveryThingToShow}')
  else:
    await ctx.send(file=discord.File(AveryThingToShow))

@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.channel)
async def dominic(ctx, **kwargs):
  dominicThings =['/home/runner/Comet/weirdVidsOfEvery1/DomVid1.mov',
    'https://tenor.com/view/dominic-gif-19894253',
    'https://tenor.com/view/yukari-takeba-gif-19575308']

  DominicThingToShow = random.choice(dominicThings)
  
  check = os.path.isfile(DominicThingToShow)
  
  if check == False:
    await ctx.channel.send(f'{DominicThingToShow}')
  else:
    await ctx.send(file=discord.File(DominicThingToShow))

@client.command(pass_context=True)
async def domo(ctx):
  await ctx.send(file=discord.File('/home/runner/Comet/weirdVidsOfEvery1/DomVid1.mov'))

@client.command(pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.channel)
async def marlon(ctx, **kwargs):
  await ctx.send(file=discord.File('/home/runner/Comet/weirdVidsOfEvery1/weirdMarlonVid.mp4'))

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

@client.command(aliases=['tts','say'], help='TTS Command')
async def repeat(ctx, *, text=None):
    # USE GOOGLETRANS V 3.1.0a0
    # To install it use pip3 install googletrans==3.1.0a0
    # Poetry doesn't have 3.1.0a0 if you use Replit

    if not text:
        # We have nothing to speak
        await ctx.send(f"Hey {ctx.author.mention}, I need to know what to say please.")
        return
    embed=discord.Embed(title="TTS Options", description="React to this message to choose a language. You have 5 seconds.", color=0x00ffee)
    embed.set_thumbnail(url="https://img.icons8.com/dusk/452/audio-wave-2.png")
    embed.add_field(name="Spanish", value="👍", inline=False)
    embed.add_field(name="Armenian", value="🌕", inline=False)
    embed.add_field(name="English", value="🔅", inline=False)
    embed.add_field(name='Korean', value='✨', inline=False)
    embed.add_field(name='Filipino', value='🌜', inline=False)
    embed.set_footer(text="Comet Alert")
    embed1 = await ctx.send(embed=embed)
    await embed1.add_reaction('👍')
    await embed1.add_reaction('🌕')
    await embed1.add_reaction('🔅')
    await embed1.add_reaction('✨')
    await embed1.add_reaction('🌜')

    def check(reaction, user):
      return user == ctx.author and (str(reaction.emoji) == '👍' or str(reaction.emoji) == '🔅' or str(reaction.emoji) == '🌕' or str(reaction.emoji) == '✨' or str(reaction.emoji) == '🌜')

    try:
      reaction, user = await client.wait_for('reaction_add', timeout=3.5, check=check)

      if str(reaction.emoji) == '👍':
        translator = Translator()
        result = translator.translate(text, dest='es')
        print(result.text)
        language = 'es'
      elif str(reaction.emoji) == '🌕':
        translator = Translator()
        result = translator.translate(text, dest='hy')
        language = 'hy'
      elif str(reaction.emoji) == '🔅':
        translator = Translator()
        result = translator.translate(text, dest='en')
        language = 'en'
      elif str(reaction.emoji) == '✨':
        translator = Translator()
        result = translator.translate(text, dest='ko')
        language = 'ko'
      elif str(reaction.emoji) == '🌜':
        translator = Translator()
        result = translator.translate(text, dest='tl')
        language = 'tl'
      else:
        await ctx.send('Defaulted to English')
        translator = Translator()
        language = 'en'
      
    except asyncio.TimeoutError:
      await ctx.send('Defaulted to English')
      language = 'en'
    
    voice2 = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice2 == None:
      channel = ctx.message.author.voice.channel
      voice = await channel.connect()
    else:
      print('hello')

    # Lets prepare our text, and then save the audio file
    tts = gTTS(text=result.text, lang=language)
    tts.save("text.mp3")
    embed2=discord.Embed(title="TTS Notification", description="Successfully set up.", color=0x3ce7e4)
    embed2.set_thumbnail(url="https://img.icons8.com/dusk/452/audio-wave-2.png")
    embed2.add_field(name="Text", value=f"{result.text}", inline=True)
    embed2.add_field(name="Language", value=f"{language}", inline=True)
    embed2.set_footer(text="Comet Alert")
    await ctx.send(embed=embed2, delete_after=30)
    
    try:
        # Lets play that mp3 file in the voice channel
        audio_source = discord.FFmpegPCMAudio('text.mp3')
        player = voice.play(audio_source)
        player.play()

    except TypeError as e:
        await ctx.send(f"TypeError exception:\n`{e}`")

@repeat.before_invoke
async def before(message):
  await message.invoke(client.get_command('leave'), musicCommand=True)

@client.command(help="Play with #rps")
async def rps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.send(f"Rock, paper, or scissors? Choose wisely...")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = (await client.wait_for('message', check=check)).content

    comp_choice = random.choice(rpsGame)
    if user_choice == 'rock':
        if comp_choice == 'rock':
            embed=discord.Embed(title="It was a tie", color=0xebee20)
            embed.set_author(name="Tie", icon_url="https://toppng.com/uploads/preview/rock-paper-scissors-circle-11562962494dqcjusyikw.png")
            embed.set_thumbnail(url="https://www.pngkey.com/png/full/87-876078_rock-paper-scissors-vector-rock-paper-scissors-clipart.png")
            embed.add_field(name="Your Choice", value=user_choice, inline=True)
            embed.add_field(name="My Choice", value=comp_choice, inline=True)
            embed.set_footer(text="Comet Game")
            await ctx.send(embed=embed)
        elif comp_choice == 'paper':
            embed=discord.Embed(title=f"{ctx.author.nick} lost", color=0xb30000)
            embed.set_author(name="Comet Won", icon_url="https://toppng.com/uploads/preview/rock-paper-scissors-circle-11562962494dqcjusyikw.png")
            embed.set_thumbnail(url="https://www.pngkey.com/png/full/87-876078_rock-paper-scissors-vector-rock-paper-scissors-clipart.png")
            embed.add_field(name="Your Choice", value=user_choice, inline=True)
            embed.add_field(name="My Choice", value=comp_choice, inline=True)
            embed.set_footer(text="Comet Game")
            await ctx.send(embed=embed)
        elif comp_choice == 'scissors':
            embed=discord.Embed(color=0xa5e199)
            embed.set_author(name=f"{ctx.author.nick} Won", icon_url="https://toppng.com/uploads/preview/rock-paper-scissors-circle-11562962494dqcjusyikw.png")
            embed.set_thumbnail(url="https://www.pngkey.com/png/full/87-876078_rock-paper-scissors-vector-rock-paper-scissors-clipart.png")
            embed.add_field(name="Your Choice", value=user_choice, inline=True)
            embed.add_field(name="My Choice", value=comp_choice, inline=True)
            embed.set_footer(text="Comet Game")
            await ctx.send(embed=embed)

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            embed=discord.Embed(color=0xa5e199)
            embed.set_author(name=f"{ctx.author.nick} Won", icon_url="https://toppng.com/uploads/preview/rock-paper-scissors-circle-11562962494dqcjusyikw.png")
            embed.set_thumbnail(url="https://www.pngkey.com/png/full/87-876078_rock-paper-scissors-vector-rock-paper-scissors-clipart.png")
            embed.add_field(name="Your Choice", value=user_choice, inline=True)
            embed.add_field(name="My Choice", value=comp_choice, inline=True)
            embed.set_footer(text="Comet Game")
            await ctx.send(embed=embed)
        elif comp_choice == 'paper':
            embed=discord.Embed(title="It was a tie", color=0xebee20)
            embed.set_author(name="Tie", icon_url="https://toppng.com/uploads/preview/rock-paper-scissors-circle-11562962494dqcjusyikw.png")
            embed.set_thumbnail(url="https://www.pngkey.com/png/full/87-876078_rock-paper-scissors-vector-rock-paper-scissors-clipart.png")
            embed.add_field(name="Your Choice", value=user_choice, inline=True)
            embed.add_field(name="My Choice", value=comp_choice, inline=True)
            embed.set_footer(text="Comet Game")
            await ctx.send(embed=embed)
        elif comp_choice == 'scissors':
            embed=discord.Embed(title=f"{ctx.author.nick} lost", color=0xb30000)
            embed.set_author(name="Comet Won", icon_url="https://toppng.com/uploads/preview/rock-paper-scissors-circle-11562962494dqcjusyikw.png")
            embed.set_thumbnail(url="https://www.pngkey.com/png/full/87-876078_rock-paper-scissors-vector-rock-paper-scissors-clipart.png")
            embed.add_field(name="Your Choice", value=user_choice, inline=True)
            embed.add_field(name="My Choice", value=comp_choice, inline=True)
            embed.set_footer(text="Comet Game")
            await ctx.send(embed=embed)

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            embed=discord.Embed(title=f"{ctx.author.nick} lost", color=0xb30000)
            embed.set_author(name="Comet Won", icon_url="https://toppng.com/uploads/preview/rock-paper-scissors-circle-11562962494dqcjusyikw.png")
            embed.set_thumbnail(url="https://www.pngkey.com/png/full/87-876078_rock-paper-scissors-vector-rock-paper-scissors-clipart.png")
            embed.add_field(name="Your Choice", value=user_choice, inline=True)
            embed.add_field(name="My Choice", value=comp_choice, inline=True)
            embed.set_footer(text="Comet Game")
            await ctx.send(embed=embed)
        elif comp_choice == 'paper':
            embed=discord.Embed(color=0xa5e199)
            embed.set_author(name=f"{ctx.author.nick} Won", icon_url="https://toppng.com/uploads/preview/rock-paper-scissors-circle-11562962494dqcjusyikw.png")
            embed.set_thumbnail(url="https://www.pngkey.com/png/full/87-876078_rock-paper-scissors-vector-rock-paper-scissors-clipart.png")
            embed.add_field(name="Your Choice", value=user_choice, inline=True)
            embed.add_field(name="My Choice", value=comp_choice, inline=True)
            embed.set_footer(text="Comet Game")
            await ctx.send(embed=embed)
        elif comp_choice == 'scissors':
            embed=discord.Embed(title="It was a tie", color=0xebee20)
            embed.set_author(name="Tie", icon_url="https://toppng.com/uploads/preview/rock-paper-scissors-circle-11562962494dqcjusyikw.png")
            embed.set_thumbnail(url="https://www.pngkey.com/png/full/87-876078_rock-paper-scissors-vector-rock-paper-scissors-clipart.png")
            embed.add_field(name="Your Choice", value=user_choice, inline=True)
            embed.add_field(name="My Choice", value=comp_choice, inline=True)
            embed.set_footer(text="Comet Game")
            await ctx.send(embed=embed)


# All the error handles
@questions.error
async def topic_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = 'Wait **{:.2f}** seconds to get a new topic.'.format(error.retry_after)
    embed=discord.Embed(title="Command On Cooldown", description=msg, color=0x2723fb)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/plantsvszombies/images/c/c7/Time_Traveler2.png/revision/latest?cb=20200317010014")
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
  else:
    raise error

@snipe.error
async def snipe_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = 'Wait **{:.2f}** seconds to snipe again.'.format(error.retry_after)
    embed=discord.Embed(title="Command On Cooldown", description=msg, color=0x2723fb)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/plantsvszombies/images/c/c7/Time_Traveler2.png/revision/latest?cb=20200317010014")
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
  else:
    raise error

@char.error
async def char_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = 'Wait **{:.2f}** seconds before admiring our lovely queen <@247163608700682240> again.'.format(error.retry_after)
    embed=discord.Embed(title="Command On Cooldown", description=msg, color=0x2723fb)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/plantsvszombies/images/c/c7/Time_Traveler2.png/revision/latest?cb=20200317010014")
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
  else:
    raise error

@eman.error
async def eman_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = 'Wait **{:.2f}** seconds before using <@588931051103977494>\'s command again.'.format(error.retry_after)
    embed=discord.Embed(title="Command On Cooldown", description=msg, color=0x2723fb)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/plantsvszombies/images/c/c7/Time_Traveler2.png/revision/latest?cb=20200317010014")
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
  else:
    raise error

@makeZalgo.error
async def zalgo_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = 'Wait **{:.2f}** seconds before creating more z̷̠͒a̡ͨ͞l̴ͬͫg̷̏͘ǫ̫͎ ṱ̷̳e̸̸͍x̢̾̇t̵̥͞.'.format(error.retry_after)
    embed=discord.Embed(title="Command On Cooldown", description=msg, color=0x2723fb)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/plantsvszombies/images/c/c7/Time_Traveler2.png/revision/latest?cb=20200317010014")
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
  else:
    raise error

@steven.error
async def steven_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = 'Wait **{:.2f}** seconds before using <@455981136724754432>\'s <:steven:753085273084133407> command again.'.format(error.retry_after)
    embed=discord.Embed(title="Command On Cooldown", description=msg, color=0x2723fb)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/plantsvszombies/images/c/c7/Time_Traveler2.png/revision/latest?cb=20200317010014")
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
  else:
    raise error

@weatherReport.error
async def weather_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = 'Weather Report is on cooldown. Try again in **{:.2f}** seconds.'.format(error.retry_after)
    embed=discord.Embed(title="Command On Cooldown", description=msg, color=0x2723fb)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/plantsvszombies/images/c/c7/Time_Traveler2.png/revision/latest?cb=20200317010014")
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
  else:
    raise error

@dead.error
async def dead_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = 'Please wait another **{:.2f}** seconds before reminding us the server/chat is dead.'.format(error.retry_after)
    embed=discord.Embed(title="Command On Cooldown", description=msg, color=0x2723fb)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/plantsvszombies/images/c/c7/Time_Traveler2.png/revision/latest?cb=20200317010014")
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
  else:
    raise error

@beg.error
async def beg_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = 'Please wait another **{:.2f}** seconds before begging again.'.format(error.retry_after)
    embed=discord.Embed(title="Command On Cooldown", description=msg, color=0x2723fb)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/plantsvszombies/images/c/c7/Time_Traveler2.png/revision/latest?cb=20200317010014")
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
  else:
    raise error

@rob.error
async def rob_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = 'Please wait another **{:.2f}** seconds before robbing again.'.format(error.retry_after)
    embed=discord.Embed(title="Command On Cooldown", description=msg, color=0x2723fb)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/plantsvszombies/images/c/c7/Time_Traveler2.png/revision/latest?cb=20200317010014")
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
  else:
    raise error

@shoot.error
async def shoot_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = 'Please wait another **{:.2f}** seconds before shoting people again.'.format(error.retry_after)
    embed=discord.Embed(title="Command On Cooldown", description=msg, color=0x2723fb)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/plantsvszombies/images/c/c7/Time_Traveler2.png/revision/latest?cb=20200317010014")
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
  else:
    raise error

@addWord.error
async def addWordError(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    ctx.channel.purge(limit=1)
    embed=discord.Embed(title="Permission Denied", description="You don't have the permissions to run the command.", color=0xff0000)
    embed.set_author(name="STOP", icon_url="https://images.vexels.com/media/users/3/193117/isolated/preview/391dc07c463639a67dcb5d471d068bff-stop-covid-badge-by-vexels.png")
    embed.set_thumbnail(url="https://images.vexels.com/media/users/3/136933/isolated/preview/12e4ab9fce4498ed36b9f1d162678300-stop-button-icon-by-vexels.png")
    embed.add_field(name="People who have permissions to run it:", value="Mods", inline=False)
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
  else:
    raise error

@removeWord.error
async def removeWordError(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    ctx.channel.purge(limit=1)
    embed=discord.Embed(title="Permission Denied", description="You don't have the permissions to run the command.", color=0xff0000)
    embed.set_author(name="STOP", icon_url="https://images.vexels.com/media/users/3/193117/isolated/preview/391dc07c463639a67dcb5d471d068bff-stop-covid-badge-by-vexels.png")
    embed.set_thumbnail(url="https://images.vexels.com/media/users/3/136933/isolated/preview/12e4ab9fce4498ed36b9f1d162678300-stop-button-icon-by-vexels.png")
    embed.add_field(name="People who have permissions to run it:", value="Mods", inline=False)
    embed.set_footer(text="Comet Alert")
    await ctx.send(embed=embed, delete_after=10)
  else:
    raise error

TOKEN = os.getenv('token')
dontDieOnMe()
client.run(TOKEN)