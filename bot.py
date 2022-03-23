import discord
from discord.ext import commands #чтобы легче управлять ботом

bot = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

@bot.command(aliases = ['пинг'])
async def ping(ctx):
    await ctx.send('pong!')

@bot.command(aliases = ['тарас'])
async def taras(ctx):
    await ctx.send('Хохол))')

@bot.event 
async def on_ready():
    print('I\'m connected!')

@bot.event 
async def on_message_edit(before, after):
    if before.content == after.content:
        return
    await before.channel.send(f'Сообщение было изменено!\n{before.content} -> {after.content}')

bot.run('OTU1MTgzOTE2NzcwMjc1NDE5.Yjd-WA.2vNxxDTJU7_0vyEwbKx58-dIcYo')