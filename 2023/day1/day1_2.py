#!/usr/bin/env python3

"""
first answer was 55309, which they said was too high...
"""

import argparse
import logging
import re

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
    regex = re.compile(r'(one)|1|(two)|2|(three)|3|(four)|4|(five)|5|(six)|6|(seven)|7|(eight)|8|(nine)|9')
    num_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    matches = regex.finditer(string)
    matchlist = [m.group() for m in matches]

    try:
        first = num_map[matchlist[0]]
    except KeyError:
        first = matchlist[0]

    try:
        last = num_map[matchlist[-1]]
    except KeyError:
        last = matchlist[-1]

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
