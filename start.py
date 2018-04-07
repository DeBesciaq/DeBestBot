import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

def log(command, author_name, author_mention):
    x = str(author_name)
    y = str(author_mention)
    print("------")
    print("Komenda: "+command)
    print("Użytkownik: "+x+", "+y)
    print("------")

bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    print("Bot jest Online!")
    print("Name: %s" % (bot.user.name))
    print("ID: %s" % (bot.user.id))


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong!")
    log("ping", ctx.message.author, ctx.message.author.mention)


@bot.command(pass_context=True)
async def jebac(ctx, user: discord.Member):
    await bot.say("**Jebac cie %s**" % (user.name))
    print("------")
    print("Komenda: jebac")
    print("Użytkownik: "+ctx.message.author.mention)
    print("------")
    log("jebac", ctx.message.author, ctx.message.author.mention)


@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    embed = discord.Embed(title="Avatar użytkownika %s:" % (user.name), url=user.avatar_url, color=0x42ebf4)
    embed.set_image(url=user.avatar_url)
    await bot.say(embed=embed)
    log("avatar", ctx.message.author, ctx.message.author.mention)


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    y = str(user.status)
    if y == "online":
        x = "Dostępny"
    elif y == "offline":
        x = "Niewidoczny"
    elif y == "dnd":
        x = "Nie przeszkadzać"
    elif y == "idle":
        x = "Zaraz wracam"

    embed = discord.Embed(title="Info użytkownika %s" % (user.name), color=0x42ebf4)
    embed.add_field(name="Nick", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=x, inline=True)
    embed.add_field(name="Rola", value=user.top_role)
    embed.add_field(name="Dołączył/a", value=user.joined_at.strftime("%d.%m.%Y %H:%M"))
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    log("info", ctx.message.author, ctx.message.author.mention)


@bot.command(pass_context=True)
async def channelid(ctx, channel: discord.Channel):
    embed = discord.Embed(title="ID kanału " + channel.name, description=channel.id,color=0x42ebf4)
    await bot.say(embed=embed)
    log("channelid", ctx.message.author, ctx.message.author.mention)


@bot.command(pass_context=True)
async def gra(ctx, arg):
    author = ctx.message.author
    if arg == "lol":
        role = discord.utils.get(ctx.message.server.roles, name="LoL")
        await bot.add_roles(author, role)
    if arg == "cs:go":
        role = discord.utils.get(ctx.message.server.roles, name="CS:GO")
        await bot.add_roles(author, role)
    if arg == "mc":
        role = discord.utils.get(ctx.message.server.roles, name="MC")
        await bot.add_roles(author, role)
    if arg == "list":
        embed = discord.Embed(title="Dostępne Rangi", color=0x42ebf4)
        embed.add_field(name="League of Legends", value="Argument: lol", inline=False)
        embed.add_field(name="Counter-Strike: Global Offensive", value="Argument: cs:go", inline=False)
        embed.add_field(name="Minecraft", value="Argument: mc", inline=False)
        embed.add_field(name="Przykładowe użycie:", value=".gra lol", inline=False)
        await bot.say(embed=embed)
    else:
        await bot.say("Podaj poprawną nazwę rangi. Aby sprawdzić dostępne wpisz .gra list ;D")

@bot.command(pass_context=True)
async def komendy(ctx):
    embed = discord.Embed(title="Dostępne komendy", description="-----------", color=0x42ebf4)
    embed.add_field(name="ping", value="Sprawdza reakcję bota", inline=False)
    embed.add_field(name="info", value="Wyświetla informacje o danym użytkowiniku", inline=False)
    embed.add_field(name="avatar", value="Wyświetla zdjęcie profilowe danego użytkownika", inline=False)
    embed.add_field(name="jebac", value="Najlepiej wpisać nick Lethrilla ;D", inline=False)
    embed.add_field(name="komendy", value="Wyświetla dostępne komendy", inline=False)
    embed.add_field(name="channelid", value="Sprawdza Indentyfikator wskazanego kanału", inline=False)
    await bot.say(embed=embed)
    log("komendy", ctx.message.author, ctx.message.author.mention)


@channelid.error
async def channelid_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="ID kanału "+ctx.message.channel.name, description=ctx.message.channel.id, color=0x42ebf4)
        await bot.say(embed=embed)
    log("channelid", ctx.message.author, ctx.message.author.mention)


@gra.error
async def gra_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await bot.say("Podaj poprawną nazwę rangi. Aby sprawdzić dostępne wpisz .gra list ;D")

bot.run("MzcyMDQ3OTcyOTQ0NTc2NTEz.DalaSw.uKGDKB5MTolbfuez7YuSsUArZzU")
