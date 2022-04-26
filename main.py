from discord.ext.commands.core import command
import requests
import time
import asyncio
import discord
from discord.ext import commands
import random
from discord.ext import tasks, commands
import asyncio
from discord_webhook import DiscordWebhook
import os
import json
from discord.ext.commands import BucketType, Cooldown
import threading
from colorama import Fore,Style,Back

color = 7419530


TOKEN = "Bot Token"
bots_channel = 
LogsChannel = 

friendqueue = []

intents = discord.Intents().all()
ice = commands.Bot(command_prefix=".",intents=intents, case_insensitive=True)
ice.remove_command('help')


@ice.event 
async def on_ready():
  print(f'Bot Online')
  await ice.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name="JAD'S FREIND BOTTER"))




@tasks.loop(seconds=5)
async def friender():
  r = open('tokens.txt', 'r')
  r2 = r.readlines()
  a = (random.choice(r2))
  b = a.strip('\n')
  headers = {
    'Authorization': b,
  }
  if len(friendqueue) == 0:
    pass
  else:
    userFetch = await ice.fetch_user(friendqueue[0])
    if isinstance(userFetch,str):
      print('Friend is string')
    else:
      friendname = userFetch.name
      friendtag = userFetch.discriminator
      payload = {"username": friendname,"discriminator": friendtag}

      r = requests.post('https://discord.com/api/v9/users/@me/relationships',headers=headers,json=payload)
      if r.status_code == 80000 or r.status_code == 400:
        channelGet = ice.get_channel(LogsChannel)
        embed = discord.Embed(title='Friend Requests Disabled!', description=f'Enable your friend requests, {str(userFetch.name) + str("#") + str(userFetch.discriminator)}',color=color)
        await channelGet.send(embed=embed)
        await channelGet.send(userFetch.mention)
        friendqueue.pop(0)
      elif r.status_code == 204:
        channelGet = ice.get_channel(LogsChannel)
        embed = discord.Embed(title='Sent Friend Requests', description=f'Successfully sent friend request to {userFetch.id}',color=color)
        await channelGet.send(embed=embed)
        friendqueue.pop(0)
      else:
        channelGet = ice.get_channel(LogsChannel)
        embed = discord.Embed(title='Error! ', description=f'Token: ---------------------\nStatus Code: {r.status_code}\n\nThis token is not working!',color=color)
        await channelGet.send(embed=embed)
        friendqueue.pop(0)
  
friender.start()

@ice.command()
async def friend(ctx, id):
  if ctx.channel.id != bots_channel:
    embed = discord.Embed(
      title="You can't use this command here",
      description='You must use this command in <#942435070235512922> ',
      color=color
    ) 
    a = await ctx.send(embed=embed)
    await asyncio.sleep(3)
    await a.delete()
  else:
      silverRole = discord.utils.get(ctx.guild.roles,id=963091764883910697)
      BronzeRole = discord.utils.get(ctx.guild.roles,id=963091768121901137)
      GoldRole = discord.utils.get(ctx.guild.roles,id=963091771217305610)
      PremiumRole = discord.utils.get(ctx.guild.roles,id=963091774350450729)
      if silverRole in ctx.author.roles:
        embed = discord.Embed(title='Sending Friend Requests', description=f'Sent 5 Friend Request To {id}', color=color)
        await ctx.send(embed=embed)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
      elif BronzeRole in ctx.author.roles:
        embed = discord.Embed(title='Sending Friend Requests', description=f'Sent 3 Friend Request To {id}', color=color)
        await ctx.send(embed=embed)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
      elif GoldRole in ctx.author.roles:
        embed = discord.Embed(title='Sending Friend Requests', description=f'Sent 10 Friend Request To {id}', color=color)
        await ctx.send(embed=embed)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
      elif PremiumRole in ctx.author.roles:
        embed = discord.Embed(title='Sending Friend Requests', description=f'Sent 20 Friend Request To {id}', color=color)
        await ctx.send(embed=embed)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
        friendqueue.append(id)
      else:
        embed = discord.Embed(title='Sending Friend Requests', description=f'Sent 2 Friend Request To {id}', color=color)
        await ctx.send(embed=embed)
        friendqueue.append(id)
        friendqueue.append(id)


ice.run(TOKEN)
