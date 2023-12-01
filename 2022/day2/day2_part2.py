#!/usr/bin/env python3

import argparse

class Player(object):
    def __init__(self, name: str, choice: object):
        self.name = name
        self.choice = choice
        self.score = 0


class Round(object):
    """A round of Rock, Paper, Scissors"""

    def __init__(self, player_1: object, player_2: object):
        self.player_1 = player_1 
        self.player_2 = player_2 
        self.points = {
            'lose': 0,
            'win': 6,
            'draw': 3
        }

    def play(self, verbose=False):
        if verbose:
            print(f'{self.player_1.name} chose {self.player_1.choice}')
            print(f'{self.player_2.name} chose {self.player_2.choice}')

        if self.player_1.choice == self.player_2.choice:
            if verbose:
                print('Draw')
            self.player_1.score = self.player_1.choice.points + self.points['draw']
            self.player_2.score = self.player_2.choice.points + self.points['draw']
            return

        if self.player_1.choice > self.player_2.choice:
            if verbose:
                print(f'{self.player_1.name} beats {self.player_2.name} ({self.player_1.choice} beats {self.player_2.choice})')
            self.player_1.score = self.player_1.choice.points + self.points['win']
            self.player_2.score = self.player_2.choice.points + self.points['lose']

        else:
            if verbose:
                print(f'{self.player_2.name} beats {self.player_1.name} ({self.player_2.choice} beats {self.player_1.choice})')
            self.player_1.score = self.player_1.choice.points + self.points['lose']
            self.player_2.score = self.player_2.choice.points + self.points['win']


class Rock(object):
    """A rock defeats scissors"""

    def __str__(self):
        return "rock"

    def __eq__(self, other):
        if isinstance(other, Rock):
            return True
        return False

    def __gt__(self, other):
        if isinstance(other, Scissors):
            return True
        return False

    def __lt__(self, other):
        if not isinstance(other, Paper):
            return False
        return True

    @property
    def points(self):
        return 1

    @property
    def lose(self):
        return Scissors()

    @property
    def draw(self):
        return Rock()

    @property
    def win(self):
        return Paper()

class Paper(object):
    """A piece of paper defeats rock"""

    def __str__(self):
        return "paper"

    def __eq__(self, other):
        if isinstance(other, Paper):
            return True
        return False

    def __gt__(self, other):
        if isinstance(other, Rock):
            return True
        return False

    def __lt__(self, other):
        if isinstance(other, Scissors):
            return False
        return True

    @property
    def points(self):
        return 2

    @property
    def lose(self):
        return Rock()

    @property
    def draw(self):
        return Paper()

    @property
    def win(self):
        return Scissors()

class Scissors(object):
    """A pair of scissors defeats paper"""

    def __str__(self):
        return "scissors"

    def __eq__(self, other):
        if isinstance(other, Scissors):
            return True
        return False

    def __gt__(self, other):
        if isinstance(other, Paper):
            return True
        return False

    def __lt__(self, other):
        if isinstance(other, Rock):
            return False
        return True

    @property
    def points(self):
        return 3

    @property
    def lose(self):
        return Paper()

    @property
    def draw(self):
        return Scissors()

    @property
    def win(self):
        return Rock()


class Code(object):
    def __init__(self, code: str, opponent_code: str):
        self.code = code
        self.opponent_code = opponent_code

    def code_map(self, code: str):
        if code == 'A':
            return Rock()
        elif code == 'B':
            return Paper()
        elif code == 'C':
            return Scissors()

    @property
    def obj(self):
        if self.code.upper() in ['A', 'B', 'C']:
            return self.code_map(self.code.upper())
        elif self.code.upper() == 'X':
            return self.code_map(self.opponent_code).lose
        elif self.code.upper() == 'Y':
            return self.code_map(self.opponent_code).draw
        elif self.code.upper() == 'Z':
            return self.code_map(self.opponent_code).win


def print_rounds(rounds: list):
    for r in range(0, len(rounds)):
        print(f'Round {r+1}:\n========')
        #print(f'winner: {rounds[r].winner.name} ({rounds[r].winner} beats {rounds[r].loser})')
        print(f'{rounds[r].player_1.name}: {rounds[r].player_1.score}')
        print(f'{rounds[r].player_2.name}: {rounds[r].player_2.score}')
        print()

def main():
    parser = argparse.ArgumentParser(
        prog = 'day2',
        description = 'Advent of Code 2022: Day 2 ')

    parser.add_argument('filename')
    #parser.add_argument('-n', '--number', default=1, type=int, help='help about -n')
    args = parser.parse_args()

    rounds = []
    with open(args.filename) as f:
        for line in f.readlines():
            p1, p2 = line.split()
            player_1 = Player("Elf", Code(p1, p2).obj)
            player_2 = Player("Chris", Code(p2, p1).obj)
            rounds.append(Round(player_1, player_2))

    for r in rounds:
        r.play(verbose=False)

    #print_rounds(rounds)
    print(f'{player_2.name} score: {sum([r.player_2.score for r in rounds])}')


if __name__ == "__main__":
    main()
