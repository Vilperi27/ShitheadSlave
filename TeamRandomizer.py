import discord
from discord.ext import commands
from discord.ext.commands import bot
import random
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import time
import os.path
from os import path
from discord.utils import find

import requests

client = commands.Bot(command_prefix='!')

nl = open('nounlist.txt')
noun_list = []

for line in nl:
    sl = line.strip()
    noun_list.append(sl)

@client.event
async def on_ready():
    print('Bot ready')

@client.event
async def on_member_join(member):

    name = noun_list[random.randint(0, len(noun_list))]
    general = find(lambda x: x.name == 'yleinen',  discord.Guild.text_channels)
    if general and general.permissions_for(discord.Guild.me).send_messages:
        await general.send('Welcome! The Elf ' + name.title() + '!')
        await member.edit(nick='The Elf ' + name.title())

@client.command(pass_context=True)
@commands.has_role('Royal')
async def rollnames(ctx):

    for member in ctx.guild.members:
        try:
            await member.edit(nick='The Elf ' + noun_list[random.randint(0, len(noun_list))].title())               
        except:
            pass

@client.command(pass_context=True)
async def reroll(ctx):
    await ctx.author.edit(nick='The Elf ' + noun_list[random.randint(0, len(noun_list))].title()) 

@client.command(pass_context = True)
async def shhelp(ctx):

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='!team', value='Divide people in two teams (Example. !team player1 player2..)\n--f parameter overrides fair distribution', inline=False)
    embed.add_field(name='!csgo', value='Randomize gun for a round with the money you have (Example. !csgo 3600)', inline=False)
    embed.add_field(name='!pubg', value='Generates a random landing spot for PUBG (Example. !pubg Erangel)\n(Erangel, Miramar, Vikendi, Sanhok, Karakin)', inline=False)
    embed.add_field(name='!ub', value='Generate random build for user(s), Ultimate Bravery\n(Example. !ub sr player1 player2..)\nMap parameters:\nAram: a\nSummoners rift: sr', inline=False)

    await ctx.send(embed=embed)


@client.command()
async def team(ctx, *args):
    force = False

    query = " ".join(args)

    if("--f" in query):
        query = query.replace(" --f", "")
        query = query.replace("--f ", "")
        print(query)
        force = True

    people = query.split(" ")

    if(len(people) % 2 != 0 and force == False):
        await ctx.send(f'Not enough people to divide in two teams.')
        return


    t1, t2 = randomize_team(people)

    await ctx.send(f'Team 1: {t1}\nTeam 2: {t2}')


def randomize_team(people):

    team_one = []
    team_two = []

    for n in range(20):
        random.shuffle(people)
    
    for player in people:
        if(people.index(player) % 2 == 0):
            team_one.append(player)
        else:
            team_two.append(player)

    t1 = str(team_one).strip("[]").replace("'", "")
    t2 = str(team_two).strip("[]").replace("'", "")

    return t1, t2


@client.command()
async def csgo(ctx, side):

    f=open("CSGOstratroulette.txt", "r")
    contents = f.readlines()

    if(side.lower() == "t"):
        await ctx.send(contents[random.randint(0,96)])

    elif(side.lower() == "ct"):
        await ctx.send(contents[random.randint(98,180)])

    else:
        await ctx.send('How do you not manage to write t or ct???')

def get_picture(json_partition, prefix):
    imgholder = json_partition
    imgholderstr = imgholder.split(prefix, 1)[1]
    
    if(path.exists('Graphics/' + imgholderstr)):
        return Image.open('Graphics/' + imgholderstr)
    else:
        var = Image.open(BytesIO(requests.get(imgholder).content))
        var.save('Graphics/' + imgholderstr)
        return var

def is_empty(any_structure):
    if any_structure:
        return False
    else:
        return True


