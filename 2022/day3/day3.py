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

    @property
    def common(self):
        return set(self.compartments[0]).intersection(set(self.compartments[1]))

    def common_priorities(self):
        priorities = {**self.lowercase, **self.uppercase}
        return [priorities[i] for i in self.common]

def main():
    parser = argparse.ArgumentParser(
        prog = 'day3',
        description = 'Advent of Code 2022: Day N ')

    parser.add_argument('filename')
    args = parser.parse_args()

    rucksacks = []
    with open(args.filename) as f:
        for line in f.readlines():
            rucksacks.append(line.strip())

    priorities = []
    for r in rucksacks:
        rucksack = Rucksack(r)
        priorities.append(rucksack.common_priorities())
    print(sum([i[0] for i in priorities]))

if __name__ == "__main__":
    main()
