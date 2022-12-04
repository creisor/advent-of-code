#!/usr/bin/env python3

import argparse
import string

def lowercase():
    return {k:v for (k,v) in zip([i for i in string.ascii_lowercase], [i for i in range(1, 27)])}

def uppercase():
    return {k:v for (k,v) in zip([i for i in string.ascii_uppercase], [i for i in range(27, 53)])}

def common_priorities(common):
    priorities = {**lowercase(), **uppercase()}
    return [priorities[i] for i in common]

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
    for r in range(0, len(rucksacks)):
        if r % 3 == 0:
            common = set(rucksacks[r]).intersection(set(rucksacks[r+1])).intersection(set(rucksacks[r+2]))#.pop()
            priorities.append(common_priorities(common)[0])
    print(sum(priorities))

if __name__ == "__main__":
    main()
