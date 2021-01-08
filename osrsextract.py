import requests
import csv
import pandas as pd
import json
from datetime import date

def get_kc_dif(name):
    user_val = get_user_stats(name)
    user_json = json.dumps(put_to_json(user_val))

    
    with open('accountdata.json', 'r') as outfile:
        json_dict = json.load(outfile)
        for x in json_dict['players'][0]:
            if(x == name):
                with open('accountdata.json', 'w') as write_file:
                    user = json.loads(user_json)
                    json_dict['players'][0][name].append(user[name][0])
                    json.dump(json_dict, write_file)
                    write_file.write(json.dump(json_dict))


def get_user_stats(name):
    r = requests.get('https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=' + str(name).replace(' ', '_'))
    output = str(r.content).strip("b'").replace('\\n', ',')[:-1]
    today = date.today()
    final = today.strftime("%d/%m/%Y") + ',' + name + ',' + output

    return final.split(',')


def put_to_json(stats):
    final_json = {
        stats[1]:[
            {
            "date" : stats[0],
            "rank": stats[2],
            "total_level": stats[3],
            "total_xp": stats[4],
            "stats": {
                "attack": {
                "rank": stats[5],
                "level": stats[6],
                "xp": stats[7]
                },
                "defence": {
                "rank": stats[8],
                "level": stats[9],
                "xp": stats[10]
                },
                "strength": {
                "rank": stats[11],
                "level": stats[12],
                "xp": stats[13]
                },
                "hitpoints": {
                "rank": stats[14],
                "level": stats[15],
                "xp": stats[16]
                },
                "ranged": {
                "rank": stats[17],
                "level": stats[18],
                "xp": stats[19]
                },
                "prayer": {
                "rank": stats[20],
                "level": stats[21],
                "xp": stats[22]
                },
                "magic": {
                "rank": stats[23],
                "level": stats[24],
                "xp": stats[25]
                },
                "cooking": {
                "rank": stats[26],
                "level": stats[27],
                "xp": stats[28]
                },
                "woodcutting": {
                "rank": stats[29],
                "level": stats[30],
                "xp": stats[31]
                },
                "fletching": {
                "rank": stats[32],
                "level": stats[33],
                "xp": stats[34]
                },
                "fishing": {
                "rank": stats[35],
                "level": stats[36],
                "xp": stats[37]
                },
                "firemaking": {
                "rank": stats[38],
                "level": stats[39],
                "xp": stats[40]
                },
                "crafting": {
                "rank": stats[41],
                "level": stats[42],
                "xp": stats[43]
                },
                "smithing": {
                "rank": stats[44],
                "level": stats[45],
                "xp": stats[46]
                },
                "mining": {
                "rank": stats[47],
                "level": stats[48],
                "xp": stats[49]
                },
                "herblore": {
                "rank": stats[50],
                "level": stats[51],
                "xp": stats[52]
                },
                "agility": {
                "rank": stats[53],
                "level": stats[54],
                "xp": stats[55]
                },
                "thieving": {
                "rank": stats[56],
                "level": stats[57],
                "xp": stats[58]
                },
                "slayer": {
                "rank": stats[59],
                "level": stats[60],
                "xp": stats[61]
                },
                "farming": {
                "rank": stats[62],
                "level": stats[63],
                "xp": stats[64]
                },
                "runecraft": {
                "rank": stats[65],
                "level": stats[66],
                "xp": stats[67]
                },
                "hunter": {
                "rank": stats[68],
                "level": stats[69],
                "xp": stats[70]
                },
                "construction": {
                "rank": stats[71],
                "level": stats[72],
                "xp": stats[73]
                }
            },
            "misc": {
                "rank_league": stats[74],
                "points_league": stats[75],
                "rank_bountyhunter_hunter": stats[76],
                "points_bountyhunter_hunter": stats[77],
                "rank_bountyhunter_rogue": stats[78],
                "points_bountyhunter_rogue": stats[79],
                "clues": {
                "rank_clues_total": stats[80],
                "total_clues": stats[81],
                "rank_beginner_clue": stats[82],
                "total_beginner": stats[83],
                "rank_easy_clue": stats[84],
                "total_easy": stats[85],
                "rank_medium_clue": stats[86],
                "total_medium": stats[87],
                "rank_hard_clue": stats[88],
                "total_hard": stats[89],
                "rank_elite_clue": stats[90],
                "total_elite": stats[91],
                "rank_master_clue": stats[92],
                "total_master": stats[93]
                },
                "rank_lms": stats[94],
                "points_lms": stats[95]
            },
            "bosses": {
                "rank_sire": stats[96],
                "kc_sire": stats[97],
                "rank_hydra": stats[98],
                "kc_hydra": stats[99],
                "rank_barrows": stats[100],
                "kc_barrows": stats[101],
                "rank_bryophyta": stats[102],
                "kc_bryophyta": stats[103],
                "rank_callisto": stats[104],
                "kc_callisto": stats[105],
                "rank_cerberus": stats[106],
                "kc_cerberus": stats[107],
                "rank_CoX": stats[108],
                "kc_CoX": stats[109],
                "rank_CoX_CM": stats[110],
                "kc_CoX_CM": stats[111],
                "rank_chaos_elemental": stats[112],
                "kc_chaos_elemental": stats[113],
                "rank_chaos_fanatic": stats[114],
                "kc_chaos_fanatic": stats[115],
                "rank_saradomin": stats[116],
                "kc_saradomin": stats[117],
                "rank_corporal_beast": stats[118],
                "kc_corporal_beast": stats[119],
                "rank_crazy_archaeologist": stats[120],
                "kc_crazy_archaeologist": stats[121],
                "rank_prime": stats[122],
                "kc_prime": stats[123],
                "rank_rex": stats[124],
                "kc_rex": stats[125],
                "rank_supreme": stats[126],
                "kc_supreme": stats[127],
                "rank_deranged_archaeologist": stats[128],
                "kc_deranged_archaeologist": stats[129],
                "rank_bandos": stats[130],
                "kc_bandos": stats[131],
                "rank_giant_mole": stats[132],
                "kc_giant_mole": stats[133],
                "rank_grotesque_guardians": stats[134],
                "kc_grotesque_guardians": stats[135],
                "rank_hespori": stats[136],
                "kc_hespori": stats[137],
                "rank_KQ": stats[138],
                "kc_KQ": stats[139],
                "rank_KBD": stats[140],
                "kc_KBD": stats[141],
                "rank_kraken": stats[142],
                "kc_kraken": stats[143],
                "rank_armadyl": stats[144],
                "kc_armadyl": stats[145],
                "rank_zamorak": stats[146],
                "kc_zamorak": stats[147],
                "rank_mimic": stats[148],
                "kc_mimic": stats[149],
                "rank_nightmare": stats[150],
                "kc_nightmare": stats[151],
                "rank_obor": stats[152],
                "kc_obor": stats[153],
                "rank_sarachnis": stats[154],
                "kc_sarachnis": stats[155],
                "rank_scorpia": stats[156],
                "kc_scorpia": stats[157],
                "rank_skotizo": stats[158],
                "kc_skotizo": stats[159],
                "rank_gauntlet": stats[160],
                "kc_gauntlet": stats[161],
                "rank_corrupted_gauntlet": stats[162],
                "kc_corrupted_gauntlet": stats[163],
                "rank_ToB": stats[164],
                "kc_ToB": stats[165],
                "rank_thermy": stats[166],
                "kc_thermy": stats[167],
                "rank_inferno": stats[168],
                "kc_inferno": stats[169],
                "rank_fight_caves": stats[170],
                "kc_fight_caves": stats[171],
                "rank_venenatis": stats[172],
                "kc_venenatis": stats[173],
                "rank_vetion": stats[174],
                "kc_vetion": stats[175],
                "rank_vorkath": stats[176],
                "kc_vorkath": stats[177],
                "rank_wintertodt": stats[178],
                "kc_wintertodt": stats[179],
                "rank_zalcano": stats[180],
                "kc_zalcano": stats[181],
                "rank_zulrah": stats[182],
                "kc_zulrah": stats[183]
            }
        }
    ]}
    return final_json

get_kc_dif("Genuine Elf")