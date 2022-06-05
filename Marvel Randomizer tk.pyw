from tkinter import *

import random


Schemes = [
"Age of Ultron",
"Annihilation Conquest", 
"Anti-Mutant Hatred",
"Avengers vs X-Men", 
"Build an Army of Annihilation", 
"Corrupt the Next Generation of Heroes",
"Crush them with my Bare Hands",
"Dark Alliance",
"Deadlands Hordes Charge the Wall",
"Detonate the Helicarrier",
"Divide and Conquer",
"Explosion at the Washingon Monument",
"Ferry Disaster",
"Find the Split Personality Killer",
"Five Families of Crime",
"Flood the Planet with Melted Glaciers",
"Forge the Infinity Gauntlet",
"Gladiatorial Pits of Sakaar",
"Go Back in Time to Slay Heroes Ancestors",
"Hail Hydra",
"House of M",
"Intergalactic Kree Nega-Bomb",
"Invade the Daily Guble News HQ",
"Invasion of the Venom Symbiotes",
"Massive Earthquake Generator",
"Master of Tyrants",
"Midtown Bank Robbery",
"Mutant-Hunting Super Sentinels",
"Nitro the Supervillain Threatens Crowds",
"Nuclear Armageddon",
"Organized Crime Wave",
"Pandimensional Plague",
"Reveal Heroes Secret Identities",
"S.H.I.E.L.D. vs Hydra War",
"Save Humanity",
"Scavenge Alien Weaponry",
"Secret Empire of Betrayal",
"Secret Hydra Corruption",
"Secret Invasion of the Skrull Shapeshifters",
"Shoot Hulk into Space", 
"Silence the Witnesses", 
"Smash two Dimensions Together",
"Splice Humans with Spider DNA",
"Steal the Weaponized Plutonium",
"Super Hero Civil War",
"Symbiotic Absorption",
"The Clone Saga",
"The Contest of Champions",
"The Dark Phoenix Saga",
"The Dark World of Svartalfheim",
"The Demon Bear Saga",
"The Kree-Skrull War",
"The Legacy Virus",
"The Unbreakable Enigma Code",
"Trapped in the Insane Asylum",
"Unite the Shards",
"War of the Frost Giants",
"Weave a Web of Lies",
"World War Hulk",
"X-Cutioners Song",
"X-Men Danger Room goes Berserk"
]

Masterminds = [
"Apocalypse", 
"Carnage",
"Dark Phoenix",
"Emma Frost",
"General Thunderbolt Ross",
"Hella",
"Hydra High Council",
"J. J. Jameson",
"Kingpin",
"Loki",
"Magneto",
"Malekith",
"Mr. Sinister",
"Mysterio",
"Secretary Alexander Peirce",
"Shadow King",
"Supreme Intelligence of the Kree",
"Thanos",
"The Grandmaster",
"The Hand, Secret Society",
"Ultron",
"Venom"
]

Villains = [
"Black Order of Thanos",
"Brotherhood of Mutants",
"Code Red",
"Elders of the Universe",
"Enemies of Asgard",
"Fingers of the Hand",
"Four Horsemen",
"Hellfire Club",
"Hellions",
"Hydra Elite",
"Infinity Stones",
"Kree Starforce",
"Marauders",
"Maximum Carnage",
"Omens of Ragnarok",
"S.H.I.E.L.D. Elite",
"Shadow X",
"Sinister Six",
"Skrulls",
"Spider-foes",
"Streets of New York",
"Ultron’s Legacy"
]

Henchmen = [
"Chitauri",
"Armies of Hydra",
"Hand Ninjas",
"Hellfire Cult",
"Maggia Goons",
"Outriders",
"Sentinels",
"Spider-slayers"
]

