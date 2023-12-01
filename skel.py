#!/usr/bin/env python3

import argparse

def args_and_inputs():
    parser = argparse.ArgumentParser(
        prog = 'skeleton',
        description = 'Advent of Code 2023: Day N ')

    parser.add_argument('filename', help='The inputs file to process')
    parser.add_argument('-n', '--number', default=1, type=int, help='some help message about -n')
    args = parser.parse_args()

    inputs = []
    with open(args.filename) as f:
        for line in f.readlines():
            inputs.append(line.rstrip('\n'))

    return args, inputs

def main():
    args, inputs = args_and_inputs()

if __name__ == "__main__":
    main()
