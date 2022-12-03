#!/usr/bin/env python3

import argparse

class Rucksack(object):
    def __init__(self, contents: str):
        self.contents = contents

    def compartments(self):
        return [[i for i in self.contents[:len(self.contents)//2]],
                [i for i in self.contents[len(self.contents)//2:]]]

def main():
    parser = argparse.ArgumentParser(
        prog = 'day3',
        description = 'Advent of Code 2022: Day N ')

    parser.add_argument('filename')
    #parser.add_argument('-n', '--number', default=1, type=int, help='some help message about -n')
    args = parser.parse_args()

    rucksacks = []
    with open(args.filename) as f:
        for line in f.readlines():
            rucksacks.append(line.strip())

    print(rucksacks)
    r = Rucksack(rucksacks[0])
    #print(f'compartment 1: {r.compartment(1)}')
    #print(f'compartment 2: {r.compartment(2)}')
    print(r.compartments())

if __name__ == "__main__":
    main()
