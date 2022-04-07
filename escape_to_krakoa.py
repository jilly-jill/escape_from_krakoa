#!/usr/bin/python3


import dice
import time


location = ""
char_sel = ""
char = ""
char_dict = {'Magneto': {'Primary': 'Magnetism', 'Secondary': 'Intelligence', 'Trait': 'Drama Queen', 'Health': str(40)},
             'Wolverine': {'Primary': 'Regeneration ', 'Secondary': 'Persistence ',
                           'Trait': 'Lack of Concern for the Opinions of Authority or Others', 'Health': str(60)},
             'Legion': {'Primary': 'Telepathy ', 'Secondary': 'Telekenesis ', 'Trait': 'Lots of Support from the Voices In Their Head',
                        'Health': str(50)},
             'Storm': {'Primary': 'Weather Manipulation ', 'Secondary': 'Leadership ', 'Trait': 'Doing it Effortlessly & with Style',
                       'Health': str(50)}
             }


def run():
    print("run")


def win():
    print(f"Congratulations {char_sel}! You arrived at Krakoa!")


def lose():
    print(f"{char_sel}, you were unfortunately unable to overcome the overwhelming human forces - luckily, there's Krakoan resurrection. \n" +
          "See you in Krakoa..")


def fight():
    p_health = int(char_dict[char].get("Health"))
    print("You turn to fight- and immediately lead to strike.\n")
    count = 0
    while count < 3:
        attack_begin = input("Which attack do you use? Select 'P' for primary or 'S' for secondary: \n" +
                         "(Press 'T' to escape)\n" + "\n").upper()
        if attack_begin == 'P' or attack_begin == 'S':
            mutant_primary = dice.primary_attack_roll()
            cpu_defense = dice.defense_roll()
            mutant_secondary = dice.secondary_attack_roll()
            primary = (char_dict[char].get('Primary'))
            secondary = (char_dict[char].get('Secondary'))

        if attack_begin == 'P':
            if mutant_primary > cpu_defense:
                calc_damage = mutant_primary - cpu_defense
                cd = str(calc_damage)    
                print(f"You attack with, {primary} \n",
                      "The attack was SUCCESSFUL!\n",
                      f"{char} dealt {cd} damage!\n",
                      f"{char} Health: {p_health}  \n",)
                        
            elif mutant_primary == cpu_defense:
                print(f"{char} it's a deadlock! You need to strike again!\n")
            
        else:
            calc_damage = (cpu_defense - mutant_primary)
            p_health =- (calc_damage)
            print(f"{char} attacks with {primary}\n",
                    "The attack was UNSUCCESSFUL!\n",
                    f"{char}  was dealt {calc_damage} damage!\n",
                    f"{char} Health: {p_health}\n")
            
        if attack_begin == 'S':
            if mutant_secondary > cpu_defense:
                calc_damage = (mutant_secondary - cpu_defense)
                cd = str(calc_damage)
                print(f"{char} attacks with {secondary}\n")
                time.sleep(3)
                print("The attack was SUCCESSFUL!\n",
                      f"{char} dealt {cd} damage!\n",
                      f"{char} Health: {p_health}\n")
            elif mutant_secondary == cpu_defense:
                print(f"{char} it's a deadlock! You need to strike again!\n")
        else:
            calc_damage = (cpu_defense - mutant_secondary)
            health =- (calc_damage)
            cd = str(calc_damage)
            print(f"{char} attacks with {secondary}\n")
            # time.sleep(3)
            print("The attack was UNSUCCESSFUL!\n",
                      f"{char_sel}  was dealt {cd} damage!\n",
                      f"{char_sel} Health: {p_health}\n")
        if attack_begin == 'T':
            run()
    
    count =+ 1    

    if p_health <= 0:
        lose()


def story():
    z = time.sleep(10)
    y = time.sleep(5)
    x = time.sleep(3)
    # time.sleep(10)
    print("You step outside of your apartment with your bags packed and begin walking down the street.\n" +
          "Keenly aware of your surroundings you feels eyes on you and pause your walk.\n")
    z
    print("You feel the eyes on your back\n")
    z
    
    print("The hair on your neck stands-up as you brace yourself\n")
    y    
    narr = input(f"LOOK OUT! You're being attacked! Ms. Halsey from apartment 3B is running at you full speed with a fleet of Sentinels behind her.\n" +
                 f"For all this time, she was keeping an eye on you waiting for you to make a move. What do you do?\n" +
                 f"Enter 'F' for Fight and 'R' for Run\n").upper()
    if narr == 'F':
        fight()
    elif narr == 'R':
        run()
    else:
        input("Please select either 'F' for fight or 'R' to run")


def character_select():
    # call global variables to be set by user input
    global char_dict
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
    primary = char_dict[char].get('Primary')
    secondary = char_dict[char].get('Secondary')
    trait = char_dict[char].get('Trait')
    health = char_dict[char].get('Health')

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
user_choice = input("Are you ready for the adventure? Y or N")
if user_choice == "Y":
    escape_from_krakoa()
else:
    print("Krakoa will be waiting")
