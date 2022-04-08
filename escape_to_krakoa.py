#!/usr/bin/python3


import dice
import mutants
import timedelay
import os

os.system("clear")

location = ""
char_sel = ""
char = ""

#win function
def win():
    print(f"Congratulations {char_sel}! You arrived at Krakoa!")

#lose function
def lose():
    print(f"{char_sel}, you were unfortunately unable to overcome the overwhelming human forces - luckily, there's Krakoan resurrection. \n" +
          "See you in Krakoa..")

#run function (in dev)
# def run():
#     print("run")
#     win()

#health function (in dev)
# def health():
#     start_health = mutants.char_dict[char].get('Health')
#     return start_health


def fight():
    print("You turn to fight- and immediately lead to strike.\n")
    count = 0
    while count < 3:
        attack_begin = input("Which attack do you use? Select 'P' for primary or 'S' for secondary: \n" + "\n").upper()
        #roll mutant dice - heavy
        mutant_primary = dice.primary_attack_roll()
        #roll defense dice
        cpu_defense = dice.defense_roll()
        #roll defense dice - light
        mutant_secondary = dice.secondary_attack_roll()
        #set primary and secondary attacks variables for selected char
        primary = (mutants.char_dict[char].get('Primary'))
        secondary = (mutants.char_dict[char].get('Secondary'))
        if attack_begin == 'P': #if heavy
            if mutant_primary > cpu_defense: #if mutant roll higer than cpu roll
                calc_damage = mutant_primary - cpu_defense #calculate damage
                cd = str(calc_damage)    #stringify damage
                print(f"You attack with, {primary} \n",
                      "The attack was SUCCESSFUL!\n",
                      f"{char} dealt {cd} damage!\n",
                      f"{char} Health: {p_health}  \n",)
            elif mutant_primary == cpu_defense: #if tie
                print(f"{char} it's a deadlock! You need to strike again!\n")
            else:
                calc_damage = (cpu_defense - mutant_primary) #if cpu roll higher than mutant roll
                p_health =- (calc_damage) #calc damage
                print(f"{char} attacks with {primary}\n",
                    "The attack was UNSUCCESSFUL!\n",
                    f"{char}  was dealt {calc_damage} damage!\n",
                    f"{char} Health: {p_health}\n")
            
        if attack_begin == 'S': #secondary attack
            if mutant_secondary > cpu_defense: #if mutant roll higher than cpu roll
                calc_damage = (mutant_secondary - cpu_defense) #calc damage
                cd = str(calc_damage) #stringify damage
                print(f"{char} attacks with {secondary}\n")
                print("The attack was SUCCESSFUL!\n",
                      f"{char} dealt {cd} damage!\n",
                      f"{char} Health: {p_health}\n")
            elif mutant_secondary == cpu_defense: #if tie
                print(f"{char} it's a deadlock! You need to strike again!\n")
            else:
                calc_damage = (cpu_defense - mutant_secondary) #if cpu roll higher than mutant / calc damage
                cd = str(calc_damage) #stringify
                print(f"{char} attacks with {secondary}\n")
                print("The attack was UNSUCCESSFUL!\n",
                      f"{char_sel}  was dealt {cd} damage!\n",
                      f"{char_sel} Health: {p_health}\n")
        count =+ 1
        if count >= 3:
            break    

def story():
    print("You step outside of your apartment with your bags packed and begin walking down the street.\n" +
          "Keenly aware of your surroundings you feels eyes on you and pause your walk.\n")
    print("You feel the eyes on your back\n")
    print("The hair on your neck stands-up as you brace yourself\n")
    narr = input(f"LOOK OUT! You're being attacked! Ms. Halsey from apartment 3B is running at you full speed with a fleet of Sentinels behind her.\n" +
                 f"For all this timedelay.time, she w1as keeping an eye on you waiting for you to make a move. What do you do?\n" +
                 f"Enter 'F' for Fight and 'R' for Run\n").upper()
    if narr == 'F':
        fight()
    else:
        input("Please select either 'F' for fight or 'R' to run")
    

def character_select():
    # call global variables to be set by user input
    global mutants
    global location
    global char_sel
    global char

    # set mutant name - placed in while loop that is continued only if the user fails to place a name
    char_sel = input("Please choose a mutant name: ").capitalize()
    while char_sel == "":
        char_sel = input("Please choose a mutant name")
    # set mutant location if left blank, auto-assigned new York
    location = input("Where are you fleeing from? ")
    if location == "":
        location = "New York"
    else:
        location == location

    # choose mutant who's powers to mimic
    pwr_sel = input("Please choose a character who's powers you would most desire: \n" +
                    "   - Magneto\n" +
                    "   - Wolverine\n" +
                    "   - Legion\n" +
                    "   - Storm\n").capitalize()
    while pwr_sel == "":
        pwr_sel = input("Please choose a character who's powers you would most desire: \n" +
                        "   - Magneto\n" +
                        "   - Wolverine\n" +
                        "   - Legion\n" +
                        "   - Storm\n").capitalize()

    # created dictionaries for each mutant powers for user to then have set as their own
    char = pwr_sel
    primary = mutants.char_dict[char].get('Primary')
    secondary = mutants.char_dict[char].get('Secondary')
    trait = mutants.char_dict[char].get('Trait')
    health = mutants.char_dict[char].get('Health')

    print(f"\n{char_sel}, you are fleeing from {location} and trying to reach the mutant-homeland of Krakoa.\n" +
          f"Although facing certain hostilities from humans. You are able to use your mutant powers in spite of power dampeners.\n" +
          f"Humans have been made aware via lists and reporting of neighbors and community members who are mutants.\n" +
          f"This means {char_sel}, you are in danger while trying to reach the gate. It will be a tenuous journey but the destination will be well worth the peril.\n" + "\n" +
          f"Current Stats for {char_sel}:\n" + "\n" +
          f"{char_sel} Powers:\n" +
          f"    Primary: {primary}\n" +
          f"    Secondary: {secondary}\n" +
          f"    Trait: {trait}\n" + "\n" +
          f"{char_sel} Health Level:\n" +
          f"    Health: {health}\n" + "\n")

    return char and primary and secondary and trait and health


def escape_from_krakoa():
    character_select()
    story()


print("The world is changing and the mutant paradise of Krakoa is growing - you are desperately seeking an escape to the island\n" +
      "but you first have to reach one of the Krakoan gates.\n")
user_choice = input("Are you ready for the adventure? Y or N\n").capitalize()
if user_choice == "Y":
    escape_from_krakoa()
else:
    print("Krakoa will be waiting")