@client.command()
async def ub(ctx, map, *args):

    if(is_empty(args)):
        user_amount = 1
        author = str(ctx.message.author).split('#',1)[0]
        args = args + (author,)

    user_amount = len(args)
    users = args

    image_build = Image.new('RGB', ((450, 200*(user_amount))))
    
    mapid = 11

    if(user_amount % 2 == 0):
        t1, t2 = randomize_team(list(users))

    if(map=='sr'):
        mapid = 11
    elif(map == 'a'):
        mapid = 12
    
    for x in range(user_amount):
        r = requests.post('https://api2.ultimate-bravery.net/bo/api/ultimate-bravery/v1/dataset', json = {"map":mapid,"level":30,"language":"en","roles":[0,1,2,3,4],"champions":[266,103,84,12,32,34,1,523,22,136,268,432,53,63,201,51,164,69,31,42,122,131,119,36,245,60,28,81,9,114,105,3,41,86,150,79,104,120,74,420,39,427,40,59,24,126,202,222,145,429,43,30,38,55,10,141,85,121,203,240,96,7,64,89,127,236,117,99,54,90,57,11,21,62,82,25,267,75,111,518,76,56,20,2,61,516,80,78,555,246,133,497,33,421,58,107,92,68,13,113,235,875,35,98,102,27,14,15,72,37,16,50,517,134,223,163,91,44,17,412,18,48,23,4,29,77,6,110,67,45,161,254,112,8,106,19,498,101,5,157,83,350,154,238,115,26,142,143]}, headers = {'Content-type':'application/json'})
        ubdata = r.json()

        
        image_build.paste(Image.open('Graphics/background.png'), (0, x * 200))
        title = ""
        champion_name = None
        ability = None
        spell_one = None
        spell_two = None
        
        title = ubdata['data']['title']

        champion_name = get_picture(ubdata['data']['champion']['image'], 'champion/')

        ability = get_picture(ubdata['data']['champion']['spell']['image'], 'spell/')

        champion_name.thumbnail((60, 60), Image.ANTIALIAS)
        image_build.paste(champion_name, (5, x * 200 + 5))

        ability.thumbnail((60, 60), Image.ANTIALIAS)
        image_build.paste(ability, (380, x * 200 + 70))

        draw = ImageDraw.Draw(image_build)
        font = ImageFont.truetype('arial.ttf', 20)
        draw.text((80, x * 200 + 25), '{0}, The {1}'.format(users[x], title), font=font)

        count = 0

        for key in ubdata['data']['summonerSpells']:
            value = ubdata['data']['summonerSpells'][key]

            if(count == 0):
                spell_one = get_picture(value, 'spell/')
                spell_one.thumbnail((30, 30), Image.ANTIALIAS)
                image_build.paste(spell_one, (380, x * 200 + 40))
            else:
                spell_two = ability = get_picture(value, 'spell/')
                spell_two.thumbnail((30, 30), Image.ANTIALIAS)
                image_build.paste(spell_two, (410, x * 200 + 40))
            
            count = 1

        count = 0

        for key in ubdata['data']['items']:
            value = ubdata['data']['items'][key]
            item_picture = get_picture(value, 'item/')
            item_picture.thumbnail((60, 60), Image.ANTIALIAS)
            image_build.paste(item_picture, (5 + (count * 60), x * 200 + 70))
            count = count + 1

        count = 0

        for key in ubdata['data']['runes']['primary']:
            value = ubdata['data']['runes']['primary'][key]

            item_picture = get_picture('https://ultimate-bravery.net/images/runes/' + value, 'runes/')
            item_picture.thumbnail((30, 30), Image.ANTIALIAS)
            if(count == 0):
                image_build.paste(item_picture, (5, x * 200 + 135))
            else:
                image_build.paste(item_picture, (5 * count + (count * 30), x * 200 + 135))

            count = count + 1

        count = 0
        
        for key in ubdata['data']['runes']['secondary']:
            value = ubdata['data']['runes']['secondary'][key]
            item_picture = get_picture('https://ultimate-bravery.net/images/runes/' + value, 'runes/')
            item_picture.thumbnail((30, 30), Image.ANTIALIAS)
            if(count == 0):
                image_build.paste(item_picture, (5, x * 200 + 165))
            else:
                image_build.paste(item_picture, (5 * count + (count * 30), x * 200 + 165))

            count = count + 1

        for key in ubdata['data']['runes']['stats']:
            item_picture = get_picture('https://ultimate-bravery.net/images/rune-stats/' + key['image'], 'rune-stats/')
            item_picture.thumbnail((30, 30), Image.ANTIALIAS)

            if(count == 0):
                image_build.paste(item_picture, (5, x * 200 + 165))
            else:
                image_build.paste(item_picture, (5 * count + (count * 30), x * 200 + 165))

            count = count + 1


        image_build.save('datasetbuild.png')

    await ctx.send(file=discord.File('datasetbuild.png'))
    
    image_build.close()

    if(user_amount % 2 == 0):
        await ctx.send(f'Team 1: {t1}\nTeam 2: {t2}')



@client.command()
async def pubg(ctx, map):
    try:

        circle_x_limit = 0
        circle_y_limit = 0

        if(map == "Erangel"):
            circle_x_limit = random.randint(50, 900)
            circle_y_limit = random.randint(150, 900)
        elif(map == "Miramar"):
            circle_x_limit = random.randint(150, 850)
            circle_y_limit = random.randint(80, 900)
        elif(map == "Karakin"):
            circle_x_limit = random.randint(160, 840)
            circle_y_limit = random.randint(180, 830)
        elif(map == "Sanhok"):
            circle_x_limit = random.randint(190, 870)
            circle_y_limit = random.randint(210, 940)
        elif(map == "Vikendi"):
            circle_x_limit = random.randint(210, 830)
            circle_y_limit = random.randint(165, 810)
        
        image = Image.open(map + '.jpg')

        draw = ImageDraw.Draw(image)
        draw.ellipse((circle_x_limit, circle_y_limit, circle_x_limit + 80, circle_y_limit + 80), width = 5, outline = (0, 255, 0, 255))
        image.save('map.jpg')

        await ctx.send(file=discord.File('map.jpg'))

    except:
        await ctx.send(f'Learn to write correctly. (Erangel, Miramar, Vikendi, Sanhok, Karakin)')

client.run('NzM0MzcyNTgzMTA5MDMzOTg1.XxU-ZQ.U0U3YAMvgsU3i45MP0OKDsMtdEk')   #Official Shitheads Slave