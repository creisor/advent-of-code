#!/usr/bin/env python3

import argparse
import string

class Rucksack(object):
    def __init__(self, contents: str):
        self.contents = contents

    @property
    def compartments(self):
        return [[i for i in self.contents[:len(self.contents)//2]],
                [i for i in self.contents[len(self.contents)//2:]]]

    @property
    def lowercase(self):
        return {k:v for (k,v) in zip([i for i in string.ascii_lowercase], [i for i in range(1, 27)])}

    @property
    def uppercase(self):
        return {k:v for (k,v) in zip([i for i in string.ascii_uppercase], [i for i in range(27, 53)])}

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
    print(r.compartments)
    print(r.lowercase)
    print(r.uppercase)

if __name__ == "__main__":
    main()
