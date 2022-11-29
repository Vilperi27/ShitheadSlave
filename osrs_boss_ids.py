import random


slayer_boss_list = {
    "Grotesque Guardians": (75, "https://oldschool.runescape.wiki/w/Grotesque_Guardians"),
    "Abyssal Sire": (85, "https://oldschool.runescape.wiki/w/Abyssal_Sire"),
    "Kraken": (87, "https://oldschool.runescape.wiki/w/Kraken"),
    "Cerberus": (91, "https://oldschool.runescape.wiki/w/Cerberus"),
    "Thermonuclear smoke devil": (93, "https://oldschool.runescape.wiki/w/Thermonuclear_smoke_devil"),
    "Alchemical Hydra": (95, "https://oldschool.runescape.wiki/w/Alchemical_Hydra")
}

monster_list = {
    "Chaos Fanatic": (0, "https://oldschool.runescape.wiki/w/Chaos_Fanatic"),
    "Crazy archaeoloist": (0, "https://oldschool.runescape.wiki/w/Crazy_archaeologist"),
    "Scorpia": (0, "https://oldschool.runescape.wiki/w/Scorpia"),
    "King Black Dragon": (0, "https://oldschool.runescape.wiki/w/King_Black_Dragon"),
    "Chaos Elemental": (0, "https://oldschool.runescape.wiki/w/Chaos_Elemental"),
    "Vet'ion": (0, "https://oldschool.runescape.wiki/w/Vet%27ion"),
    "Venenatis": (0, "https://oldschool.runescape.wiki/w/Venenatis"),
    "Callisto": (0, "https://oldschool.runescape.wiki/w/Callisto"),
    "Obor": (0, "https://oldschool.runescape.wiki/w/Obor"),
    "Bryophyta": (0, "https://oldschool.runescape.wiki/w/Bryophyta"),
    "Tempoross": (0, "https://oldschool.runescape.wiki/w/Tempoross"),
    "Wintertodt": (0, "https://oldschool.runescape.wiki/w/Wintertodt"),
    "Zalcano": (0, "https://oldschool.runescape.wiki/w/Zalcano"),
    "Chambers of Xeric": (0, "https://oldschool.runescape.wiki/w/Chambers_of_Xeric"),
    "Theatre of Blood": (0, "https://oldschool.runescape.wiki/w/Theatre_of_Blood"),
    "Tombs of Amascut": (0, "https://oldschool.runescape.wiki/w/Tombs_of_Amascut"),
    "Gauntlet": (0, "https://oldschool.runescape.wiki/w/The_Gauntlet"),
    "TzTok-Jad": (0, "https://oldschool.runescape.wiki/w/TzTok-Jad"),
    "TzKal-Zuk": (0, "https://oldschool.runescape.wiki/w/TzKal-Zuk"),
    "Barrows": (0, "https://oldschool.runescape.wiki/w/Barrows"),
    "Giant Mole": (0, "https://oldschool.runescape.wiki/w/Giant_Mole"),
    "Deranged Archaeologist": (0, "https://oldschool.runescape.wiki/w/Deranged_Archaeologist"),
    "Dagannoth Kings": (0, "https://oldschool.runescape.wiki/w/Dagannoth_Kings"),
    "Sarachnis": (0, "https://oldschool.runescape.wiki/w/Sarachnis"),
    "Kalphite Queen": (0, "https://oldschool.runescape.wiki/w/Kalphite_Queen"),
    "Kree'arra (Armadyl)": (0, "https://oldschool.runescape.wiki/w/Kree%27arra"),
    "Commander Zilyana (Saradomin)": (0, "https://oldschool.runescape.wiki/w/Commander_Zilyana"),
    "General Graardor (Bandos)": (0, "https://oldschool.runescape.wiki/w/General_Graardor"),
    "K'ril Tsutsaroth (Zamorak)": (0, "https://oldschool.runescape.wiki/w/K%27ril_Tsutsaroth"),
    "Zulrah": (0, "https://oldschool.runescape.wiki/w/Zulrah"),
    "Vorkath": (0, "https://oldschool.runescape.wiki/w/Vorkath"),
    "Corporeal Beast": (0, "https://oldschool.runescape.wiki/w/Corporeal_Beast"),
    "The Nightmare": (0, "https://oldschool.runescape.wiki/w/The_Nightmare"),
    "Nex": (0, "https://oldschool.runescape.wiki/w/Nex"),
}

def get_random_boss(slayer_level=99):
    boss_list = monster_list

    for boss in slayer_boss_list:
        if slayer_level >= slayer_boss_list[boss][0]:
            boss_list.update({boss: slayer_boss_list[boss]})

    chosen_boss = random.choice(list(boss_list))
    chosen_boss_details = (chosen_boss, monster_list[chosen_boss][1])
    return chosen_boss_details