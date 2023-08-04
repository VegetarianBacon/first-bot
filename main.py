from keep_alive import keep_alive

import discord

import pymongo
from pymongo import MongoClient

mclient = MongoClient()
mclient = MongoClient(
    'mongodb+srv://VegetarianBacon:J252Fu2xHyW3jnR@cluster0-0pp9p.mongodb.net/test?retryWrites=true'
)

db = mclient.test_database

import datetime

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}
#posts = db.posts
#post_id = posts.insert_one(post).inserted_id
#print(str(post_id))

from discord.ext.commands import Bot

import random

import re

from discord.utils import get

from discord.ext import commands

import time

print(time.time())

import asyncio

import os

BOT_PREFIX = (">", "<@!496104735724797952>", "<@496104735724797952> ")

TOKEN = os.getenv("token")

print("The secret TOKEN is:")
print(TOKEN)

client = Bot(command_prefix=BOT_PREFIX, case_insensitive=True)

client.remove_command('help')


@client.event
async def on_ready():
    server = len(client.servers)
    activityy = discord.Game(name=str(server) + " servers. Type " +
                             BOT_PREFIX[0] + "help")
    await client.change_presence(game=activityy, status=discord.Status.idle)


async def background_loop():
    await client.wait_until_ready()
    while not client.is_closed:
        f = open('a.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('a.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('autorole.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('autorole.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('botfile4.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('botfile4.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('c.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('c.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('cookiedir.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('cookiedir.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('cookies.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('cookies.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f.close()
        f = open('currency', 'r')
        lines = f.readlines()
        print('CURRENCY LINES:\n' + str(lines) + 'e')
        for line in lines:
            if line.startswith('219235011545530368'):
                print('Veggie line: ' + line)
                channel = client.get_channel('510786188077170688')
                await client.send_message(channel, 'Veggie line: ' + line)
        #lines = f.readlines()
        lines = "".join(str(y) for y in lines)
        f = open('currency', 'w')
        f.write(lines)
        f = open('hunt.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('hunt.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('hello.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('hello.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('leaver.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('leaver.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('rates.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('rates.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('ulf.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('ulf.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('userlist.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('userlist.txt', 'w')
        f.write("".join(str(y) for y in lines))
        #f = open('utext.txt', 'r')
        #f.close()
        f = open('utest.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('utest.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('utest2.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('utest2.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('wait.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('wait.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('welcomer.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('welcomer.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('zemotes.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('zemotes.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f = open('zroles.txt', 'r')
        lines = f.readlines()
        #print(lines)
        f = open('zroles.txt', 'w')
        f.write("".join(str(y) for y in lines))
        f.close()
        from datetime import datetime
        from pytz import timezone
        est = timezone('EST')
        print(str(datetime.now(est)) + " - Files refreshed")

        await asyncio.sleep(60)


#@client.command(pass_context = True)
#async def serverr(context):
#await client.say(context.message.server.name)

#egg

#@client.event
#async def on_guild_join(guild):
#from discord.utils import find
#general = find(lambda x: x.name == 'general', guild.text_channels)
#if general and general.permissions_for(guild.me).send_messages:
#await general.send('Thanks for adding me to **{}**! For increased perfomance in areas such as my currency system, add me to the top of the roles list and make sure that I have all permissions checked (you don\'t have to give me administrator or tag everyone permissions though).\n\nThanks for adding me to your server! For questions or concerns, contact me at `VegetarianBacon#5162` or join my server: https://discord.gg/VEnS4Vj'.format(guild.name))

#@client.command()
#async def eek(context):
#await client.say(context)


@client.event
async def on_server_emojis_update(emojibefore, emojiafter):
    for emoji in emojibefore:
        server_id = emoji.server.id

    if server_id in open('zroles.txt', 'r') or open('zemotes.txt', 'r'):
        print('Custom emoji updated')
        zrolecheck = False
        zemotescheck = False
        zroledefaults = []
        f = open('zroles.txt', 'r')
        lines = f.readlines()
        for line in lines:
            defaultcheck = line.split(' -- ', 1)[1]
            zrolecheck = True
            if len(defaultcheck) < 10:
                zroledefaults.append(line)
        f.close()

        zemotesdefaults = []
        f = open('zemotes.txt', 'r')
        lines = f.readlines()
        for line in lines:
            defaultcheck = line.split(' -- ', 1)[1]
            zemotescheck = True
            if len(defaultcheck) < 10:
                zemotesdefaults.append(line)
        f.close()

        #checking to see if emoji name changed

        linecheck = "x"

        count = 0
        count2 = 0
        for emoji in emojibefore:
            count += 1

        for emoji in emojiafter:
            count2 += 1

        if count == count2:
            linecheck = False

            f = open('zroles.txt', 'r')
            lines = f.readlines()
            #f = open('zroles.txt', 'w')
            #f.write('')
            f = open('zroles.txt', 'r')
            server = discord.Server

            afterlist = []
            for emoji in emojibefore:
                print('emojibefore: ' + str(emoji))
            for emoji in emojiafter:  #for all new emojis in list
                print('emojiafter: ' + str(emoji))
                #f = open('zroles.txt', 'r')
                for line in lines:  #for all the old emojis in list that are being used for the self-role system
                    #f = open('zroles.txt', 'r')
                    print(line)
                    if emoji.id in line:  #if the bot sees a new emoji in "emojiafter", then it will go here
                        print('emoji id is in line')
                        print(str(emoji))
                        beforesep = (line.split(" -- ")[0])
                        aftersep = str(emoji)
                        print('aftersep: ' + aftersep)
                        newline = (beforesep + " -- " + aftersep + " \n")
                        afterlist.append(newline)
                        linecheck = True

                    else:
                        print('emoji id is NOT in line')
                        newline = line
                        #afterlist.append(newline)
                    #f.close()

            afterlist = "".join(str(y) for y in afterlist)
            print('hello, i am here:' + afterlist)
            if linecheck == True:
                f = open('zroles.txt', 'w')
                f.write('')
                f.write(afterlist)
            f.close()

        if linecheck == False:
            f = open('zroles.txt', 'r')
            lines = f.readlines()
            f = open('zroles.txt', 'w')
            f.write('')
            f = open('zroles.txt', 'r')

            #checking to see if emoji was deleted
            #server_id = server.id
            print(server_id)
            for line in lines:
                if line.startswith(server_id):
                    for emoji1 in emojibefore:
                        if emoji1 not in emojiafter:
                            if not line.__contains__(emoji1.id):
                                f = open('zroles.txt', 'a')
                                f.write(line)
                                print(line)
            f.close()

        count = 0
        count2 = 0
        for emoji in emojibefore:
            count += 1

        for emoji in emojiafter:
            count2 += 1

        if count == count2:
            linecheck = False

            f = open('zemotes.txt', 'r')
            lines = f.readlines()
            #f = open('zemotes.txt', 'w')
            #f.write('')
            f = open('zemotes.txt', 'r')
            server = discord.Server

            afterlist = []
            for emoji in emojibefore:
                print('emojibefore NUMBER 2: ' + str(emoji))
            for emoji in emojiafter:  #for all new emojis in list
                print('emojiafter NUMBER 2: ' + str(emoji))
                #f = open('zroles.txt', 'r')
                for line in lines:  #for all the old emojis in list that are being used for the self-role system
                    #f = open('zroles.txt', 'r')
                    print(line)
                    if emoji.id in line:  #if the bot sees a new emoji in "emojiafter", then it will go here
                        print('emoji id is in line')
                        print(str(emoji))
                        beforesep = (line.split(" - ")[0])
                        aftersep = str(emoji)
                        print('aftersep: ' + aftersep)
                        newline = (beforesep + " - " + aftersep + " \n")
                        afterlist.append(newline)
                        linecheck = True

                    else:
                        print('emoji id is NOT in line')
                        newline = line
                        #afterlist.append(newline)
                    #f.close()

            afterlist = "".join(str(y) for y in afterlist)
            print('hello, i am here:' + afterlist)
            if linecheck == True:
                f = open('zemotes.txt', 'w')
                f.write('')
                f.write(afterlist)
            f.close()

        if linecheck == False:
            f = open('zemotes.txt', 'r')

            lines = f.readlines()

            f = open('zemotes.txt', 'w')
            f.write('')
            f = open('zemotes.txt', 'a')

            for line in lines:
                if line.startswith(server_id):
                    for emoji1 in emojibefore:
                        if emoji1 not in emojiafter:
                            if not line.__contains__(emoji1.id):
                                f = open('zemotes.txt', 'a')
                                f.write(line)
                                print(line)

        if zrolecheck == True:
            f = open('zroles.txt', 'a')
            f.write(zroledefaults)
            f.close()

        if zemotescheck == True:
            f = open('zemotes.txt', 'a')
            f.write(zemotesdefaults)
            f.close()

    #x = get(discord.Server)
    #server_id = x.id
    #print(server)
    #for emoji in emojibefore:
    #if emoji not in emojiafter:
    #print(str(emoji))
    #print(str(server))


@client.event
async def on_server_role_delete(role):
    f = open('zroles.txt', 'r')
    lines = f.readlines()
    f = open('zroles.txt', 'w')
    f.write('')
    f = open('zroles.txt', 'r')
    for line in lines:
        if line.startswith(role.server.id):
            if not line.__contains__(role.id):
                f = open('zroles.txt', 'a')
                f.write(line)
    f.close()


@client.event
async def on_member_join(member):
    print('member joined')
    f = open('autorole.txt', 'r')
    lines = f.readlines()
    for role in member.server.roles:
        for line in lines:
            if role.id in line:
                role = discord.utils.get(member.server.roles, id=line[:-1])
                try:
                    await client.add_roles(member, role)
                except:
                    pass
                print('line ' + line[:-1])

    f = open('welcomer.txt', 'r')
    lines = f.readlines()
    for channel in member.server.channels:
        for line in lines:
            if channel.id in line:
                for line in lines:
                    if line.startswith(channel.id):
                        print('indeed')
                        linemessage = line.split(channel.id + '= ', 1)[1]
                        memberfancy = '<member>'
                        for memberfancy in linemessage:
                            linemessage = linemessage.replace(
                                '<member>', '<@!' + member.id + '>')
                            membercountfancy = '<membercount>'
                            for membercountfancy in linemessage:
                                membercount = len(member.server.members)

                                def place_value(number):
                                    return ("{:,}".format(number))

                                membercount = (place_value(int(membercount)))
                                linemessage = linemessage.replace(
                                    '<membercount>', str(membercount))

                                membercountending = len(member.server.members)

                                def place_value(number):
                                    return ("{:,}".format(number))

                                membercountending = (place_value(
                                    int(membercountending)))
                                endingdecider = membercountending[-1:]
                                ending = 'th'
                                if endingdecider == '1':
                                    ending = 'st'
                                if endingdecider == '2':
                                    ending = 'nd'
                                if endingdecider == '3':
                                    ending = 'rd'
                                membercountending = str(
                                    membercountending) + ending
                                linemessage = linemessage.replace(
                                    '<membercountending>',
                                    str(membercountending))
                                realchannel = discord.utils.get(
                                    member.server.channels, id=str(channel.id))

                        await client.send_message(realchannel, linemessage)

                        await client.process_commands(member)


@client.event
async def on_member_remove(member):
    print('member left')
    f = open('leaver.txt', 'r')
    lines = f.readlines()
    for channel in member.server.channels:
        for line in lines:
            if channel.id in line:
                for line in lines:
                    if line.startswith(channel.id):
                        print('indeed')
                        linemessage = line.split(channel.id + '= ', 1)[1]
                        memberfancy = '<member>'
                        for memberfancy in linemessage:
                            linemessage = linemessage.replace(
                                '<member>', '<@!' + member.id + '>')
                            membercountfancy = '<membercount>'
                            for memberfancy in linemessage:
                                membercount = len(member.server.members)

                                def place_value(number):
                                    return ("{:,}".format(number))

                                membercount = (place_value(int(membercount)))
                                linemessage = linemessage.replace(
                                    '<membercount>', str(membercount))

                                membercountending = len(member.server.members)

                                def place_value(number):
                                    return ("{:,}".format(number))

                                membercountending = (place_value(
                                    int(membercountending)))
                                endingdecider = membercountending[-1:]
                                ending = 'th'
                                if endingdecider == '1':
                                    ending = 'st'
                                if endingdecider == '2':
                                    ending = 'nd'
                                if endingdecider == '3':
                                    ending = 'rd'
                                membercountending = str(
                                    membercountending) + ending
                                linemessage = linemessage.replace(
                                    '<membercountending>',
                                    str(membercountending))
                            realchannel = discord.utils.get(
                                member.server.channels, id=str(channel.id))
                            await client.send_message(realchannel, linemessage)

                            await client.process_commands(member)


@client.event
async def on_message(message):

    if message.author == client.user:
        return
        print('ok')

    #print(message.author.name + "#" + message.author.discriminator)

    if message.content.startswith('>'):

        print(message.author.name)
        print(message.author.id)
        print(message.author.name + "#" + message.author.discriminator)

        #await client.send_message(message.channel, message.author.name)
        #print(message.author.user.tag)
    #serverlist = "".join(str(y) for y in serverlist)

    #if message.content.__contains__('egg'):
    #await client.send_message(message.channel, 'egg indeed')

    #FOR EMOJI STUFF: MAKE COMPATIBILITY WITH UNICODE EMOTES (IMPORT SIX AND STUFF https://stackoverflow.com/questions/4987327/how-do-i-check-if-a-string-is-unicode-or-ascii)
    f = open('zemotes.txt', 'r')
    listwithservers = []
    try:
        server_id = message.server.id
        for line in f:
            if server_id in line:
                line2 = line[line.rindex('= ') + 1:]
                #print(line2)
                lMessage1 = str(line2)
                lMessage = lMessage1.split(' - ')[0]
                lMessage2 = lMessage1.split(' - ')[1]
                lMessage = lMessage[1:]
                #print(lMessage)
                n = message.content.lower()
                #print('xxxxxx' + n)
                #print('xxxxxx' + lMessage.lower())
                if n.__contains__(str(lMessage.lower())):
                    #await client.send_message(message.channel, "goteem")
                    #await client.send_message(message.channel, line)
                    #print('alright')
                    lineread = f.readline()
                    listwithservers.append(line)
                    #await client.send_message(message.channel, lineread)
                    emoji = str(lMessage2)
                    #await client.send_message(message.channel, emoji)
                    #print('ooooo' + lMessage2)

                    #import six
                    #if isinstance(emoji, six.text_type):

                    #else:
                    charcount = len(emoji)
                    print(emoji)
                    print(charcount)
                    if charcount == 3:
                        emoji = emoji[:-2]
                        await client.add_reaction(message, emoji)
                    else:
                        emoji = "".join(emoji.split(":", 2)[2])

                        emoji = emoji[:-2]

                        emoji = emoji[:-1]

                        #await client.send_message(message.channel, emoji)

                        for x in client.get_all_emojis():
                            if x.id == emoji:
                                try:
                                    await client.add_reaction(message, x)
                                    #await client.send_message(message.channel, emoji)
                                except:
                                    pass
    except:
        pass

    if message.content.startswith('>members'):
        x = message.server.members
        y = []
        for member in x:
            y.append(member.name + "\n")
        y = "".join(str(z) for z in y)
        a = message.server.id
        y = (y + " " + str(a))
        await client.send_message(message.channel, y)

    if message.content == '>leaderboard':
        await client.send_message(
            message.channel,
            'Incorrect usage. Usage: `>leaderboard [server - shows leaderboard for this server, global - shows global leaderboard]`'
        )

    if message.content.startswith('>testing'):
        x = message.server.members
        y = []
        f = open("currency", "r")
        for member in x:
            memid = member.id
            if memid in open("currency").read():
                await client.send_message(message.channel, "True")
            else:
                await client.send_message(message.channel, "False")
            y.append(member.id + "\n")
        f.close()
        y = "".join(str(z) for z in y)
        a = message.server.id

    if message.content.startswith('>leaderboard global'):
        f = open('currency', 'r')
        count = 0
        listt = []
        #members = message.server.members
        for x in f.readlines():
            count += 1
            #if count > 10:
            #continue
            #print(str(count))
            #print(x)
            x = x.split()
            #money = x.split(' ', 1)[1]
            #money = money.strip('\n')
            #print(money)
            listt.append(x)
            listt.sort(key=lambda y: int(y[1]), reverse=True)
            #print(listt)

        #print('ok')

        count2 = 0

        listt2 = []

        for x in listt:
            while count2 + 1 < 11:

                #print(str(count2))
                #print(x)
                x = ' '.join(str(y) for y in x)
                amount = x.split(' ', 1)[1]
                user = x.split(' ', 1)[0]
                for server in client.servers:
                    for member in server.members:
                        if str(member.id) == user:
                            user = discord.utils.get(client.get_all_members(),
                                                     id=str(user))
                            count2 += 1

                            listt2.append(
                                str(count2) + '. ' + str(user) + ' - ' +
                                amount + '\n')
                #print(str(listt2))
                break

        import random

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        x = discord.Color((r << 16) + (g << 8) + b)

        embed = discord.Embed(title="Showing global leaderboard...",
                              description=''.join(str(x) for x in listt2),
                              color=x)
        embed.set_author(
            name="Leaderboard",
            icon_url=
            "https://cdn.discordapp.com/attachments/356529602555805696/505737945903398912/bbot_1.png"
        )
        embed.set_footer(
            text='For best results, make sure the bot is above other ranks.')
        await client.send_message(message.channel, embed=embed)
        f.close()

    if message.content.startswith('>leaderboard server'):
        f = open('currency', 'r')
        count = 0
        listt = []
        for x in f.readlines():
            count += 1
            #if count > 10:
            #continue
            #print(str(count))
            #print(x)
            x = x.split()
            #money = x.split(' ', 1)[1]
            #money = money.strip('\n')
            #print(money)
            listt.append(x)
            listt.sort(key=lambda y: int(y[1]), reverse=True)
            #print(listt)

        #print('ok')

        count2 = 0

        listt2 = []

        for x in listt:
            while count2 + 1 < 11:

                #print(str(count2))
                #print(x)
                x = ' '.join(str(y) for y in x)
                amount = x.split(' ', 1)[1]
                user1 = x.split(' ', 1)[0]
                user = discord.utils.get(client.get_all_members(),
                                         id=str(user1))
                if user not in message.server.members:
                    break
                else:
                    count2 += 1
                    listt2.append(
                        str(count2) + '. ' + str(user) + ' - ' + amount + '\n')
                    #print(str(listt2))
                    break

        import random

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        x = discord.Color((r << 16) + (g << 8) + b)

        embed = discord.Embed(title="Showing global leaderboard...",
                              description=''.join(str(x) for x in listt2),
                              color=x)
        embed.set_author(
            name="Leaderboard",
            icon_url=
            "https://cdn.discordapp.com/attachments/356529602555805696/505737945903398912/bbot_1.png"
        )
        embed.set_footer(
            text='For best results, make sure the bot is above other ranks.')
        await client.send_message(message.channel, embed=embed)
        f.close()

    if message.content.startswith(">friendsearch"):
        f = open('utest.txt')
        line = f.readline()

        f2 = open('utest2.txt', 'w')

        while line:

            sep = ' - '
            rest2 = line.split(sep, 1)[0]
            st = line

            sep = ' - '
            rest3 = line.split(sep, 1)[1]
            st1 = rest3
            st1 = st1[:-1]
            userlistwithformatting = ('<@!' + rest2 + '>' + ' - ' + st1 + "\n")
            f2.write(userlistwithformatting)
            line = f.readline()

        f2 = open('utest2.txt', "r")

        import random
        lines = open('utest2.txt').readlines()
        random.shuffle(lines)
        open('utest2.txt', 'w').writelines(lines)
        lineList = f2.readlines()

        lineList2 = ''.join(map(str, lineList))
        print(lineList2)
        f2.close()

        f = open("utest2.txt", "r")
        read = f.readlines()

        lastlines = read[-5:]
        lastlines2 = " ".join(str(x) for x in lastlines)

        print(lastlines2)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        x = discord.Color((r << 16) + (g << 8) + b)

        f.close()
        f2.close()
        print(userlistwithformatting)
        embed = discord.Embed(title="Some cool dudes you should check out...",
                              description=lastlines2,
                              color=x)
        await client.send_message(message.channel, embed=embed)

    else:
        pass

    await client.process_commands(message)


@client.command(pass_context=True)
async def register(context):
    #await client.say(context.message.author.id)
    f = open("currency", "r")
    if context.message.author.id in f.read():
        await client.say("You have already registered.")
        f.close()

    else:
        f = open("currency", "a")
        f.write(context.message.author.id + " 1000\n")
        await client.say(
            "Thanks for registering. You now have the ability to use the currency commands!"
        )
        f.close()

    pass_context = False


@client.command(
    pass_context=True,
    aliases=['money', 'cash', 'dollars', 'credits', 'wallet', 'bacon'])
async def baconbucks(context):
    f = open("currency", "r")
    if context.message.author.id in open("currency").read():
        f = open("currency", "r")
        linez = f.readlines()

        linese = "".join(str(y) for y in linez)
        print(linese)

        print('1---')

        with open("currency", "r") as fi:
            #description = []
            for ln in fi:
                if ln.startswith(str(context.message.author.id) + " "):
                    id2 = ln
                    print("id: " + str(id2))

        sep = str(context.message.author.id)
        textbeforeclientID2 = linese.split(sep, 1)[0]
        if textbeforeclientID2 == " ":
            textbeforeclientID2 = "h"
        print(textbeforeclientID2)

        print('2---')

        sep = str(id2)
        textafterclientID2 = linese.split(sep, 1)[1]
        if textafterclientID2 == " ":
            textafterclientID2 = "h"
        print(textafterclientID2)

        sep = ' '
        rest2 = id2.split(sep, 1)[0]
        print('3---')
        print(rest2)

        sep = ' '
        usercurrency = id2.split(sep, 1)[1]
        print('3.5---')
        print(usercurrency)
        usercurrency = str(usercurrency)
        await client.say("You have **" + usercurrency[:-1] +
                         "** :bacon: BaconBucks. :bacon:")
    else:
        await client.say(
            "You have not registered for the currency system. To register, run the command `>register`. *Note: By registering, your username and discriminator will be shown on the global leaderboard.* "
        )
        await client.process_commands(context)
        f.close()
    pass_context = False


#8ball


@client.command(name='8ball',
                description="Shakes the eight ball.",
                brief="Shakes the eight ball.",
                pass_context=True)
async def eightball(context):
    possible_responses = [
        'That is a no',
        'It is not looking likely',
        'Too hard to tell',
        'Maybe',
        'Yes',
    ]
    await client.say(
        random.choice(possible_responses) + ", " +
        context.message.author.mention + ".")


pass_context = False

#ping


@client.command()
async def ping():
    import requests
    time = requests.get("https://VegetarianBot--robbiewinfield.repl.co"
                        ).elapsed.total_seconds()
    print("Pong!")

    await client.say("Pong! " + str(time) + 's')


@client.command()
async def invite():
    print(
        "https://discordapp.com/oauth2/authorize?client_id=496104735724797952&scope=bot&permissions=2146958839"
    )

    await client.say(
        "https://discordapp.com/oauth2/authorize?client_id=496104735724797952&scope=bot&permissions=2146958839"
    )


#googlesearch


@client.command()
async def googlesearch(*args):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    botargs = ''
    for word in args:
        botargs += word
        botargs += ' '

        print(args)

    if botargs.__contains__(", "):
        print("okay")
    else:
        await client.say(
            "Please follow this format: `googlesearch [query], [number of results]`"
        )

    stringnumber = (botargs.split(", ")[1])
    print(int(stringnumber))

    stringquery = (botargs.split(", ")[0])

    if int(stringnumber) > 10:
        await client.say("Please input a number no greater than 10.")
    else:
        showingresults = "Showing top " + str(
            stringnumber) + "results for " + str(stringquery) + "."

        await client.say(showingresults)

        # to search
        query = str(stringquery)

        searchlist = []

        for j in search(query,
                        tld="co.in",
                        safe='on',
                        num=float(stringnumber),
                        stop=1,
                        pause=2):
            searchlist.append(j + "\n")

            if str(j):
                "ok"
            else:
                await client.say("No results found.")
        searchlist = "".join(str(y) for y in searchlist)
        await client.say(searchlist)


#echo


@client.command()
async def echo(*args):

    countcheck = 0

    f = open("botfile4.txt", "r")

    with open('botfile4.txt') as f:
        first = f.read(1)
        if not first:
            print('botfile4.txt is empty; starting at 0')
            f = open("botfile4.txt", "w")
            f.write(str(0))

    f = open("botfile4.txt", "r")

    countcheckinteger = f.read()

    ###

    countcheck = int(countcheckinteger)

    count = True

    while count:
        countcheck = countcheck + 1
        print("Command run ", countcheck, " times.")

        f = open("botfile4.txt", "w")
        f.write(countcheck.__str__())

        text = "\nThis command has been run " + str(
            countcheck) + " times.\nGoal: 1,000 runs!"

        f.close()

        count = False


#outputting response \/ \/ \/

    output = ''
    for word in args:
        output += word
        output += ' '
    if '@' in output:
        output = output.replace("@", "@ ")

    newline = "\n"

    await client.say(output + "\n")
    await client.say(text)


@client.command(pass_context=True)
async def help(ctx):
    f = open("botfile4.txt", "r")
    helpcountcheck = f.read()

    m = True
    desc = "🍎 - General commands\n💵 - Currency commands\n🛠️ - Administrator only commands\n🏠 - Return back to this page\n\nCommand prefix: " + BOT_PREFIX[
        0] + " or just tag me like `@BaconBot#8035 [command]`\nSupport server: https://discord.gg/XaZB5ua\nBot developer: VegetarianBacon#5162"

    DMCheck = False

    if ctx.message.server == None:
        #await client.say("Sending DM friendly version of the help message...")
        DMCheck = True
        reactorid = "placeholder"

    DMCheck = True

    #channel2 = ctx.message.channel
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    randcolor = discord.Color((red << 16) + (green << 8) + blue)
    homecolor = discord.Color(0xffffff)

    if DMCheck == False:
        helpp = "Help"
    else:
        #helpp = "Help (DM version)"
        helpp = "Help"

    embed = discord.Embed(
        title=
        "React with the following to view a particular category of commands...",
        description=desc,
        color=homecolor)
    embed.set_author(
        name=helpp,
        icon_url=
        "https://cdn.discordapp.com/attachments/356529602555805696/505737945903398912/bbot_1.png"
    )
    embed.set_footer(
        text=
        'Make sure I have the ability to add reactions AND to manage reactions.'
    )
    x = await client.say(embed=embed)
    homeembed = embed

    await client.add_reaction(x, '🏠')
    await client.add_reaction(x, '🍎')
    await client.add_reaction(x, '💵')
    await client.add_reaction(x, '🛠')
    #author = reaction.message.author
    #await client.say(author)
    while m == True:
        #if DMCheck == False:
        userreaction, reactor = await client.wait_for_reaction(
            ['🏠', '🍎', '💵', '🛠'], message=x)
        #res2, reactor = await client.wait_for_reaction(['👎'], message=x)

        reactorid = reactor.id
        #await client.say(str(reactorid))
        if reactorid == ctx.message.author.id:
            e = True
            #await client.remove_reaction(x, '🏠', member = reactor)
            #await client.remove_reaction(x, '🍎', member = reactor)
            #await client.remove_reaction(x, '💵', member = reactor)
            #await client.remove_reaction(x, '🛠', member = reactor)
        else:
            e = False

        if e == True:

            if reactorid == "496104735724797952":
                pass
            else:
                #await client.say('{0.user} reacted with {0.reaction.emoji}!'.format(res))

                currencydesc = '`dailybacon`: Receive your daily 1,000 :bacon: BaconBucks. :bacon:\n\n`register`: Register for the currency commands. *Note: By registering, your username and discriminator will be shown on the global leaderboard.* \n\n`baconbucks`: Check your current amount of :bacon: BaconBucks :bacon:.\n\n`leaderboard global`: Shows the top users with the most :bacon: BaconBucks :bacon: across the globe.\n\n`leaderboard server`: View the top users with the most :bacon: BaconBucks :bacon: in your server.\n\n`hunt` and `redeem`: Use the hunt command to hunt for wild boars. After you catch one, use the redeem command to get your :bacon: BaconBucks. :bacon:\n\n`pay`: Pay a member :bacon: BaconBucks. :bacon: Usage: `pay [member to pay; tag them] [amount of 🥓 BaconBucks 🥓 to give]`'

                regulardesc = '`roles`: Shows a list of self-assignable roles for your server, if it has been set up on your server. React with the emojis given to receive the corresponding role. To remove a role, react with the same emoji.\n\n`8ball`: Ask a question and shake the 8ball.\n\n`echo`: Echos whatever you say. Also, please get this command to 1,000 runs. We are currently at ' + str(
                    helpcountcheck
                ) + ' runs.\n\n`googlesearch`: Search for up to 10 sites at once. Usage: `googlesearch [query], [number of results]`\n\n`ping`: Pong!\n\n`servers`: Displays a list of servers I am in. If I have the ability to create an invite per each server I am in, I will create an invite for that server. Otherwise, I will display \"No invite available\".\n\n`pdpvsts`: Short for \"PewDiePie vs. T-Series\"; checks the current number of subscribers each one has and shows who has more by how much.'

                aodesc = '`addreaction`: Adds a reaction to every message sent that you specify. Usage: `addreaction [message to react to] - [emoji]`\n\n`removereaction`: Removes an existing reaction. Usage: `removereaction [message to remove reaction to] - [emoji]`\n\n`addrole`: Adds a role to the self-assignable role system. Users will have to run the command ' + BOT_PREFIX[
                    0] + 'roles and react with an emoji you choose to obtain the role. Usage: `addrole [self-assignable role users can get; caps-sensitive] -- [emoji they must react with to obtain the role]`\n\n`removerole`: Remove a role to the self-assignable role system. This role will not be obtainable via the ' + BOT_PREFIX[
                        0] + 'roles command anymore. Usage: `removerole [self-assignable role to remove; caps-sensitive] -- [emoji that\'s used to obtain role]`\n\n`welcomer`: Enables/disables a welcome message I will say upon a member joining. Run the command in the channel you would like people to be welcomed in. Usage: `welcomer [message I will say upon a member joining; use <membercount> to show your current member count or use <membercountending> to get the member count with \"st\", \"nd\", or \"rd\" at the end - note: you must include the phrase \"<member>\" so I can mention the member]`\n\n`leaver`: Enables/disables a leave message I will say upon a member leaving. Run the command in the channel you would like people to be said bye to in. Usage: `leaver [message I will say upon a member leaving; use <membercount> to show your current member count or use <membercountending> to get the member count with \"st\", \"nd\", or \"rd\" at the end - note: you must include the phrase \"<member>\" so I can mention the member]`\n\n`autorole`: Enables/disables the autorole function; gives a member a role upon joining. Usage: `autorole [role to give to members upon joining]`'

                currencycolor = discord.Color(0x33cc33)
                regularcolor = discord.Color(0xff0000)
                aocolor = discord.Color(0x7289DA)

                currencyembed = discord.Embed(
                    title="Showing a list of currency commands...",
                    description=currencydesc,
                    color=currencycolor)
                currencyembed.set_author(
                    name=helpp,
                    icon_url=
                    "https://cdn.discordapp.com/attachments/356529602555805696/505737945903398912/bbot_1.png"
                )
                currencyembed.set_footer(
                    text='Make sure I have the ability to add reactions.')

                regularembed = discord.Embed(
                    title="Showing a list of general commands...",
                    description=regulardesc,
                    color=regularcolor)
                regularembed.set_author(
                    name=helpp,
                    icon_url=
                    "https://cdn.discordapp.com/attachments/356529602555805696/505737945903398912/bbot_1.png"
                )
                regularembed.set_footer(
                    text='Make sure I have the ability to add reactions.')

                aoembed = discord.Embed(
                    title="Showing a list of administrator only commands...",
                    description=aodesc,
                    color=aocolor)
                aoembed.set_author(
                    name=helpp,
                    icon_url=
                    "https://cdn.discordapp.com/attachments/356529602555805696/505737945903398912/bbot_1.png"
                )
                aoembed.set_footer(
                    text='Make sure I have the ability to add reactions.')

                if userreaction.emoji == '🏠':
                    #await client.say(str(reactor) + ' has reacted with ' + str(userreaction.emoji))
                    #await client.say(homeembed)
                    if DMCheck == False:
                        await client.edit_message(x, embed=homeembed)
                    else:
                        await client.delete_message(x)
                        x = await client.say(embed=homeembed)
                        await client.add_reaction(x, '🏠')
                        await client.add_reaction(x, '🍎')
                        await client.add_reaction(x, '💵')
                        await client.add_reaction(x, '🛠')
                if userreaction.emoji == '🍎':
                    #await client.say(str(reactor) + ' has reacted with ' + str(userreaction.emoji))
                    if DMCheck == False:
                        await client.edit_message(x, embed=regularembed)
                    else:
                        await client.delete_message(x)
                        x = await client.say(embed=regularembed)
                        await client.add_reaction(x, '🏠')
                        await client.add_reaction(x, '🍎')
                        await client.add_reaction(x, '💵')
                        await client.add_reaction(x, '🛠')
                if userreaction.emoji == '💵':
                    #await client.say(str(reactor) + ' has reacted with ' + str(userreaction.emoji))
                    if DMCheck == False:
                        await client.edit_message(x, embed=currencyembed)
                    else:
                        await client.delete_message(x)
                        x = await client.say(embed=currencyembed)
                        await client.add_reaction(x, '🏠')
                        await client.add_reaction(x, '🍎')
                        await client.add_reaction(x, '💵')
                        await client.add_reaction(x, '🛠')
                if userreaction.emoji == '🛠':
                    #await client.say(str(reactor) + ' has reacted with ' + str(userreaction.emoji))
                    if DMCheck == False:
                        await client.edit_message(x, embed=aoembed)
                    else:
                        await client.delete_message(x)
                        x = await client.say(embed=aoembed)
                        await client.add_reaction(x, '🏠')
                        await client.add_reaction(x, '🍎')
                        await client.add_reaction(x, '💵')
                        await client.add_reaction(x, '🛠')

                if DMCheck == False:
                    await client.remove_reaction(x, '🏠', member=reactor)
                    await client.remove_reaction(x, '🍎', member=reactor)
                    await client.remove_reaction(x, '💵', member=reactor)
                    await client.remove_reaction(x, '🛠', member=reactor)
                else:
                    pass

                #await client.add_reaction(x, '🏠')
                #await client.add_reaction(x, '🍎')
                #await client.add_reaction(x, '💵')
                #await client.add_reaction(x, '🛠')
                m = True

            f.close()


@client.command(pass_context=True)
async def servers(message):
    if message.message.server.id != '530023458910765086':
        await client.say('Removed.')
        await client.process_commands(message)

    DMCheck = False

    if message.message.server == None:
        DMCheck = True
        DMCheck2 = False

    count = 0
    count2 = 0
    number = 0

    msg = await client.say('Processing... this may take a minute...')
    serverlist = []
    serverss = list(client.servers)
    servercount = str(len(client.servers))

    for server in client.servers:
        number += 1
        count = 0
        count2 = 0
        # Spin through every server
        for channel in server.channels:
            b = server.id
            count = count + 1
        #await client.say(str(count))
        channelstuff = client.get_server(b)
        #await client.say(str(channelstuff))

        server2 = server.id
        #print(server2)
        server22 = client.get_server(server2)
        for channel in server.channels:
            # Channels on the server
            try:
                if channel.permissions_for(server.me).send_messages:
                    b = channel.id
                    #print(b)
                    channelstuff = client.get_channel(b)

                    server2 = server.id
                    #print(server2)
                    server22 = client.get_server(server2)
                    #print(server22)
                    try:
                        invite = await client.create_invite(
                            destination=channelstuff, xkcd=True, max_uses=0)
                        #await client.say(str(invite) + ' ')

                        #if len("".join(str(y) for y in serverlist) + str(number) + '. :diamond_shape_with_a_dot_inside: ' + str(server22) + ' - ' + str(invite) + '\n') >= 2048:
                        #pass
                        #else:
                        serverlist.append(
                            str(number) +
                            '. :diamond_shape_with_a_dot_inside: ' +
                            str(server22) + ' - ' + str(invite) + '\n')
                        break
                    except:
                        count2 = count2 + 1
                    #except:
                    #invite = "Sorry, no invite available"
                    #await client.say(str(invite))
                else:
                    count2 = count2 + 1
            except:
                pass
        if count2 == count:
            #if len("".join(str(y) for y in serverlist) + str(number) +'. :diamond_shape_with_a_dot_inside: ' + str(server22) + ' - ' + 'No invite available\n') >= 2048:
            #pass
            #else:
            serverlist.append(
                str(number) + '. :diamond_shape_with_a_dot_inside: ' +
                str(server22) + ' - ' + 'No invite available\n')
        #print(str(serverlist))

    serverlist2 = serverlist
    serverlist = "".join(str(y) for y in serverlist)

    if len(serverlist) <= 2048:
        await client.say(serverlist)
        pass
    else:
        listt = []
        s = ''.join(str(n) for n in serverlist2)
        elecount = 0
        ncount = 0
        templist = []
        for element in serverlist2:
            elecount += 1
        print(str(elecount))
        for element in serverlist2:
            count = 0
            if len(''.join(str(o) for o in templist)) + len(element) > 2048:
                for item in templist:
                    count += 1
                    #print(str(count))
                ncount += 1
                listt.append(''.join(str(o) for o in templist))
                templist = []
                templist.append(element)
            else:
                templist.append(element)
        listt.append(''.join(str(o) for o in templist))
        #print('listt ' + str(listt))
        #print('templist ' + str(templist))
        #x = await client.say(listt[0])

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        x = discord.Color((r << 16) + (g << 8) + b)
        #print(serverlist)

        embed = discord.Embed(title='I am currently in **' + servercount +
                              ' servers:**\n',
                              description=listt[0],
                              color=x)
        embed.set_author(
            name="Page 1",
            icon_url=
            "https://cdn.discordapp.com/attachments/356529602555805696/505737945903398912/bbot_1.png"
        )
        embed.set_footer(
            text=
            'For best results, make sure the bot has the ability to create instant invites.'
        )
        await client.delete_message(msg)
        msg = await client.say(embed=embed)
        counter = 0
        await client.add_reaction(msg, '⬅')
        await client.add_reaction(msg, '➡')
        maximum = 0
        for element in listt:
            maximum += 1
        while True:
            userreaction, reactor = await client.wait_for_reaction(['⬅', '➡'],
                                                                   message=msg)
            if reactor.id == message.message.author.id:
                pass
            if reactor.id == "496104735724797952":
                pass
            else:
                if userreaction.emoji == '➡':
                    print('maximum = ' + str(maximum))
                    print('counter = ' + str(counter))
                    if maximum - 1 == counter:
                        pass
                    else:
                        counter += 1

                        embed = discord.Embed(title='I am currently in **' +
                                              servercount + ' servers:**\n',
                                              description=listt[counter],
                                              color=x)
                        embed.set_author(
                            name="Page " + str(counter + 1),
                            icon_url=
                            "https://cdn.discordapp.com/attachments/356529602555805696/505737945903398912/bbot_1.png"
                        )
                        embed.set_footer(
                            text=
                            'For best results, make sure the bot has the ability to create instant invites.'
                        )

                        await client.edit_message(msg, embed=embed)
                    await client.remove_reaction(msg, '➡', member=reactor)
                if userreaction.emoji == '⬅':
                    if counter == 0:
                        pass
                    else:
                        counter -= 1
                        embed = discord.Embed(title='I am currently in **' +
                                              servercount + ' servers:**\n',
                                              description=listt[counter],
                                              color=x)
                        embed.set_author(
                            name="Page " + str(counter + 1),
                            icon_url=
                            "https://cdn.discordapp.com/attachments/356529602555805696/505737945903398912/bbot_1.png"
                        )
                        embed.set_footer(
                            text=
                            'For best results, make sure the bot has the ability to create instant invites.'
                        )

                        await client.edit_message(msg, embed=embed)
                    await client.remove_reaction(msg, '⬅', member=reactor)
        #await client.say(str(len(embed)))


@client.command()
async def servers2():

    serverlist = []
    serverss = list(client.servers)
    servercount = str(len(client.servers))

    for x in serverss:
        server22 = x.name
        serverlist.append(':diamond_shape_with_a_dot_inside: ' + server22 +
                          '\n')
        print(serverlist)
    serverlist = "".join(str(y) for y in serverlist)
    await client.say('I am currently in **' + servercount + ' servers:**\n' +
                     serverlist)


@client.command()
async def friends():
    await client.say(
        "`adduser`: Adds your Discord profile to a public list; means you are open for others sending you friend requests.\n`removeuser`: Removes you from the list.\n`friendsearch`: Shows the list of users who are open to friending (they have added theirself to this list via the adduser command)."
    )


@client.command(pass_context=True)
async def removeuser(context):

    author = context.message.author.id

    print(author)

    f = open("utest.txt", "a")

    if context.message.author.id in open('utest.txt').read():

        # to delete the line from the file

        with open('utest.txt', 'r+') as f:
            data = ''.join([i for i in f
                            if not i.lower().startswith(author)])  #1
            f.seek(0)  #2
            f.write(data)  #3
            f.truncate()
        await client.say("Removing ID from the file.")
    else:
        await client.say("You are not in the file.")
        #deleting empty lines
        with open("utest.txt", "r") as f:
            lines = f.readlines()

        with open("utest.txt", "w") as f:
            [f.write(line) for line in lines if line.strip()]
        #

    pass_context = False


@client.command()
async def servercount():
    await client.say(len(client.servers))


@client.command(pass_context=True, aliases=['daily'])
async def dailybacon(context):

    f = open("currency", "r")
    if context.message.author.id in f.read():
        f.close()

        author = context.message.author.id

        import time

        check = False

        start = time.time()

        time.clock()

        # await client.say(time.time())

        elapsed = 0

        timeuntil = float(time.time()) + 86400

        f = open("wait.txt", "r")

        ###

        #if the user already has a timestamp in the file
        if context.message.author.id in open('wait.txt').read():

            linez = f.readlines()

            linese = "".join(str(y) for y in linez)
            print(linese)

            print('1---')

            with open("wait.txt", "r") as fi:
                #description = []
                for ln in fi:
                    if ln.startswith(str(context.message.author.id) + " "):
                        id2 = ln
                        print("id: " + str(id2))

            sep = str(context.message.author.id)
            textbeforeclientID2 = linese.split(sep, 1)[0]
            if textbeforeclientID2 == " ":
                textbeforeclientID2 = "h"
            print(textbeforeclientID2)

            print('2---')

            sep = str(id2)
            textafterclientID2 = linese.split(sep, 1)[1]
            if textafterclientID2 == " ":
                textafterclientID2 = "h"
            print(textafterclientID2)

            sep = ' '
            rest2 = id2.split(sep, 1)[0]
            print('3---')
            print(rest2)

            sep = ' '
            timeee = id2.split(sep, 1)[1]
            print('3.5---')
            print(timeee)

            #timeee is the time that is currently in the file for the user

            #if the current time is less than the time in the file
            if time.time() < float(timeee):
                #away = int(round(float(timeee) - time.time()))

                #away = str(away)

                import time

                away = int(round(float(timeee) - time.time()))

                away = str(away)

                sec = float(away.strip())

                days = (sec / 86400)

                hrs = (sec / 3600)
                hrs1 = int(hrs)

                mins = (abs(hrs1 - hrs)) * 60

                roundedmins = round(mins)

                if roundedmins == 60:
                    hrs1 = hrs1 + 1
                    roundedmins = 0

                #tells how long until the command cannot be used

                if hrs1 == 1:

                    send = "You cannot use this command for " + str(
                        hrs1) + ' hour and ' + str(roundedmins) + " minutes."
                else:
                    send = "You cannot use this command for " + str(
                        hrs1) + ' hours and ' + str(roundedmins) + " minutes."

                await client.say(send)

                f.close()
                fi.close()
            else:
                #if the time in the file is expired/if the time in the file is less than the current time

                id2REVISED = (rest2 + " " + str(timeuntil))
                #this replaces the time in the file with the time until they can hunt again

                print('4---')

                rewritetofile = (textbeforeclientID2.strip("\n") + "\n" +
                                 id2REVISED + "\n" + textafterclientID2)

                #await client.say(rewritetofile)

                f = open("wait.txt", "w")
                f.write(rewritetofile)

                #await client.say("time started " + context.message.author.id)
                f.close()

                f = open("currency", "r")

                if context.message.author.id in open('currency').read():

                    f = open("currency", "r")

                    linez = f.readlines()

                    linese = "".join(str(y) for y in linez)
                    print(linese)

                    print('1---')

                    with open("currency", "r") as fi:
                        #description = []
                        for ln in fi:
                            if ln.startswith(
                                    str(context.message.author.id) + " "):
                                id2 = ln
                                print("id: " + str(id2))

                    sep = str(context.message.author.id)
                    textbeforeclientID2 = linese.split(sep, 1)[0]
                    if textbeforeclientID2 == " ":
                        textbeforeclientID2 = "h"
                    print(textbeforeclientID2)

                    print('2---')

                    sep = str(id2)
                    textafterclientID2 = linese.split(sep, 1)[1]
                    if textafterclientID2 == " ":
                        textafterclientID2 = "h"
                    print(textafterclientID2)

                    sep = ' '
                    rest2 = id2.split(sep, 1)[0]
                    print('3---')
                    print(rest2)

                    sep = ' '
                    usercurrency = id2.split(sep, 1)[1]
                    print('3.5---')
                    print(usercurrency)

                    usercurrency = float(usercurrency)
                    usercurrency = usercurrency + 1000
                    usercurrency = int(usercurrency)
                    print(usercurrency)

                    id2REVISED = (rest2 + " " + str(usercurrency))

                    print('4---')

                    rewritetofile = (textbeforeclientID2.strip("\n") + "\n" +
                                     id2REVISED + "\n" + textafterclientID2)

                    print(rewritetofile)

                    f = open("currency", "w")
                    f.write(str(rewritetofile))
                    f.close()
                    await client.say(
                        "You have gained your daily 1,000 🥓 BaconBucks. 🥓")
                else:
                    await client.say(
                        "You have gained your daily 1,000 🥓 BaconBucks. 🥓")
                    f = open("wait.txt", "a")
                    f.write(context.message.author.id + " " + str(timeuntil) +
                            "\n")
                    f.close()
                    f = open("currency", "r")
                    linez = f.readlines()

                    linese = "".join(str(y) for y in linez)
                    print(linese)

                    print('1---')

                    with open("currency", "r") as fi:
                        #description = []
                        for ln in fi:
                            if ln.startswith(
                                    str(context.message.author.id) + " "):
                                id2 = ln
                                print("id: " + str(id2))

                    sep = str(context.message.author.id)
                    textbeforeclientID2 = linese.split(sep, 1)[0]
                    if textbeforeclientID2 == " ":
                        textbeforeclientID2 = "h"
                    print(textbeforeclientID2)

                    print('2---')

                    sep = str(id2)
                    textafterclientID2 = linese.split(sep, 1)[1]
                    if textafterclientID2 == " ":
                        textafterclientID2 = "h"
                    print(textafterclientID2)

                    sep = ' '
                    rest2 = id2.split(sep, 1)[0]
                    print('3---')
                    print(rest2)

                    sep = ' '
                    usercurrency = id2.split(sep, 1)[1]
                    print('3.5---')
                    print(usercurrency)

                    usercurrency = float(usercurrency)
                    usercurrency = usercurrency + 1000
                    usercurrency = int(usercurrency)
                    print(usercurrency)

                    id2REVISED = (rest2 + " " + str(usercurrency))

                    print('4---')

                    rewritetofile = (textbeforeclientID2.strip("\n") + "\n" +
                                     id2REVISED + "\n" + textafterclientID2)

                    print(rewritetofile)

                    f = open("currency", "w")
                    f.write(str(rewritetofile))
                    f.close()
                ###
        else:
            await client.say(
                "You have gained your daily 1,000 :bacon: BaconBucks. 🥓")
            f = open("wait.txt", "a")
            f.write(context.message.author.id + " " + str(timeuntil) + "\n")
            f.close()
            f = open("currency", "r")
            linez = f.readlines()

            linese = "".join(str(y) for y in linez)
            print(linese)

            print('1---')

            with open("currency", "r") as fi:
                #description = []
                for ln in fi:
                    if ln.startswith(str(context.message.author.id) + " "):
                        id2 = ln
                        print("id: " + str(id2))

            sep = str(context.message.author.id)
            textbeforeclientID2 = linese.split(sep, 1)[0]
            if textbeforeclientID2 == " ":
                textbeforeclientID2 = "h"
            print(textbeforeclientID2)

            print('2---')

            sep = str(id2)
            textafterclientID2 = linese.split(sep, 1)[1]
            if textafterclientID2 == " ":
                textafterclientID2 = "h"
            print(textafterclientID2)

            sep = ' '
            rest2 = id2.split(sep, 1)[0]
            print('3---')
            print(rest2)

            sep = ' '
            usercurrency = id2.split(sep, 1)[1]
            print('3.5---')
            print(usercurrency)

            usercurrency = float(usercurrency)
            usercurrency = usercurrency + 1000
            usercurrency = int(usercurrency)
            print(usercurrency)

            id2REVISED = (rest2 + " " + str(usercurrency))

            print('4---')

            rewritetofile = (textbeforeclientID2.strip("\n") + "\n" +
                             id2REVISED + "\n" + textafterclientID2)

            print(rewritetofile)

            f = open("currency", "w")
            f.write(str(rewritetofile))
            f.close()
    else:
        await client.say(
            "You have not registered for the currency system. To register, run the command `>register`."
        )


@client.command()
async def haha():
    await client.say('yes <:yess:471749005177782283>')


@client.command(pass_context=True, no_pm=True)
async def addreaction(ctx, *args):
    if ctx.message.author.server_permissions.administrator:
        f = open('zemotes.txt', 'r+')
        server_id = ctx.message.server.id
        #await client.say(args)
        #await client.say(ctx.message.content)

        print(args)

        botargs = ''
        for word in args:
            botargs += word
            botargs += ' '

            print(args)

        if botargs.__contains__(" - "):
            print("okay")

        else:
            await client.say(
                "Please follow this format: `addreaction [message to react to] - [emoji]`"
            )
            await client.process_commands(ctx)

        stringnumber = (botargs.split(" - ")[1])
        print(str(stringnumber))

        stringquery = (botargs.split(" - ")[0])
        e = str(stringnumber)

        print(e)
        print('kyhgvbhj' + str(len(e)))
        v = len(e)
        if v == 2:
            e = e[:-1]
            try:
                await client.add_reaction(ctx.message, e)
            except:
                await client.say(
                    "Invalid emoji; please only insert an emoji after the \" - \"."
                )
                await client.process_commands(ctx)
            f = open('zemotes.txt', 'a+')
            f.write(server_id + '= ' + botargs + "\n")
            print(botargs)
            f = open('zemotes.txt', 'r+')
            f.close()
            await client.say("I will now react to \"" + stringquery +
                             "\" with \"" + stringnumber + "\".")
            await client.process_commands(ctx)
        else:
            pass

        try:
            e = "".join(e.split(":", 2)[2])
        except:
            await client.say(
                "Invalid emoji; please only insert an emoji after the \" - \"."
            )
            await client.process_commands(ctx)

        e = e[:-2]

        #await client.say(e)

        for x in client.get_all_emojis():
            if x.id == e:
                try:
                    await client.add_reaction(ctx.message, x)
                except:
                    await client.say(
                        'I either do not have sufficient permissions to add reactions or I was given an invalid emoji.'
                    )

                    await client.process_commands(ctx)
        #if e not in client.get_all_emojis():
        #await client.say('Invalid emoji. Please check to make sure this emoji exists orif you already have a reaction set up with the same emoji and message.')
        #await client.process_commands(ctx)

        if stringquery.__contains__(" - "):
            await client.say(
                "Sorry, but you cannot use \" - \" in your message")
            await client.process_commands(ctx)
        f = open('zemotes.txt', 'a+')
        f.write(server_id + '= ' + botargs + "\n")
        print(botargs)
        f = open('zemotes.txt', 'r+')
        f.close()

        await client.say("I will now react to \"" + stringquery +
                         "\" with \"" + stringnumber + "\".")
    else:
        await client.say(
            'You do not have administrator permissions and therefore cannot add messages for me to react to.'
        )


@client.command(pass_context=True, no_pm=True)
async def toast(emoji: discord.Emoji, ctx, *args):
    await client.say(str(args))
    print(args)
    await client.say(ctx)
    server_id = ctx.message.server.id


@client.command(pass_context=True, no_pm=True)
async def removereaction(ctx, *args):
    if ctx.message.author.server_permissions.administrator:
        f = open('zemotes.txt', 'r+')
        server_id = ctx.message.server.id
        #await client.say(args)
        #await client.say(ctx.message.content)

        print(args)

        botargs = ''
        for word in args:
            botargs += word
            botargs += ' '

            print(args)

        if botargs.__contains__(" - "):
            print("okay")

        else:
            await client.say(
                "Please follow this format: `addreaction [message to remove reaction to] - [emoji]`"
            )
            await client.process_commands(ctx)

        stringnumber = (botargs.split(" - ")[1])
        print(str(stringnumber))

        stringquery = (botargs.split(" - ")[0])
        e = str(stringnumber)

        f = open('zemotes.txt', 'r')
        with open('zemotes.txt', encoding='utf-8') as f:
            linesread = f.read()
            print('j,bnnmb,mn' + str(linesread))
            print(server_id + '= ' + botargs)
            if (server_id + '= ' + botargs) in linesread:
                pass
            else:
                await client.say('Emoji or message does not exist.')
                await client.process_commands(ctx)
        f = open('zemotes.txt', 'r')
        lines = f.readlines()
        f = open('zemotes.txt', 'w')
        for line in lines:
            if line != (server_id + '= ' + botargs + "\n"):
                f.write(line)

        if len(stringquery) == 2:
            stringnumber = stringnumber[:-1]

        await client.say('Reaction \"' + stringnumber + '\" removed for \"' +
                         stringquery + '\".')
        f.close()


@client.command(pass_context=True, no_pm=True)
async def reactions(ctx):
    server_id = ctx.message.server.id
    y = []
    f = open('zemotes.txt', 'r')
    for line in f.readlines():
        if line.startswith(str(server_id)):
            z = line
            print(server_id + '= ')
            z = ''.join(z.partition('= ')[1:])
            z = z[2:]
            y.append(z)

    y = "".join(str(x) for x in y)
    await client.say(y)


@client.event
async def on_server_join(ctx):
    owner = (ctx.owner.name + "#" + ctx.owner.discriminator)
    ownerid = ctx.owner.id
    for channel in ctx.channels:
        if channel.permissions_for(ctx.me).send_messages:
            channelid = channel.id
            channelstuff = client.get_channel(channelid)
            try:
                await client.send_message(
                    channelstuff,
                    "Thanks for adding me to your server! In order for me to perform the best, I suggest making sure I have at minimum the following permissions...\n\n-Create instant invite\n-Manage emojis\n-Manage roles\n-Read text channels & see voice channels\n-All of the text permissions (except for mention everyone)\n\nI will not perform any actions that use the permissions above unless you use a command that tells me to. Make sure to type >help for a list of the commands that I can perform!"
                )
                break
            except:
                pass
    me = await client.get_user_info(ownerid)
    await client.send_message(
        me,
        "Thanks for adding me to your server! In order for me to perform the best, I suggest making sure I have at minimum the following permissions...\n\n-Create instant invite\n-Manage emojis\n-Read text channels & see voice channels\n-All of the text permissions (except for mention everyone)\n\nMake sure to type >help for a list of the commands that I can perform!"
    )


@client.command(pass_context=True, no_pm=True)
async def addrole(ctx, *args):
    if ctx.message.author.server_permissions.administrator:
        f = open('zroles.txt', 'r+')
        f.close()
        server_id = ctx.message.server.id
        #await client.say(args)
        #await client.say(ctx.message.content)

        f = open('zroles.txt', 'r')
        lines = f.readlines()
        idcount = lines.count(server_id)
        if idcount > 20:
            await client.say(
                'Due to Discord limitations, I cannot have 20 different reactions per message, meaning I cannot have more than 20 auto-roles'
            )
            await client.process_commands(ctx)

        print(args)

        botargs = ''
        for word in args:
            botargs += word
            botargs += ' '

            print(args)

        if botargs.__contains__(" -- "):
            print("okay")

        else:
            await client.say(
                "Please follow this format: `addrole [role to make self-assignable] - [emoji user will react with to get role]`"
            )
            await client.process_commands(ctx)

        stringnumber = (botargs.split(" -- ")[1])
        print(str(stringnumber))

        stringquery = (botargs.split(" -- ")[0])
        e = str(stringnumber)

        server_id = ctx.message.server.id
        f = open('zroles.txt', 'r')
        for line in f.readlines():
            if line.startswith(str(server_id)):
                nm = False
                if stringnumber in line:

                    await client.say(
                        'You\'re already using this emoji for a different role reaction, please use a different emoji.'
                    )
                    await client.process_commands(ctx)
                #if len(stringquery) == 2:
                #stringquery2 = stringquery
                #stringquery2 = stringquery2[:-1]
                #if stringquery2 in line:
                #await client.say('You\'re already using this role as with the auto-roler.')
                #await client.process_commands(ctx)
                try:
                    role = get(ctx.message.server.roles, name=stringquery)
                    if role.id in line:
                        await client.say(
                            'You\'re already using this role with the self-role-assigner.'
                        )
                        nm = True

                except:
                    pass
                    #await client.process_commands(ctx)
                if nm == True:
                    await client.process_commands(ctx)

        print(e)
        print('kyhgvbhj' + str(len(e)))
        v = len(e)
        if v == 2:
            e = e[:-1]
            try:
                await client.add_reaction(ctx.message, e)
            except:
                await client.say(
                    "Invalid emoji; please only insert an emoji after the \" -- \"."
                )
                await client.process_commands(ctx)
            #await client.say(stringquery)
            #print(stringquery[1:])

            role = get(ctx.message.server.roles, name=stringquery)
            if str(role) == "None":
                await client.say(
                    "This role does not exist... Please check for capitalization and spelling."
                )
                await client.process_commands(ctx)
            #role = role.id
            #roleid = discord.Role
            botargs = (str(role.id) + " -- " + stringnumber)
            f = open('zroles.txt', 'a+')
            f.write(server_id + '= ' + botargs + "\n")
            print(botargs)
            f = open('zroles.txt', 'r+')
            f.close()
            await client.say("Users will now get the role \"" + stringquery +
                             "\" when they react with \"" + stringnumber +
                             "\" on the command " + BOT_PREFIX[0] + "roles.")
            await client.process_commands(ctx)
        else:
            pass

        try:
            e = "".join(e.split(":", 2)[2])
        except:
            await client.say(
                "Invalid emoji; please only insert an emoji after the \" - \"."
            )
            await client.process_commands(ctx)

        e = e[:-2]

        #await client.say(e)
        k = False
        for x in client.get_all_emojis():
            if x.id == e:
                try:
                    await client.add_reaction(ctx.message, x)
                    k = True
                except:
                    await client.say(
                        'I either do not have sufficient permissions to add reactions or I was given an invalid emoji.'
                    )

                    await client.process_commands(ctx)
        if k == False:
            await client.say(
                'Invalid emoji. Please check to make sure this emoji exists or if you already have an auto-role set up with the same emoji and message.'
            )
            await client.process_commands(ctx)

        if stringquery.__contains__(" -- "):
            await client.say(
                "Sorry, but you cannot use \" -- \" in your role name.")
            await client.process_commands(ctx)
        #await client.say(stringquery)
        #print(stringquery[1:])

        role = get(ctx.message.server.roles, name=stringquery)
        if str(role) == "None":
            await client.say(
                "This role does not exist... Please check for capitalization and spelling."
            )
            await client.process_commands(ctx)
        #role = role.id
        #roleid = discord.Role
        botargs = (str(role.id) + " -- " + stringnumber)
        f = open('zroles.txt', 'a+')
        f.write(server_id + '= ' + botargs + "\n")
        print(botargs)
        f = open('zroles.txt', 'r+')
        f.close()
        await client.say("Users will now get the role \"" + stringquery +
                         "\" when they react with \"" + stringnumber + "\".")
        await client.process_commands(ctx)
    else:
        await client.say(
            'You do not have administrator permissions and therefore cannot add messages for me to react to.'
        )


@client.command(pass_context=True, no_pm=True)
async def roles(ctx):
    server_id = ctx.message.server.id
    y = []
    f = open('zroles.txt', 'r')
    for line in f.readlines():
        if line.startswith(str(server_id)):
            z = line
            print(server_id + '= ')
            z = ''.join(z.partition('= ')[1:])
            z = z[2:]
            y.append(z)

    listt = []
    #y = "".join(str(x) for x in y)
    #await client.say(y)
    for line in y:
        zz = line
        #await client.say(zz)
        roleid = (zz.split(" -- ")[0])
        #await client.say(roleid)
        rolename = get(ctx.message.server.roles, id=roleid)
        #await client.say(str(rolename))
        emoji = (zz.split(" -- ", 1)[1])
        #emojiid = discord.Emoji
        #emojiname = emojiid.name
        listt.append(str(rolename) + ": " + emoji)
    listt = "".join(str(x) for x in listt)
    #await client.say(str(listt))

    color = 0xFFFFFF

    embed = discord.Embed(
        title=
        "React with one of the following to obtain the corresponding role...",
        description=listt,
        color=color)
    embed.set_author(
        name="Roles",
        icon_url=
        "https://cdn.discordapp.com/attachments/356529602555805696/505737945903398912/bbot_1.png"
    )
    embed.set_footer(
        text='For best results, make sure the bot is above other ranks.')
    xx = await client.send_message(ctx.message.channel, embed=embed)
    #reactablemessage = await client.say(y)
    emojilist = []
    for line in y:
        #roleid = (line.split(" -- ")[0])
        emojiid = (line.split(" -- ")[1])
        print(emojiid)
        print(len(emojiid))
        emojiid = emojiid[:-2]

        if len(emojiid) > 10:
            emojiid = emojiid.split(r':')[-1]
            emojiid = emojiid[:-1]
            print('utfgtkihu,kgjn ' + emojiid)
            emojiname = discord.utils.get(client.get_all_emojis(),
                                          id=str(emojiid))
            await client.add_reaction(xx, emojiname)
            emojilist.append(emojiname)
        else:
            #await client.say(str(emojiname))
            await client.add_reaction(xx, emojiid)
            emojilist.append(emojiid)
    #await client.say(emojilist)

    m = True
    while m == True:
        #if DMCheck == False:
        userreaction, reactor = await client.wait_for_reaction(emojilist,
                                                               message=xx)
        #res2, reactor = await client.wait_for_reaction(['👎'], message=x)

        reactorid = reactor.id
        #await client.say(str(reactorid))
        if reactorid == ctx.message.author.id:
            pass

        if reactorid == "496104735724797952":
            pass
        else:
            emoji = discord.Emoji
            #await client.say(str(userreaction.emoji))
            emojiidnew = userreaction.emoji
            y = []
            f = open('zroles.txt', 'r')
            for line in f.readlines():
                if line.startswith(str(server_id)):
                    z = line
                    print(server_id + '= ')
                    z = ''.join(z.partition('= ')[1:])
                    z = z[2:]
                    y.append(z)
            for line in y:
                if str(emojiidnew) in line:
                    roleid = (line.split(" -- ")[0])
                    #await client.add_role(ctx.message.author, roleid)
                    rolename = get(ctx.message.server.roles, id=roleid)
                    if rolename in ctx.message.author.roles:

                        try:
                            await client.remove_roles(ctx.message.author,
                                                      rolename)
                        except:
                            await client.say(
                                'I either do not have permissions to add roles or this role is too high for me to remove.'
                            )
                            await client.process_commands(ctx)
                        await client.send_message(
                            ctx.message.author,
                            (ctx.message.server.name + ': role \"' +
                             str(rolename) + '\" removed.'))

                        await client.remove_reaction(xx,
                                                     emojiidnew,
                                                     member=reactor)
                        #await asyncio.sleep(5)
                        #await client.delete_message(n)
                    else:
                        try:
                            await client.add_roles(ctx.message.author,
                                                   rolename)
                        except:
                            await client.say(
                                'I either do not have permissions to add roles or this role is too high for me to add.'
                            )
                            await client.process_commands(ctx)

                        await client.send_message(
                            ctx.message.author,
                            (ctx.message.server.name + ': role \"' +
                             str(rolename) + '\" added.'))

                        await client.remove_reaction(xx,
                                                     emojiidnew,
                                                     member=reactor)
                        #await asyncio.sleep(5)
                        #await client.delete_message(n)


@client.command(pass_context=True, no_pm=True)
async def removerole(ctx, *args):
    if ctx.message.author.server_permissions.administrator:
        f = open('zroles.txt', 'r+')
        f.close()
        server_id = ctx.message.server.id
        #await client.say(args)
        #await client.say(ctx.message.content)

        print(args)

        botargs = ''
        for word in args:
            botargs += word
            botargs += ' '

            print(args)

        if botargs.__contains__(" -- "):
            print("okay")

        else:
            await client.say(
                "Please follow this format: `addrole [self-assignable role to remove] - [emoji user will react with to get role]`"
            )
            await client.process_commands(ctx)

        stringnumber = (botargs.split(" -- ")[1])
        print(str(stringnumber))

        stringquery = (botargs.split(" -- ")[0])
        e = str(stringnumber)
        role = get(ctx.message.server.roles, name=stringquery)
        botargs = (str(role.id) + ' -- ' + stringnumber)
        f = open('zroles.txt', 'r')
        with open('zroles.txt', encoding='utf-8') as f:
            linesread = f.read()
            print('j,bnnmb,mn' + str(linesread))
            print(server_id + '= ' + botargs)
            if (server_id + '= ' + botargs) in linesread:
                pass
            else:
                await client.say('Emoji or role does not exist.')
                await client.process_commands(ctx)
        f = open('zroles.txt', 'r')
        lines = f.readlines()
        f = open('zroles.txt', 'w')
        for line in lines:
            if line != (server_id + '= ' + botargs + "\n"):
                f.write(line)

        if len(stringquery) == 2:
            stringnumber = stringnumber[:-1]

        await client.say('Self-assignable role \"' + stringquery +
                         '\" removed with reaction \"' + stringnumber + '\".')
        f.close()


@client.command()
async def zroles():
    z = []
    f = open("zroles.txt", "r")
    for line in f.readlines():
        z.append(line)
    z = "".join(str(y) for y in z)
    await client.say(z)


@client.command()
async def zemotes():
    z = []
    f = open("zemotes.txt", "r")
    for line in f.readlines():
        z.append(line)
    z = "".join(str(y) for y in z)
    await client.say(z)


@client.command()
async def clear():
    f = open("zroles.txt", "w")
    f.write('')
    f.close()


@client.command(pass_context=True, no_pm=True)
async def welcomer(ctx, *args):
    if ctx.message.author.server_permissions.administrator:
        f = open('welcomer.txt', 'r+')
        lines = f.readlines()

        #print('lines ' + f.read())
        print(ctx.message.channel.id)
        channelid = ctx.message.channel.id
        
        writetofile = []
        #for channel in ctx.message.server.channels:
        for line in lines:
            if channelid in line:
                f = open('welcomer.txt', 'w')
                for line in lines:
                    if ctx.message.channel.id not in line:
                        writetofile.append(line)
                writetofile = ''.join(str(y) for y in writetofile)
                f.write(writetofile)
                f.close()
                await client.say('Welcomer disabled.')
                await client.process_commands(ctx)

        for channel in ctx.message.server.channels:
            for line in lines:
                if channel.id in line:
                    channelname = get(ctx.message.server.channels,
                                      id=channel.id)
                    await client.say(
                        'You already have a welcomer set up in #' +
                        str(channelname) + '.')
                    await client.process_commands(ctx)
        #print(args)

        botargs = ''
        for word in args:
            botargs += word
            botargs += ' '

            print(args)

        if '<member>' not in botargs:
            await client.say(
                'You must include \"<member>\" in your message so I can mention the member when they join.'
            )
            await client.process_commands(ctx)
        f = open('welcomer.txt', 'a')
        f.write(ctx.message.channel.id + '= ' + botargs + '\n')
        f.close()
        await client.say('Great! I will now say, \"' + botargs +
                         '\" in this channel when a new member joins.')


@client.command(pass_context=True, no_pm=True)
async def leaver(ctx, *args):
    if ctx.message.author.server_permissions.administrator:
        f = open('leaver.txt', 'r+')
        #print('lines ' + f.read())
        print(ctx.message.channel.id)
        channelid = ctx.message.channel.id
        lines = f.readlines()
        writelist = []
        #for channel in ctx.message.server.channels:
        for line in lines:
            if channelid in line:
                f = open('leaver.txt', 'w')
                for line in lines:
                    if ctx.message.channel.id not in line:
                        writelist.append(line)
                f = open('leaver.txt', 'w')
                writetofile = ''.join(str(y) for y in writelist)
                f.write(writetofile)
                f.close()
                await client.say('Leaver disabled.')
                await client.process_commands(ctx)

        for channel in ctx.message.server.channels:
            for line in lines:
                if channel.id in line:
                    channelname = get(ctx.message.server.channels,
                                      id=channel.id)
                    await client.say(
                        'You already have a leave message set up in #' +
                        str(channelname) + '.')
                    await client.process_commands(ctx)
        #print(args)

        botargs = ''
        for word in args:
            botargs += word
            botargs += ' '

            print(args)

        if '<member>' not in botargs:
            await client.say(
                'You must include \"<member>\" in your message so I can mention the member when they leave.'
            )
            await client.process_commands(ctx)
        f = open('leaver.txt', 'a')
        f.write(ctx.message.channel.id + '= ' + botargs + '\n')
        f.close()
        await client.say('Great! I will now say, \"' + botargs +
                         '\" in this channel when a member leaves.')


@client.command(pass_context=True, aliases=['boarhunt'])
async def hunt(ctx):
    f = open('hunt.txt', 'r')
    x = f.readlines()
    import time
    f = open('currency', 'r')
    lines = f.readlines()
    if ctx.message.author.id not in ''.join(str(y) for y in lines):
        await client.say(
            'You have not registered for the currency system yet. Run >register to register.'
        )
        f.close()
        await client.process_commands(ctx)
    f = open('hunt.txt', 'r')
    lines = f.readlines()
    print('hguiwoekgjhnbhueikfgjn ' + str(lines))
    if ctx.message.author.id not in ''.join(str(y) for y in lines):
        f = open('hunt.txt', 'a')
        f.write(ctx.message.author.id + ' ' + '0;0;0;0\n')
        print('i got here')
        f = open('hunt.txt', 'r')
        lines = f.readlines()
        f.close()
    for line in lines:
        if line.startswith(ctx.message.author.id):
            myline = line
    #checking how many boars there are
    myboarcount = myline.split(';')[0]
    myboarcount = myboarcount.split(' ')[1]
    print('myboarcount ' + myboarcount)
    if myboarcount == '1':
        await client.say('Your inventory is full.')
        await client.process_commands(ctx)
    #checking for cooldown between two hunt commands
    mytime = myline.split(';', 1)[1]
    mytime = mytime.split(';', 1)[0]
    if float(mytime) > float(time.time()):
        timedif = int(round(float(mytime) - time.time()))
        timedif = timedif
        sec = round(timedif)
        await client.say('You cannot hunt for ' + str(sec) + ' second(s).')
        await client.process_commands(ctx)
    newtime = time.time() + 30
    print(myline)
    mytimeafter = myline.split(';', 1)[1]
    print(mytimeafter)
    mytimeafter = mytimeafter.split(';', 1)[1]
    print('real: ' + mytimeafter)
    mytimebefore = myline.split(';', 1)[0]
    f = open('hunt.txt', 'w')
    f.write('')
    f = open('hunt.txt', 'a')
    for line in lines:
        if line.startswith(ctx.message.author.id):
            f.write(mytimebefore + ';' + str(newtime) + ';' + mytimeafter)
            print(mytimebefore + ';' + str(newtime) + ';' + mytimeafter)
        else:
            f.write(line)
    myline = mytimebefore + ';' + str(newtime) + ';' + mytimeafter
    import random
    f = open('hunt.txt', 'r')
    print('error: ' + str(f.readlines()))
    randpercent = random.randint(1, 4)
    if int(randpercent) != 1:
        r = random.randint(20, 40)
        randmessage = [
            'You were trampled by the boar. You have been charged ' + str(r) +
            ' :bacon: BaconBucks :bacon: for medical bills.',
            'You got lost along the way and could not find the boar. You have been charged '
            + str(r) +
            ' :bacon: BaconBucks :bacon: in hotel fees for the night.',
            'You caught a boar, but he got loose and ran away. You have been charged '
            + str(r) +
            ' :bacon: BaconBucks :bacon: for having to find food for the night.',
            'You tried to find a boar, but you were attacked by a pack of wolves on the way and your clothes were ripped to shreds. You paid '
            + str(r) + ' :bacon: BaconBucks :bacon: for new clothes.'
        ]
        await client.say(random.choice(randmessage))
        c = open('currency', 'r')
        clines = c.readlines()
        for line in clines:
            if line.startswith(ctx.message.author.id):
                cline = line
        currency = cline.split(' ', 1)[1]
        cid = cline.split(' ', 1)[0]
        #r = random.randint(20, 50)
        currency = str(int(currency) - int(r))
        newcline = (cid + ' ' + currency)
        f = open('currency', 'w')
        for line in clines:
            if line.startswith(ctx.message.author.id):
                f.write(newcline + '\n')
                print(newcline)
            else:
                f.write(line)
        f = open('currency', 'r')
        newclines = c.readlines()
        print(''.join(str(y) for y in newclines))
        await client.process_commands(ctx)
    print('hello there yeet')
    #make sure they can't redeem for 120 seconds
    #make sure they have a '1' instead of a '0'
    beforeturedeem = ";".join(myline.split(";", 2)[:2])
    print('1 ' + myline)
    turedeem = myline.split(';', 1)[1]
    turedeem = turedeem.split(';', 1)[1]
    afterturedeem = turedeem.split(';', 1)[1]
    turedeem = turedeem.split(';', 1)[0]
    turedeem = time.time() + 120
    f = open('hunt.txt', 'r')
    lines = f.readlines()
    f = open('hunt.txt', 'w')
    f.write('')
    f = open('hunt.txt', 'a')
    for line in lines:
        if line.startswith(ctx.message.author.id):
            f.write(beforeturedeem + ';' + str(turedeem) + ';' + afterturedeem)
            print('2 ' + beforeturedeem + ';' + str(turedeem) + ';' +
                  afterturedeem)
        else:
            f.write(line)
    myline = (beforeturedeem + ';' + str(turedeem) + ';' + afterturedeem)
    beforeboarcount = myline.split(' ')[0]
    afterboarcount = myline.split(';', 1)[1]
    myboarcount = '1'
    f = open('hunt.txt', 'r')
    lines = f.readlines()
    f = open('hunt.txt', 'w')
    f.write('')
    f = open('hunt.txt', 'a')
    for line in lines:
        print('line ' + line)
        if line.startswith(ctx.message.author.id):
            f.write(beforeboarcount + ' ' + str(myboarcount) + ';' +
                    afterboarcount)
            print('3 ' + beforeboarcount + ' ' + str(myboarcount) + ';' +
                  afterboarcount)
        else:
            f.write(line)
    f = open('hunt.txt', 'r+')
    lines = f.read()
    print('ewrtrewrtyr ' + str(lines))
    f.close()
    myline = (beforeboarcount + ' ' + str(myboarcount) + ';' + afterboarcount)
    await client.say(
        "You have caught a wild boar! After the cooldown, type >redeem to receive your 300 🥓 BaconBucks. 🥓"
    )


@client.command(pass_context=True)
async def redeem(ctx):
    f = open('hunt.txt', 'r')
    x = f.readlines()
    import time
    f = open('currency', 'r')
    lines = f.readlines()
    if ctx.message.author.id not in ''.join(str(y) for y in lines):
        await client.say(
            'You have not registered for the currency system yet. Run >register to register.'
        )
        f.close()
        await client.process_commands(ctx)
    f = open('hunt.txt', 'r')
    lines = f.readlines()
    print('hguiwoekgjhnbhueikfgjn ' + str(lines))
    if ctx.message.author.id not in ''.join(str(y) for y in lines):
        await client.say(
            'You cannot redeem :bacon: BaconBucks :bacon: if you don\'t have a boar! Use '
            + BOT_PREFIX[0] + 'hunt to hunt for a boar.')
        await client.process_commands(ctx)
    for line in lines:
        if line.startswith(ctx.message.author.id):
            myline = line
    print(myline)
    beforebetweenredeem = ";".join(myline.split(";", 3)[:3])
    betweenredeem = ";".join(myline.split(";", 3)[3:])
    
    if float(betweenredeem) > float(time.time()):
        timedif = int(round(float(betweenredeem) - time.time()))
        timedif = timedif
        secs = round(timedif)
        secs = timedif
        days = secs // 86400
        hours = (secs - days * 86400) // 3600
        minutes = (secs - days * 86400 - hours * 3600) // 60
        seconds = secs - days * 86400 - hours * 3600 - minutes * 60
        print('days ' + str(days))
        print('hours ' + str(hours))
        print('minutes ' + str(minutes))
        print('seconds ' + str(seconds))
        if minutes == 1:
            await client.say(
                'You are on a cooldown from your last redemption and cannot use this command for '
                + str(minutes) + ' minutes and ' + str(seconds) +
                ' second(s).')
        if minutes == 0:
            await client.say(
                'You are on a cooldown from your last redemption and cannot use this command for '
                + str(seconds) + ' second(s).')
        else:
            await client.say(
                'You are on a cooldown from your last redemption and cannot use this command for '
                + str(minutes) + ' minutes and ' + str(seconds) +
                ' second(s).')
        await client.process_commands(ctx)
    beforehuntandredeem = ";".join(myline.split(";", 2)[:2])
    huntandredeem = myline.split(';', 1)[1]
    huntandredeem = huntandredeem.split(';', 1)[1]
    afterhuntandredeem = huntandredeem.split(';', 1)[1]
    huntandredeem = huntandredeem.split(';', 1)[0]
    if float(huntandredeem) > float(time.time()):
        timedif = int(round(float(huntandredeem) - time.time()))
        timedif = timedif
        secs = round(timedif)
        days = secs // 86400
        hours = (secs - days * 86400) // 3600
        minutes = (secs - days * 86400 - hours * 3600) // 60
        seconds = secs - days * 86400 - hours * 3600 - minutes * 60
        print('days ' + str(days))
        print('hours ' + str(hours))
        print('minutes ' + str(minutes))
        print('seconds ' + str(seconds))
        if minutes == 0:
            await client.say(
                'You are still walking home and cannot use this command for ' +
                str(seconds) + ' second(s).')
        else:
            await client.say(
                'You are still walking home and cannot use this command for ' +
                str(minutes) + ' minute and ' + str(seconds) + ' second(s).')
        await client.process_commands(ctx)
    betweenredeem = time.time() + 600
    f = open('hunt.txt', 'w')
    f.write('')
    f = open('hunt.txt', 'a')
    for line in lines:
        if line.startswith(ctx.message.author.id):
            f.write(beforebetweenredeem + ';' + str(betweenredeem))
            print('2 ' + beforebetweenredeem + ';' + str(betweenredeem))
        else:
            f.write(line)
    myline = beforebetweenredeem + ';' + str(betweenredeem)
    beforeboarcount = myline.split(' ')[0]
    afterboarcount = myline.split(';', 1)[1]
    boarcounttest = myline.split(' ', 1)[1]
    boarcounttest = boarcounttest.split(';', 1)[0]
    if boarcounttest != '1':
        await client.say(
            'You cannot redeem :bacon: BaconBucks :bacon: if you don\'t have a boar! Use '
            + BOT_PREFIX[0] + 'hunt to hunt for a boar.')
        await client.process_commands(ctx)
    myboarcount = '0'
    f = open('hunt.txt', 'r')
    lines = f.readlines()
    f = open('hunt.txt', 'w')
    f.write('')
    f = open('hunt.txt', 'a')
    for line in lines:
        print('line ' + line)
        if line.startswith(ctx.message.author.id):
            f.write(beforeboarcount + ' ' + str(myboarcount) + ';' +
                    afterboarcount + '\n')
            print('3 ' + beforeboarcount + ' ' + str(myboarcount) + ';' +
                  afterboarcount)
        else:
            f.write(line)
    c = open('currency', 'r')
    clines = c.readlines()
    for line in clines:
        if line.startswith(ctx.message.author.id):
            cline = line
    currency = cline.split(' ', 1)[1]
    cid = cline.split(' ', 1)[0]
    currency = str(int(currency) + 300)
    newcline = (cid + ' ' + currency)
    f = open('currency', 'w')
    for line in clines:
        if line.startswith(ctx.message.author.id):
            f.write(newcline + '\n')
            print(newcline)
        else:
            f.write(line)
    f = open('currency', 'r')
    newclines = c.readlines()
    print(''.join(str(y) for y in newclines))
    await client.say(
        'You have redeemed your bacon from the boar and have received 300 :bacon: BaconBucks! :bacon:'
    )


@client.command()
async def huntread():
    f = open('hunt.txt', 'r')
    lines = f.readlines()
    await client.say(str(lines))


@client.command(pass_context=True, no_pm=True)
async def autorole(ctx, *args):
    if ctx.message.author.server_permissions.administrator:
        botargs = ''
        for word in args:
            botargs += word
            botargs += ' '

            print(args)
        if botargs == None:
            await client.say(
                'Please follow this format: `autorole [role to give to members upon joining]`'
            )
        role = get(ctx.message.server.roles, name=botargs[:-1])
        if role == None:
            await client.say(
                "This role does not exist... Please check for capitalization and spelling."
            )
            await client.process_commands(ctx)
        f = open('autorole.txt', 'r')
        lines = f.readlines()
        print(str(lines))
        print(role.id)
        writetofile = []
        for line in lines:
            if role.id in line:
                f = open('autorole.txt', 'w')
                for line in lines:
                    print('alright')
                    if role.id not in line:
                        writetofile.append(line)
                        #f.write(line)
                        #f = open('autorole.txt', 'r')
                        #print('yhgbk,ujh' + str(f.readlines()))
                        #f = open('autorole.txt', 'w')
                f = open('autorole.txt', 'w')
                writetofile = ''.join(str(y) for y in writetofile)
                f.write(writetofile)
                await client.say('\"' + botargs[:-1] +
                                 '\" has been removed as an auto-role.')
                f.close()
                await client.process_commands(ctx)

        await client.say('Users will now receive \"' + botargs[:-1] +
                         '\" upon joining.')
        f = open('autorole.txt', 'a')
        f.write(role.id + '\n')
        f.close()


@client.command()
async def autoread():
    f = open('autorole.txt', 'r')
    lines = f.read()
    await client.say(str(lines))
    f.close()


@client.command()
async def welcomeread():
    f = open('welcomer.txt', 'r')
    lines = f.read()
    await client.say(str(lines))
    f.close()


@client.command(pass_context=True)
async def cookieregister(context):
    #await client.say(context.message.author.id)
    f = open("cookies.txt", "r")
    if context.message.author.id in f.read():
        await client.say("You have already registered.")
        f.close()

    else:
        f = open("cookies.txt", "a")
        f.write(context.message.author.id + " 0\n")
        await client.say(
            "Thanks for registering. You now have the ability to use the cookie commands!"
        )
        f.close()
        f = open("rates.txt", "a")
        f.write(context.message.author.id + " 0\n")
        f.close()


@client.command(pass_context=True)
async def cookies(ctx):
    f = open('cookies.txt', 'r')

    if ctx.message.author.id in f.read():
        pass
    else:
        f = open('cookies.txt', 'a')
        f.write(ctx.message.author.id + ' 0\n')
    f = open('cookies.txt', 'r')

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    x = discord.Color((r << 16) + (g << 8) + b)
    lines = f.readlines()
    for line in lines:
        if line.startswith(ctx.message.author.id):
            cookiecount = line.split(' ', 1)[1]

    embed = discord.Embed(title="Cookie clicker...",
                          description=str(cookiecount))
    embed.set_author(
        name="Cookies",
        icon_url=
        "https://cdn.discordapp.com/attachments/356529602555805696/505737945903398912/bbot_1.png"
    )
    embed.set_image(
        url=
        "https://vignette.wikia.nocookie.net/steven-universe/images/7/70/Cookie.png/revision/latest?cb=20160822165305"
    )
    x = await client.send_message(ctx.message.channel, embed=embed)
    while True:

        await client.add_reaction(x, '🍪')
        userreaction, reactor = await client.wait_for_reaction(['🍪'],
                                                               message=x)
        #res2, reactor = await client.wait_for_reaction(['👎'], message=x)

        reactorid = reactor.id
        #await client.say(str(reactorid))
        if reactorid == ctx.message.author.id:
            pass

        if reactorid == "496104735724797952":
            pass
        else:
            print(cookiecount)
            cookiecount = int(cookiecount[:-1]) + 1
            for line in lines:
                if line.startswith(ctx.message.author.id):
                    myline = line
            cookiecount = str(str(cookiecount) + '\n')
            fileread = ''.join(str(y) for y in lines)
            fileread = fileread.replace(
                myline, ctx.message.author.id + ' ' + str(cookiecount))
            embed = discord.Embed(title="Cookie clicker...",
                                  description=str(cookiecount))
            embed.set_author(
                name="Cookies",
                icon_url=
                "https://cdn.discordapp.com/attachments/356529602555805696/505737945903398912/bbot_1.png"
            )
            embed.set_image(
                url=
                "https://vignette.wikia.nocookie.net/steven-universe/images/7/70/Cookie.png/revision/latest?cb=20160822165305"
            )
            await client.edit_message(x, embed=embed)
            await client.remove_reaction(x, '🍪', member=reactor)
            f = open('cookies.txt', 'w')
            f.write(fileread)
            f.close()


@client.command(pass_context=True)
async def cookiedir(ctx):
    f = open('cookiedir.txt', 'r')
    for line in f.readlines():
        if line.startswith('1 '):
            after = line.split(' = ', 1)[1]
            after = after[:-1]

    f = open('rates.txt', 'r')
    for line in f.readlines():
        if ' 1(' in line:
            after2 = line.split('1(', 1)[1]
            after2 = after2.split(')', 1)[0]
            print(str(after2))

    dif = float(time.time() - float(after2))
    numerator = after.split('/', 1)[0]
    denomenator = after.split('/', 1)[1]
    after = int(numerator) / int(denomenator)
    after = float(after) * int(dif)
    await client.say(str(int(after)))


keep_alive()


@client.command(pass_context=True)
async def pop(ctx):
    y = 'aaaaabbbbbcccccddddd'
    if len(y) <= 1:
        await client.say(y)
    else:
        listt = []
        while len(y) > 0:
            first = y[:5]
            y = y.split(first, 1)[1]
            listt.append(first)
            print(str(listt))
        x = await client.say(listt[0])
        await client.add_reaction(x, '⬅')
        await client.add_reaction(x, '➡')
        messagenumber = 0
        while True:
            userreaction, reactor = await client.wait_for_reaction(['⬅', '➡'],
                                                                   message=x)
            if reactor.id == ctx.message.author.id:
                pass
            if reactor.id == "496104735724797952":
                pass
            else:
                if userreaction.emoji == '➡':
                    if len(listt) == messagenumber + 1:
                        print('ok')
                    else:
                        messagenumber = messagenumber + 1
                        print(str(messagenumber))
                        try:
                            after = listt[messagenumber]
                            await client.edit_message(x, after)
                        except:
                            pass
                    await client.remove_reaction(x, '➡', member=reactor)
                if userreaction.emoji == '⬅':
                    if messagenumber == 0:
                        print('ok')
                    else:
                        messagenumber = messagenumber - 1
                        print(str(messagenumber))
                        try:
                            after = listt[messagenumber]
                            await client.edit_message(x, after)
                        except:
                            pass
                    await client.remove_reaction(x, '⬅', member=reactor)


@client.command(pass_context=True)
async def pay(ctx, *args):
    botargs = ''
    for word in args:
        botargs += word
        botargs += ' '

        print(args)
    print(botargs)

    if botargs.__contains__(" "):
        print("okay")

    else:
        await client.say(
            "Please follow this format: `pay [member to pay; tag them] [amount of 🥓 BaconBucks 🥓 to give]`"
        )
        await client.process_commands(ctx)

    membertopay = botargs.split(' ', 1)[0]

    print(str(membertopay))
    if membertopay[10] == '!':
        membertopay = membertopay[:-1][3:]
    else:
        membertopay = membertopay[:-1][2:]
    print(membertopay)
    if membertopay == ctx.message.author.id:
        await client.say(
            '...Well, I don\'t know why you\'d pay yourself, but...')
        await client.process_commands(ctx)
    f = open('currency', 'r')
    read = f.read()
    print(read)
    if membertopay not in read:
        await client.say(
            'That user has not registered for the currency system yet.')
        await client.process_commands(ctx)
    f.seek(0)
    lines = f.readlines()
    for line in lines:
        print('egg ' + line)
    for line in lines:
        #print('bcvcvcxv')
        if line.startswith(ctx.message.author.id):
            amount = line.split(' ', 1)[1]
            amount = amount[:-1]
            moneyinput = botargs.split(' ', 1)[1]
            print('e')
            try:
                moneyinput = (str(abs(int(moneyinput))))
            except:
                await client.say('Please give a valid integer.')
                await client.process_commands(ctx)
            print('ee')
            if int(moneyinput) > int(amount):
                await client.say(
                    'You cannot pay someone an amount that exceeds your total amount of :bacon: BaconBucks :bacon:!'
                )
                await client.process_commands(ctx)
            difference = int(amount) - int(moneyinput)
            newcline = (ctx.message.author.id + ' ' + str(difference))
            f = open('currency', 'w')
            for line in lines:
                if line.startswith(ctx.message.author.id):
                    f.write(newcline + '\n')
                    print(newcline)
                else:
                    f.write(line)
            f = open('currency', 'r')
            user = discord.utils.get(client.get_all_members(),
                                     id=str(membertopay))
            lines = f.readlines()
            for line in lines:
                if line.startswith(membertopay):
                    mtpline = line
                    print('mmm ' + mtpline)
                    amount = mtpline.split(' ', 1)[1]
                    amount = amount[:-1]
                    print('mmm ' + str(amount))
            added = int(amount) + int(moneyinput)
            newcline = (membertopay + ' ' + str(added))

            f = open('currency', 'w')
            for line in lines:
                if line.startswith(membertopay):
                    f.write(newcline + '\n')
                    print(newcline)
                else:
                    f.write(line)
                    print(line)
            f.seek(0)
            f = open('currency', 'r')
            lines = f.readlines()
            for line in lines:
                print('yegz ' + line)
            await client.say('You have payed ' + str(user) + ' **' +
                             str(moneyinput) +
                             '** :bacon: BaconBucks. :bacon:')
            f.close()


@client.command()
async def veggie():
    f = open('hunt.txt', 'r')


@client.group(pass_context=True)
async def shop(ctx):
    a = 'a'
    if ctx.invoked_subcommand is None:
        await client.say('Invalid sub command passed...')


@shop.group(pass_context=True)
async def buy(ctx):
    if ctx.invoked_subcommand is buy:
        await client.say('Invalide sub command passed...')


@client.command()
async def pdpvsts():
    import urllib.request
    import json
    import time

    key = "AIzaSyBZZCJ9xO_d7lGg40bTYfhgn-U4gyaqVSE"
    f = False
    #while True:
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

    key = "AIzaSyBZZCJ9xO_d7lGg40bTYfhgn-U4gyaqVSE"

    pew_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=PewDiePie&key=" + key
    tseries_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key=" + key
    headers = {
        'User-Agent': user_agent,
    }
    request = urllib.request.Request(pew_url, None,
                                     headers)  #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read()
    psubs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    headers = {
        'User-Agent': user_agent,
    }
    request = urllib.request.Request(tseries_url, None,
                                     headers)  #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read()
    tsubs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]

    if int(psubs) > int(tsubs):
        pdifference = int(psubs) - int(tsubs)

        def place_value(number):
            return ("{:,}".format(number))

        pdifference = (place_value(int(pdifference)))
        plead = 'PewDiePie leads T-Series by ' + str(
            pdifference) + ' subscribers.'
        iconpic = "https://yt3.ggpht.com/a-/AAuE7mAPBVgUYqlLw9SvJyKAVWmgkQ2-KrkgSv4_5A=s176-c-k-c0x00ffffff-no-rj-mo"
    else:
        pdifference = int(tsubs) - int(psubs)

        def place_value(number):
            return ("{:,}".format(number))

        pdifference = (place_value(int(pdifference)))
        plead = 'T-Series leads PewDiePie by ' + str(
            pdifference) + ' subscribers.'
        iconpic = "https://yt3.ggpht.com/a-/AAuE7mBlVCRJawuU4QYf21y-Fx-cc8c9HhExSiAPtQ=s88-mo-c-c0xffffffff-rj-k-no"

    def place_value(number):
        return ("{:,}".format(number))

    psubs = (place_value(int(psubs)))
    tsubs = (place_value(int(tsubs)))

    msgtosendd = ("PewdiePie has **" + str(psubs) +
                  " subscribers**.\nT-Series has **" + str(tsubs) +
                  " subscribers**.\n\n")
    x = 0xffffff
    embed = discord.Embed(description=msgtosendd, color=x)
    embed.set_author(name=plead, icon_url=iconpic)
    #embed.set_footer(text='For best results, make sure the bot is above other ranks.')
    msgtosend = embed
    #if f == False:
    x = await client.say(embed=embed)

    #await asyncio.sleep(2)


client.loop.create_task(background_loop())

#client.loop.create_task(my_background_task())
client.run(TOKEN)

import sys

sys.exit(0)
