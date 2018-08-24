# Imports
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from beem.account import Account
import json
import requests

# Variables
bot = commands.Bot(command_prefix="!")
notes = {}

# Print When Ready
@bot.event
async def on_ready():
  print("I am ready!")
	
# Commands
@bot.command(pass_context=True)
async def blog(ctx, username, amount=5):
  acc = Account(username.lower())
  embed = discord.Embed(title=("DiscordSteem"), description=("Last %s Posts Of %s" % (amount, username)), color=(0x00ff00))
  embed.set_thumbnail(url=(acc.profile["profile_image"]))
  for post in acc.blog_history(limit=amount, reblogs=False):
    embed.add_field(name=(post["title"]), value=("By " + post["author"]))
  await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def feed(ctx, username, amount=5):
  acc = Account(username.lower())
  embed = discord.Embed(title=("DiscordSteem"), description=("This is the feed of %s" % (username)), color=(0x00ff00))
  embed.set_thumbnail(url=(acc.profile["profile_image"]))
  for post in acc.feed_history(limit=amount):
    embed.add_field(name=(post["title"]), value=("By " + post["author"]))
  await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def comments(ctx, username, amount=5):
  acc = Account(username.lower())
  embed = discord.Embed(title=("DiscordSteem"), description=("These are last %s comments of %s" % (amount, username)), color=(0x00ff00))
  embed.set_thumbnail(url=(acc.profile["profile_image"]))
  for post in acc.comment_history(limit=amount):
    embed.add_field(name=(post["title"]), value=("By " + post["author"]))
  await bot.say(embed=embed)   

@bot.command(pass_context=True)
async def info(ctx, username):
  acc = Account(username.lower())
  embed = discord.Embed(title=(username), description=(acc.profile["about"]), color=(0x00ff00))
  embed.set_thumbnail(url=(acc.profile["profile_image"]))
  embed.add_field(name=("Reputation"), value=(int(acc.rep)))
  embed.add_field(name=("Followers"), value=(len(acc.get_followers())))
  embed.add_field(name=("Accounts Following"), value=(len(acc.get_following())))
  embed.add_field(name=("Number Of Posts"), value=(acc["post_count"]))
  embed.add_field(name=("STEEM Balance"), value=(acc["balance"]))
  embed.add_field(name=("SBD Balance"), value=(acc["sbd_balance"]))
  embed.add_field(name=("Witnesses Voted"), value=(acc["witnesses_voted_for"]))
  await bot.say(embed=embed)   

@bot.command(pass_context=True)
async def ticker(ctx, coin, currency="usd"):
  cur = currency.lower()
  r = requests.get("https://api.coinmarketcap.com/v1/ticker/%s/?convert=%s" % (coin, cur))
  r_json = r.json()
  if type(r_json) is list:
    price = r_json[0].get(("price_" + cur), ("Invalid currency"))
    if price[0] == "I":
    	embed = discord.Embed(title=("DiscordSteem"), description=("Invalid currency"))
    	await bot.say(embed=embed)
    else:
    	embed = discord.Embed(title=("Price Of " + coin.upper()), description=("%.2f %s" % (float(price), cur.upper())))
    	await bot.say(embed=embed)
  else:
  	embed = discord.Embed(title=("DiscordSteem"), description=("Invalid coin"))
  	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def addnote(ctx, note):
  author = ctx.message.author
  if author in notes:
    notes[author] += [note]
    embed = discord.Embed(title="Note Added!", color=0x00ff00)
    await bot.say(embed=embed)
  else:
    notes[author] = [note]
    embed = discord.Embed(title="Note Added!", color=0x00ff00)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def note(ctx):
  author = ctx.message.author
  embed = discord.Embed(title=("DiscordSteem"), description=("Your Notes"), color=0x00ff00, inline=True)
  for note in notes[author]:
    embed.add_field(name=note, value="Note")
  await bot.send_message(author, embed=embed)
	
@bot.command(pass_context=True)
async def delnote(ctx):
  author = ctx.message.author
  del notes[author]
  embed = discord.Embed(title="Notes Deleted!", color=0x00ff00)
  await bot.say(embed=embed)

# Run The Bot
bot.run("TOKEN")
bot.close()
