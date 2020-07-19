import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot ready')

@client.command()
async def randomize(ctx, *args):
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

    t1 = str(team_one).strip("[]")
    t2 = str(team_two).strip("[]")
    t1 = t1.replace("'", "")
    t2 = t2.replace("'", "")
    await ctx.send(f'Team 1: {t1}\nTeam 2: {t2}')

client.run('NzM0MzcyNTgzMTA5MDMzOTg1.XxQv3g.4xRevABHXrpYX7Cx1-AQbmZCR9M')