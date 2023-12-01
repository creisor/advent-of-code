#!/usr/bin/env python3

import argparse

def parse_input(inpt):
    bundle = []
    for i in inpt:
        if i == '':
            yield bundle
            bundle = []
        else:
            bundle.append(int(i))
    yield bundle

def main():
    parser = argparse.ArgumentParser(
        prog = 'code',
        description = 'Advent of Code 2022: Day 1 ')

    parser.add_argument('input', help='Input file with values described in the problem')
    args = parser.parse_args()

    inpt = None
    with open(args.input) as f:
        inpt = f.read().strip()

    bundles = list(parse_input(inpt.split('\n')))

    bundle_sizes = [sum(i) for i in bundles]

    print(f'biggest bundle is #{bundle_sizes.index(max(bundle_sizes)) + 1} at {max(bundle_sizes)} calories')

    
if __name__ == "__main__":
    main()
