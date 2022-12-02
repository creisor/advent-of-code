#!/usr/bin/env python3

import argparse

class Round(object):
    """A round of Rock, Paper, Scissors"""

    def __init__(self, player_1: object, player_2: object):
        self.player_1 = player_1 
        self.player_2 = player_2 

    def print(self):
        print(self.player_1)
        print(self.player_2)
        print(f'does player_1 ({self.player_1}) beat player_2 ({self.player_2})? {self.player_1 > self.player_2}')


class Rock(object):
    """A rock defeats scissors"""

    def __str__(self):
        return "rock"

    def __gt__(self, other):
        if isinstance(other, Scissors):
            return True
        return False

    def __lt__(self, other):
        if not isinstance(other, Paper):
            return False
        return True

class Paper(object):
    """A piece of paper defeats rock"""


class Scissors(object):
    """A pair of scissors defeats paper"""

def code_to_object(code: str):
    code_map = {
        'A': Rock(),
        'B': Paper(),
        'C': Scissors(),
        'X': Rock(),
        'Y': Paper(),
        'Z': Scissors(),
    }

    return code_map[code.upper()]

def main():
    #parser = argparse.ArgumentParser(
    #    prog = 'day2',
    #    description = 'Advent of Code 2022: Day 2 ')

    #parser.add_argument('skeleton')
    #parser.add_argument('-n', '--number', default=1, type=int, help='help about -n')
    #args = parser.parse_args()

    player_1 = code_to_object('A')
    player_2 = code_to_object('Y')

    round1 = Round(player_1, player_2)
    round1.print()

if __name__ == "__main__":
    main()
