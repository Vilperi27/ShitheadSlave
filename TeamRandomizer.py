import discord
from discord.ext import commands
from discord.ext.commands import bot
import random
from io import BytesIO
from PIL import Image, ImageDraw

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

    t1 = str(team_one).strip("[]").replace("'", "")
    t2 = str(team_two).strip("[]").replace("'", "")

    await ctx.send(f'Team 1: {t1}\nTeam 2: {t2}')


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

@client.command()
async def ub(ctx):
    await ctx.send('Under construction')

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
#client.run('NzM0NDcwMTg2NTg4OTYyODc3.XxaCow.x6WIuJlx6lyxefPaioYoInoydtc')   #Test Environment