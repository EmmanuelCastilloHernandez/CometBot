# This is unused code that may return in the future
from replit import db

# This function is responsible for warning people
@client.command(aliases=['givewarning', 'givewarn'], help='Warn command for mods.', pass_context=True)
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(kick_members=True, administrator=True)
async def warn(ctx, user: discord.Member, *, reason=None):
  userCheck = str(user)
  warning = {f"{user} | {ctx.guild.name}":f"{reason}"}
  admin = get(ctx.guild.roles, name='Admin')
  coolerppl = get(ctx.guild.roles, name='cooler people')
  owner = get(ctx.guild.roles, name='owner')

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