Heroes = [
"Angel",
"Ant Man",
"Beast",
"Bishop",
"Black Panther",
"Black Widow",
"Cable",
"Captain America",
"Captain Marvel",
"Colossus",
"Cyclops",
"Daredevil",
"Deadpool",
"Domino",
"Dr. Strange",
"Drax",
"Falcon",
"Gambit",
"Gamora",
"Groot",
"Hawkeye",
"Hulk",
"Hulkbuster Iron Man",
"Ice Man",
"Iron Fist",
"Iron Man",
"Iron Spider Man",
"Jean Grey",
"Jessica Jones",
"Jubilee",
"Kitty Pride",
"Korg",
"Legion",
"Loki",
"Luke Cage",
"Mantis",
"Nebula",
"Nightcrawler",
"Professor X",
"Punisher",
"Quicksilver",
"Rocket",
"Rogue",
"Scarlet Witch",
"Shang-Chi",
"Silk",
"Spider-Gwen",
"Spider-Man",
"Starlord",
"Storm",
"Thor",
"Ultimate Spider-Man",
"Vision",
"Winter Soldier",
"Wolverine"
]

vilnum = 1
hennum = 1
hernum = 1

def Player1():
    global vilnum
    global hennum
    global hernum
    vilnum = 1
    hennum = 1
    hernum = 3

def Player2():
    global vilnum
    global hennum
    global hernum
    vilnum = 1
    hennum = 1
    hernum = 5

def Player3():
    global vilnum
    global hennum
    global hernum
    vilnum = 2
    hennum = 1
    hernum = 5

def Player4():
    global vilnum
    global hennum
    global hernum
    vilnum = 2
    hennum = 2
    hernum = 5

def Randomize(tipo):
    random_item = tipo[random.randint(0,len(tipo)-1)]
    return random_item

def Randomize_lista(tipo, num):
    lista = set()
    while len(lista) < num:
        lista.add(tipo[random.randint(0,len(tipo)-1)])
    listaprint = " // ".join(lista)
    if tipo == Masterminds:
        third = random.randint(1,3)
        if third == 3:
            listaprint = "Epic {}".format(listaprint)
    return listaprint


def Show_Schemes(num):
    SchemeCont = Label(root, text="{}".format(Randomize_lista(Schemes,num)), bg="lightgreen", width=60)    
    SchemeCont.grid(row=2,column=1, columnspan=3)

def Show_Mastermind(num):
    MastermindCont = Label(root, text = "{}".format(Randomize_lista(Masterminds,num)), bg="pink", width=60)
    MastermindCont.grid(row=3, column=1, columnspan=3)

def Show_Villains(num):
    VillainCont = Label(root, text = "{}".format(Randomize_lista(Villains,num)), bg="orange", width=60)
    VillainCont.grid(row=4, column=1, columnspan=3)

def Show_Henchmen(num):
    if hernum != 3:
        HenchmenCont = Label(root, text = "{}".format(Randomize_lista(Henchmen,num)), bg="yellow", width=60)
        
    else:
        HenchmenCont = Label(root, text = "{} (only 3 cards)".format(Randomize_lista(Henchmen,num)), bg="yellow", width=60)

    HenchmenCont.grid(row=5, column=1, columnspan=3)

def Show_Heroes(num):
    HeroesCont = Label(root, text = "{}".format(Randomize_lista(Heroes,num)), bg="lightblue", width=60)
    HeroesCont.grid(row=6, column=1, columnspan=3)

def Show_Bystanders(num):
    BystandersTitle = Label(root, text = "Number of Bystanders: {}".format(num), bg="white", width=60)
    BystandersTitle.grid(row=7, column=1, columnspan=3)

def Show1Scheme():
    Show_Schemes(1)

def Show1Mastermind():
    Show_Mastermind(1)

def Show1Villain():
    Show_Villains(vilnum)

def Show1Henchman():
    Show_Henchmen(hennum)

def Show1Heroe():
    Show_Heroes(hernum)
   

def Randomize_1P():
    Player1()
    Show_Schemes(1)
    Show_Mastermind(1)
    Show_Villains(vilnum)
    Show_Henchmen(hennum)
    Show_Heroes(hernum)
    Show_Bystanders(1)

def Randomize_2P():
    Player2()
    Show_Schemes(1)
    Show_Mastermind(1)
    Show_Villains(vilnum)
    Show_Henchmen(hennum)
    Show_Heroes(hernum)
    Show_Bystanders(2)

