import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


bot = commands.Bot(command_prefix='.')


@bot.command
async def text():
    kanal = bot.get_channel("429594209532772353")
    while True:
        x = str(input())
        await bot.send_message(kanal, x)
