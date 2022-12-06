#!/usr/bin/env python3

import argparse
import re

class Instruction(object):
    def __init__(self, line):
        self.line = line
        self.r = re.compile(r'\d')

    @property
    def num_crates(self):
        return int(self.r.findall(self.line)[0])

    @property
    def from_stack(self):
        return int(self.r.findall(self.line)[1])

    @property
    def to_stack(self):
        return int(self.r.findall(self.line)[2])

class Stack(object):
    def __init__(self, ident: int, items: list):
        self.id = ident
        self.__items = [re.sub(r'[\[\]]', '', i) for i in items]

    def __str__(self):
        return str(self.id)

    def print(self):
        for i in self.items:
            print(i)

    @property
    def items(self):
        return self.__items

    @property
    def top(self):
        return self.items[0]

    def move(self, num, to):
        for i in range(0, num-1):
            to.items.insert(0, self.__items.pop(0))

def args_and_inputs():
    parser = argparse.ArgumentParser(
        prog = 'skeleton',
        description = 'Advent of Code 2022: Day N ')

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
    
    # regex for a crate
    r = re.compile(r'(\[\w\])')

    # get the number of colums
    cols = int(len(re.findall(r'([\w\W])', inputs[0])) / 3)

    rows = []
    columns = []
    for line in inputs:
        if re.match(r'^ \d', line):
            break
        matches = [i for i in r.finditer(line)]
        crates = {int(m.span()[0]/4):m.group() for m in matches}
        #import pdb; pdb.set_trace()
        for i in range(0, cols):
            if crates.get(i):
                columns.append(crates.get(i))
            else:
                columns.append('')
        rows.append(columns)
        columns = []

    stacks = []
    for i in range(0, cols):
        stacks.append(Stack(i, [row[i] for row in rows]))

    # regex for an instruction:
    r = re.compile(r'^move')
    instructions = []
    for line in inputs:
        m = r.search(line)
        if m:
            instructions.append(Instruction(line))

    print([i.items for i in stacks])
    for i in instructions:
        print(f'move {i.num_crates} from stack {i.from_stack} to {i.to_stack}')
        for r in range(0, i.num_crates):
            # TODO: need to update the logic to say "put it in the first empty index"
            print(f'take crate {stacks[i.from_stack-1].items[0]} from stack {i.from_stack} and put it in index {r-1} on stack {i.to_stack}')
            stacks[i.to_stack-1].items[r-1] = stacks[i.from_stack-1].items.pop(0)
        print([i.items for i in stacks])

    print([s.top for s in stacks])

if __name__ == "__main__":
    main()
