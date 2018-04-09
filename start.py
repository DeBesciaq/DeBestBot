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


bot = commands.Bot(command_prefix='.')


#--------------------EVENT--------------------#


@bot.event
async def on_ready():
    print("Bot jest Online!")
    print("Name: %s" % (bot.user.name))
    print("ID: %s" % (bot.user.id))


#--------------------COMMAND--------------------#


@bot.command(pass_context=True)
async def hi(ctx):
    await bot.say("**Siemka %s**" %(ctx.message.author.name))


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong!")
    log("ping", ctx.message.author, ctx.message.author.mention)

    
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    y = str(user.status)
    if y == "online":
        x = "Dostepny"
    elif y == "offline":
        x = "Niewidoczny"
    elif y == "dnd":
        x = "Nie przeszkadzac"
    elif y == "idle":
        x = "Zaraz wracam"

    embed = discord.Embed(title="Info uzytkownika %s" % (user.name), color=0x42ebf4)
    embed.add_field(name="Nick", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=x, inline=True)
    embed.add_field(name="Rola", value=user.top_role)
    embed.add_field(name="Dolaczyl/a", value=user.joined_at.strftime("%d.%m.%Y %H:%M"))
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    log("info", ctx.message.author, ctx.message.author.mention)


@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    embed = discord.Embed(title="Avatar uzytkownika %s:" % (user.name), url=user.avatar_url, color=0x42ebf4)
    embed.set_image(url=user.avatar_url)
    await bot.say(embed=embed)
    log("avatar", ctx.message.author, ctx.message.author.mention)


@bot.command(pass_context=True)
async def jebac(ctx, user: discord.Member):
    await bot.say("**Jebac cie %s**" % (user.mention))
    log("jebac", ctx.message.author, ctx.message.author.mention)


@bot.command(pass_context=True)
async def channelid(ctx, channel: discord.Channel):
    embed = discord.Embed(title="ID kanalu " + channel.name, description=channel.id,color=0x42ebf4)
    await bot.say(embed=embed)
    log("channelid", ctx.message.author, ctx.message.author.mention)


@bot.command(pass_context=True)
async def gra_dodaj(ctx, arg : str):
    author = ctx.message.author
    if arg == "lol":
        role = discord.utils.get(ctx.message.server.roles, name="LoL")
        await bot.add_roles(author, role)
        emoji = discord.utils.get(ctx.message.server.emojis, name="poggers")
        await bot.say("Poprawnie nadano range LoL %s" %(emoji))
    elif arg == "cs:go":
        role = discord.utils.get(ctx.message.server.roles, name="CS:GO")
        await bot.add_roles(author, role)
        emoji = discord.utils.get(ctx.message.server.emojis, name="poggers")
        await bot.say("Poprawnie nadano range CS:GO %s" %(emoji))
    elif arg == "mc":
        role = discord.utils.get(ctx.message.server.roles, name="MC")
        await bot.add_roles(author, role)
        emoji = discord.utils.get(ctx.message.server.emojis, name="poggers")
        await bot.say("Poprawnie nadano range MC %s" %(emoji))
    else:
        emoji = discord.utils.get(ctx.message.server.emojis, name="thinkers")
        await bot.say("Podaj poprawną nazwę rangi %s. Aby sprawdzic dostepne wpisz .gra list" %(emoji))
    log("gra_dodaj", ctx.message.author, ctx.message.author.mention)


@bot.command(pass_context=True)
async def gra_usun(ctx, arg : str):
    author = ctx.message.author
    if arg == "lol":
        role = discord.utils.get(ctx.message.server.roles, name="LoL")
        await bot.remove_roles(author, role)
        emoji = discord.utils.get(ctx.message.server.emojis, name="poggers")
        await bot.say("Poprawnie odebrano range LoL %s" %(emoji))
    elif arg == "cs:go":
        role = discord.utils.get(ctx.message.server.roles, name="CS:GO")
        await bot.remove_roles(author, role)
        emoji = discord.utils.get(ctx.message.server.emojis, name="poggers")
        await bot.say("Poprawnie odebrano range CS:GO %s" %(emoji))
    elif arg == "mc":
        role = discord.utils.get(ctx.message.server.roles, name="MC")
        await bot.remove_roles(author, role)
        emoji = discord.utils.get(ctx.message.server.emojis, name="poggers")
        await bot.say("Poprawnie odebrano range MC %s" %(emoji))
    else:
        emoji = discord.utils.get(ctx.message.server.emojis, name="thinkers")
        await bot.say("Podaj poprawną nazwę rangi %s. Aby sprawdzic dostepne wpisz .gra list" %(emoji))
    log("gra_usun", ctx.message.author, ctx.message.author.mention)