def Randomize_3P():
    Player3()
    Show_Schemes(1)
    Show_Mastermind(1)
    Show_Villains(vilnum)
    Show_Henchmen(hennum)
    Show_Heroes(hernum)
    Show_Bystanders(8)

def Randomize_4P():
    Player4()
    Show_Schemes(1)
    Show_Mastermind(1)
    Show_Villains(vilnum)
    Show_Henchmen(hennum)
    Show_Heroes(hernum)
    Show_Bystanders(8)

def Reset():
    global vilnum
    global hennum
    global hernum
    vilnum = 1
    hennum = 1
    hernum = 1
    SchemeCont = Label(root, text= "", bg="lightgreen", width=60)
    SchemeCont.grid(row=2,column=1, columnspan=3)
    MastermindCont = Label(root, text = "", bg="pink", width=60)
    MastermindCont.grid(row=3, column=1, columnspan=3)
    VillainCont = Label(root, text = "", bg="orange", width=60)
    VillainCont.grid(row=4, column=1, columnspan=3)
    HenchmenCont = Label(root, text = "", bg="yellow", width=60)
    HenchmenCont.grid(row=5, column=1, columnspan=3)
    HeroesCont = Label(root, text = "", bg="lightblue", width=60)
    HeroesCont.grid(row=6, column=1, columnspan=3)
    BystandersTitle = Label(root, text = "", bg="white", width=60)
    BystandersTitle.grid(row=7, column=1, columnspan=3)

root = Tk()

root.title("Marvel Legendary Randomizer")
root.iconbitmap("dice.ico")
root.resizable(width=0, height=0)


PlayersTitle = Label(root, text="Choose number of Players", bg="purple", fg="white", width=75)
PlayersTitle.grid(row=0, column=0, columnspan=4)

Button1P = Button(root, text="Solo", bg="purple", fg="white", width=10, command=Randomize_1P)
Button1P.grid(row=1)

Button2P = Button(root, text="2", bg="purple", width=20, fg="white", command=Randomize_2P)
Button2P.grid(row=1, column=1)

Button3P = Button(root, text="3", bg="purple", width=20, fg="white", command=Randomize_3P)
Button3P.grid(row=1, column=2)

Button4P = Button(root, text="4", bg="purple", width=20, fg="white", command=Randomize_4P)
Button4P.grid(row=1, column=3)

SchemeTitle = Button(root, text = "Scheme:", bg="lightgreen", width=10, command=Show1Scheme)
SchemeTitle.grid(row=2, column=0)

SchemeCont = Label(root, text= "", bg="lightgreen", width=60)
SchemeCont.grid(row=2,column=1, columnspan=3)

MastermindTitle = Button(root, text = "Mastermind:", bg="pink", width=10, command=Show1Mastermind)
MastermindTitle.grid(row=3, column=0)

MastermindCont = Label(root, text = "", bg="pink", width=60)
MastermindCont.grid(row=3, column=1, columnspan=3)

VillainTitle = Button(root, text = "Villains:", bg="orange", width=10, command=Show1Villain)
VillainTitle.grid(row=4, column=0)

VillainCont = Label(root, text = "", bg="orange", width=60)
VillainCont.grid(row=4, column=1, columnspan=3)

HenchmenTitle = Button(root, text = "Henchmen:", bg="yellow", width=10, command=Show1Henchman)
HenchmenTitle.grid(row=5, column=0)

HenchmenCont = Label(root, text = "", bg="yellow", width=60)
HenchmenCont.grid(row=5, column=1, columnspan=3)

HeroesTitle = Button(root, text = "Heroes:", bg="lightblue", width=10, command=Show1Heroe)
HeroesTitle.grid(row=6, column=0)

HeroesCont = Label(root, text = "", bg="lightblue", width=60)
HeroesCont.grid(row=6, column=1, columnspan=3)

ResetButton = Button(root, text = "Reset", bg ="black", fg="white", width=10, command=Reset)
ResetButton.grid(row=7)

BystandersTitle = Label(root, text = "", bg="white", width=60)
BystandersTitle.grid(row=7, column=1, columnspan=3)



root.mainloop()

