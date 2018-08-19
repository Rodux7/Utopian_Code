# Imports
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from beem.account import Account

# Variables
bot = commands.Bot(command_prefix="!")

# Print When Ready
@bot.event
async def on_ready():
	print("I am ready!")
	
# Commands
# Reputation Command
@bot.command(pass_context=True)
async def rep(ctx, username):
  acc = Account(username.lower())
  rep = acc.rep
  embed = discord.Embed(title=("DiscordSteem"), description=("Reputation of %s is %s" % (username, rep)))
  await bot.say(embed=embed)

# Blog Command
@bot.command(pass_context=True)
async def blog(ctx, username):
  acc = Account(username.lower())
  for post in acc.blog_history(limit=5, reblogs=False):
    embed = discord.Embed(title=(post["title"]), color=(0x00ff00))
    await bot.say(embed=embed)

# Feed Command    
@bot.command(pass_context=True)
async def feed(ctx, username):
  acc = Account(username.lower())
  for post in acc.feed_history(limit=5):
    embed = discord.Embed(title=(post["title"]), description=("By " + post["author"]),color=(0x00ff00))
    await bot.say(embed=embed)

# Comments Command    
@bot.command(pass_context=True)
async def comments(ctx, username):
  acc = Account(username.lower())
  for post in acc.comment_history(limit=5):
    embed = discord.Embed(description=(post["body"]),color=(0x00ff00))
    await bot.say(embed=embed)   

# Run The Bot
bot.run("TOKEN")
bot.close()
