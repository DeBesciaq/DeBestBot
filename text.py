import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


bot = commands.Bot(command_prefix='.')


while True:
    x = str(input())
    await bot.say(x)
