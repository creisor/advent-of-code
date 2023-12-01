#!/usr/bin/env python3

import argparse
import logging

def args_and_inputs():
    parser = argparse.ArgumentParser(
        prog = 'skeleton',
        description = 'Advent of Code 2023: Day N ')

    parser.add_argument('filename', help='The inputs file to process')
    parser.add_argument('-d', '--debug', action=argparse.BooleanOptionalAction, default=False, type=bool, help='enable debug output')
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
    else:
        logging.basicConfig(encoding='utf-8', level=logging.WARNING)

    inputs = []
    with open(args.filename) as f:
        for line in f.readlines():
            inputs.append(line.rstrip('\n'))

    return args, inputs

def first_last_num(string):
    logging.debug(f'string; {string}')
    numbers = [str(n) for n in [*range(0,10)]]

    first = [n for n in string if n in numbers][0]

    rev = [s for s in string]
    rev.reverse()
    last = [n for n in str(rev) if n in numbers][0]

    firstlast = int(f'{first}{last}')
    logging.debug(f'firstlast: {firstlast}')

    return firstlast

def main():
    args, inputs = args_and_inputs()

    calibrations = []
    for line in inputs:
        calibrations.append(first_last_num(line))

    print(sum(calibrations))

if __name__ == "__main__":
    main()
