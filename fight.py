#!/usr/bin/python3
import dice
import mutants

def fight():
    health = health()
    print("You turn to fight- and immediately lead to strike.\n")
    
    count = 0
    while count < 3:
        attack_begin = input("Which attack do you use? Select 'P' for primary or 'S' for secondary: \n" +
                         "(Press 'T' to escape)\n" + "\n").upper()
        if attack_begin == 'P' or attack_begin == 'S':
            mutant_primary = dice.primary_attack_roll()
            cpu_defense = dice.defense_roll()
            mutant_secondary = dice.secondary_attack_roll()
            primary = (mutants.char_dict[char].get('Primary'))
            secondary = (mutants.char_dict[char].get('Secondary'))
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
                timedelay.time.sleep(13)
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
            # timedelay.time.sleep(13)
            print("The attack was UNSUCCESSFUL!\n",
                      f"{char_sel}  was dealt {cd} damage!\n",
                      f"{char_sel} Health: {p_health}\n")
        if attack_begin == 'T':
            run()
    
    count =+ 1    

    if p_health <= 0:
        lose()
