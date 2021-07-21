
@client.command(aliases=['ssnipe','snipe+'], help='A super snipe command for snitches')
async def SuperSnipe(ctx, *, messageToRetrieve: int=1):
  channel = ctx.channel

  try:
    if messageToRetrieve < 0:
      await ctx.send('***Value too low. TF***')
    if messageToRetrieve == 1:
      embed = discord.Embed(title=f"Page 1: {editMessageAuthor1[channel.id]}", color=0x2f3136)
      embed.set_author(name=f"Super Edit in {channel.name} {messageToRetrieve}")
      embed.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/snipeIcon.png")
      embed.add_field(name='Before:', value=beforeMessage1[channel.id], inline=False)
      embed.add_field(name='After:', value=afterMessage1[channel.id], inline=False)
      embed.set_footer(text=f"Sniper: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    if messageToRetrieve == 2:
      embed = discord.Embed(title=f"Page 1: {editMessageAuthor2[channel.id]}", color=0x2f3136)
      embed.set_author(name=f"Super Edit in {channel.name} {messageToRetrieve}")
      embed.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/snipeIcon.png")
      embed.add_field(name='Before:', value=beforeMessage2[channel.id], inline=False)
      embed.add_field(name='After:', value=afterMessage2[channel.id], inline=False)
      embed.set_footer(text=f"Sniper: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    if messageToRetrieve == 3:
      embed = discord.Embed(title=f"Page 3: {editMessageAuthor3[channel.id]}", color=0x2f3136)
      embed.set_author(name=f"Super Edit in {channel.name} {messageToRetrieve}")
      embed.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/snipeIcon.png")
      embed.add_field(name='Before:', value=beforeMessage3[channel.id], inline=False)
      embed.add_field(name='After:', value=afterMessage3[channel.id], inline=False)
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

        await buttonCheck.respond(content='Changing Super Edit Snipe Page')
        if buttonCheck.component.label == '1':
          embed2 = discord.Embed(title=f"Page 1: {editMessageAuthor1[channel.id]}", color=0x2f3136)
          embed2.set_author(name=f"Super Edit in {channel.name}")
          embed.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/snipeIcon.png")
          embed2.add_field(name='Before:', value=beforeMessage1[channel.id], inline=False)
          embed2.add_field(name='After:', value=afterMessage1[channel.id], inline=False)
          embed2.set_footer(text=f"Sniper: {buttonCheck.user.name}#{buttonCheck.user.discriminator}", icon_url=buttonCheck.user.avatar_url)
          await mg.edit(embed=embed2)
        if buttonCheck.component.label == '2':
          embed2 = discord.Embed(title=f"Page 2: {editMessageAuthor2[channel.id]}", color=0x2f3136)
          embed2.set_author(name=f"Super Edit in {channel.name}")
          embed.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/snipeIcon.png")
          embed2.add_field(name='Before:', value=beforeMessage2[channel.id], inline=False)
          embed2.add_field(name='After:', value=afterMessage2[channel.id], inline=False)
          embed2.set_footer(text=f"Sniper: {buttonCheck.user.name}#{buttonCheck.user.discriminator}", icon_url=buttonCheck.user.avatar_url)
          await mg.edit(embed=embed2)
        if buttonCheck.component.label == '3':
          embed2 = discord.Embed(title=f"Page 3: {editMessageAuthor1[channel.id]}", color=0x2f3136)
          embed2.set_author(name=f"Super Edit in {channel.name} {messageToRetrieve}")
          embed.set_thumbnail(url="https://cometbot.emmanuelch.repl.co/static/photoToRender/snipeIcon.png")
          embed2.add_field(name='Before:', value=beforeMessage3[channel.id], inline=False)
          embed2.add_field(name='After:', value=afterMessage3[channel.id], inline=False)
          embed2.set_footer(text=f"Sniper: {buttonCheck.user.name}#{buttonCheck.user.discriminator}", icon_url=buttonCheck.user.avatar_url)
          await mg.edit(embed=embed2)
      except:
        await mg.edit(content='Memory Cleared: No Retriable messages.')
  except:
    embed=discord.Embed(title=" ", color=0x0603bf)
    embed.set_author(name=f"𝙉𝙤 𝙀𝙣𝙩𝙧𝙞𝙚𝙨 𝙍𝙚𝙘𝙤𝙧𝙙𝙚𝙙, {ctx.author.name}")
    await ctx.send(embed=embed)