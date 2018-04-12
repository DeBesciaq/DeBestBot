import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


def log(command, author_name, author_mention):
    x = str(author_name)
    y = str(author_mention)
    print("------")
    print("Komenda: "+command)
    print("Uzytkownik: "+x+", "+y)
    print("------")

bot = commands.Bot()


while True:
    x = str(input())
    await bot.say(x)
