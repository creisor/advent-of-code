#!/usr/bin/env python3

import argparse

def contains_overlap(assignment_pair):
    p1, p2 = assignment_pair.split(',')

    a1 = set([i for i in range(int(p1.split('-')[0]), int(p1.split('-')[1])+1)])
    a2 = set([i for i in range(int(p2.split('-')[0]), int(p2.split('-')[1])+1)])

    return len(a1 & a2) > 0

def main():
    parser = argparse.ArgumentParser(
        prog = 'day4',
        description = 'Advent of Code 2022: Day 4')

    parser.add_argument('filename', help='The inputs file to process')
    args = parser.parse_args()

    inputs = []
    with open(args.filename) as f:
        for line in f.readlines():
            inputs.append(line.strip())

    overlaps = 0
    for pair in inputs:
        if contains_overlap(pair):
            #print(f'found overlap in {pair}')
            overlaps += 1

    print(f'\n{overlaps} assignment pairs contain overlap')


if __name__ == "__main__":
    main()
