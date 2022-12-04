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

def bundle_sizes(bundles: list):
    return [sum(i) for i in bundles]

def top_bundles(num: int, bundles: list):
    biggest = []
    sizes = bundle_sizes(bundles)
    for i in range(0, num):
        biggest.append(sizes.pop(sizes.index(max(sizes))))

    return biggest

def main():
    parser = argparse.ArgumentParser(
        prog = 'code',
        description = 'Advent of Code 2022: Day 1 ')

    parser.add_argument('input', help='Input file with values described in the problem')
    parser.add_argument('-n', '--number', default=1, type=int, help='Show the top N bundles')
    args = parser.parse_args()

    inpt = None
    with open(args.input) as f:
        inpt = f.read().strip()

    bundles = list(parse_input(inpt.split('\n')))

    top = top_bundles(args.number, bundles)

    print(f'Top {args.number} bundles:')
    for b in top:
        print(b)
    print(f'Total: {sum(top)}')
    
if __name__ == "__main__":
    main()
