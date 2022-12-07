#!/usr/bin/env python3

import argparse

def args_and_inputs():
    parser = argparse.ArgumentParser(
        prog = 'day6',
        description = 'Advent of Code 2022: Day 6')

    parser.add_argument('filename', help='The inputs file to process')
    args = parser.parse_args()

    inputs = []
    with open(args.filename) as f:
        for line in f.readlines():
            inputs.append(line.rstrip('\n'))

    return args, inputs

def get_marker(stream: str):
    start = 0
    end = 4
    while end < len(stream):
        if len([i for i in stream[start:end] if stream[start:end].count(i) > 1]) == 0:
            return end
        start += 1
        end += 1

def main():
    args, inputs = args_and_inputs()

    for i in inputs:
        print(get_marker(i))

if __name__ == "__main__":
    main()
