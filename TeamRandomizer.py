import discord
from discord.ext import commands
from discord.ext.commands import bot
import random
import requests
from io import BytesIO
import cv2
from PIL import Image

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot ready')

@client.command(pass_context = True)
async def shhelp(ctx):

    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='!team', value='Divide people in two teams (Example. !team player1 player2..)\n--f parameter overrides fair distribution', inline=False)
    embed.add_field(name='!csgo', value='Randomize gun for a round with the money you have (Example. !csgo 3600)', inline=False)
    embed.add_field(name='!pubg', value='Generates a random landing spot for PUBG (Example. !pubg Erangel)\n(Erangel, Miramar, Vikendi, Sanhok, Karakin)', inline=False)
    embed.add_field(name='!ub', value='Generate random build for user(s), Ultimate Bravery (Example. !ub)', inline=False)

    await ctx.send(embed=embed)


@client.command()
async def team(ctx, *args):
    team_one = []
    team_two = []
    force = False

    query = " ".join(args)

    if("tuomas" in query or "Tuomas" in query):
        ran = random.randint(0, 4)

        switcher = {
            0: "\nTuomas on homo",
            1: "\nTuomaksella on pieni muna",
            2: "\nTuomas tykkää rempasta",
            3: "\nTuomas on tyhmä :--D",
            4: "\nTuomaksen suussa on rempan muna xDDXDDXD"
        }

        finalmessage = switcher.get(ran)

    if("--f" in query):
        query = query.replace(" --f", "")
        query = query.replace("--f ", "")
        print(query)
        force = True

    people = query.split(" ")

    if(len(people) % 2 != 0 and force == False):
        await ctx.send(f'Not enough people to divide in two teams.')
        return

    for n in range(20):
        random.shuffle(people)
    
    for player in people:
        if(people.index(player) % 2 == 0):
            team_one.append(player)
        else:
            team_two.append(player)

    t1 = str(team_one).strip("[]")
    t2 = str(team_two).strip("[]")
    t1 = t1.replace("'", "")
    t2 = t2.replace("'", "")

    await ctx.send(f'Team 1: {t1}\nTeam 2: {t2}{finalmessage}')


@client.command()
async def csgo(ctx, *args):
    await ctx.send('Under construction')

@client.command()
async def ub(ctx):
    await ctx.send('Under construction')

@client.command()
async def pubg(ctx, map):
    try:
        image = cv2.imread(map + '.jpg')

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
        
        cv2.circle(image,(circle_x_limit, circle_y_limit), 40, (0,255,0), 3)
        cv2.imwrite("map.jpg", image)

        await ctx.send(file=discord.File('map.jpg'))

    except:
        await ctx.send(f'Learn to write correctly. (Erangel, Miramar, Vikendi, Sanhok, Karakin)')

client.run('NzM0MzcyNTgzMTA5MDMzOTg1.XxU-ZQ.U0U3YAMvgsU3i45MP0OKDsMtdEk')