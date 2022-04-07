#!/usr/bin/python3
import random


def primary_attack_roll():
    primary_attack_roll = random.randrange(1, 11)
    return primary_attack_roll
def secondary_attack_roll():
    secondary_attack_roll = random.randrange(1, 7)
    return secondary_attack_roll
def defense_roll():
    defense_roll = random.randrange(1, 7)*2
    return defense_roll

primary_attack_roll()
secondary_attack_roll()
defense_roll()