@bot.command(pass_context=True)
async def gra_list(ctx):
    embed = discord.Embed(title="Dostępne Rangi", color=0x42ebf4)
    embed.add_field(name="League of Legends", value="Argument: lol", inline=False)
    embed.add_field(name="Counter-Strike: Global Offensive", value="Argument: cs:go", inline=False)
    embed.add_field(name="Minecraft", value="Argument: mc", inline=False)
    embed.add_field(name="Przykładowe użycie:", value=".gra_dodaj lol", inline=False)
    await bot.say(embed=embed)
    log("gra_list", ctx.message.author, ctx.message.author.mention)
    

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def aktualizacja(ctx, tresc : str):
    embed = discord.Embed(title="Aktualizacja Bota", description=tresc, color=0x42ebf4)
    await bot.say(embed=embed)
    await bot.delete_message(ctx.message)
    log("aktualizacja", ctx.message.author, ctx.message.author.mention)


@bot.command(pass_context=True)
async def komendy(ctx):
    embed = discord.Embed(title="Dostepne komendy", description="-----------", color=0x42ebf4)
    embed.add_field(name="hi", value="Powitaj sie z botem :D", inline=False)
    embed.add_field(name="ping", value="Sprawdza reakcję bota", inline=False)
    embed.add_field(name="info", value="Wyświetla informacje o danym użytkowniku", inline=False)
    embed.add_field(name="avatar", value="Wyświetla zdjęcie profilowe danego uśytkownika", inline=False)
    embed.add_field(name="jebac", value="Najlepiej wpisać nick Lethrilla ;D", inline=False)
    embed.add_field(name="komendy", value="Wyswietla dostepne komendy", inline=False)
    embed.add_field(name="channelid", value="Sprawdza Indentyfikator wskazanego kanału", inline=False)
    embed.add_field(name="gra_dodaj", value="Po wskazaniu rangi tematycznej z gry, przyznaje ci ją", inline=False)
    embed.add_field(name="gra_usun", value="Po wskazaniu rangi tematycznej z gry, odbiera ci ją", inline=False)
    embed.add_field(name="gra_list", value="Wyświetla listę dostępnych rang", inline=False)
    await bot.say(embed=embed)
    log("komendy", ctx.message.author, ctx.message.author.mention)


#--------------------ERROR--------------------#


@channelid.error
async def channelid_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="ID kanalu "+ctx.message.channel.name, description=ctx.message.channel.id, color=0x42ebf4)
        await bot.say(embed=embed)
        log("channelid", ctx.message.author, ctx.message.author.mention)


@avatar.error
async def channelid_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Twój awatar to:", url=ctx.message.author.avatar_url, color=0x42ebf4)
        embed.set_image(url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
        log("avatar", ctx.message.author, ctx.message.author.mention)

    
@jebac.error
async def jebac_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        user = discord.utils.get(ctx.message.server.members, id="218294304353943553")
        await bot.say("**Jebac cie %s**" % (user.mention))
        log("jebac", ctx.message.author, ctx.message.author.mention)

    
@gra_dodaj.error
async def gra_dodaj_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        emoji = discord.utils.get(ctx.message.server.emojis, name="thinkers")
        await bot.say("Podaj poprawna nazwe rangi %s. Aby sprawdzic dostepne wpisz .gra list ;D" %(emoji))
        log("gra_dodaj", ctx.message.author, ctx.message.author.mention)


@gra_usun.error
async def gra_usun_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        emoji = discord.utils.get(ctx.message.server.emojis, name="thinkers")
        await bot.say("Podaj poprawna nazwe rangi %s. Aby sprawdzic dostepne wpisz .gra list ;D" %(emoji))
        log("gra_usun", ctx.message.author, ctx.message.author.mention)
        

bot.run("MzcyMDQ3OTcyOTQ0NTc2NTEz.DalaSw.uKGDKB5MTolbfuez7YuSsUArZzU")
