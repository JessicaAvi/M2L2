
with open('text.txt', 'w', encoding='utf-8') as f:
    print(f.write("Book"))

    import discord
from discord.ext import commands
import os
import random


intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)


#PILIH SAMPAH
organik = ["buah-buahan", "kotoran hewan", "sisa makanan", "sayur-sayuran", "minyak bekas", "air cucian beras", "dedaunan kering", "ranting pohon", "kayu", "kertas", "rotan", "bambu"]
anorganik = ["plastik", "botol / kaleng minuman", "kresek", "ban bekas", "besi", "kaca", "kabel", "barang elektronik", "bohlam lampu"]

@bot.command()
async def pilih_sampah(ctx):
      await ctx.send("Masukkan jenis sampah: ")
      msg = await bot.wait_for("message")
      if msg.content in organik:
        await ctx.send("Buang ke tempat sampah organik")
      elif msg.content in anorganik:
        await ctx.send("Buang ke tempat sampah anorganik")  

bot.run("MTIxODQxNjQ2MTk1ODIyMTg2OA.GjrMua.-92A954P7NwybqNz61vK1HmZ0KM6gYG5h4x2XU")
  