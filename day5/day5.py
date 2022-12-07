#!/usr/bin/env python3

import argparse
import re

class Instruction(object):
    def __init__(self, line):
        self.line = line
        self.r = re.compile(r'\d+')

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
            if i:
                print(f'[{i}]')
            else:
                print()
        print(self.id)

    @property
    def items(self):
        return self.__items

    @property
    def top(self):
        return self.items[0]

    def remove(self, num):
        items = []
        for i in range(0, num):
            items.append(self.__items.pop(0))
        #print(f'items to remove: {items}')
        return items

    def add(self, items: list):
        crates = [i for i in self.__items if i]
        print(f'{len(crates)} crates in {self.id} before')
        for i in items:
            crates.insert(0, i)
        self.__items = crates
        print(f'{len(self.__items)} crates {self.id} after')

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
    print('move 4 crates from stack 1 to 2')
    stack1 = Stack(1, ['', '', 'N', 'C', 'B', 'D', 'P'])
    stack2 = Stack(2, ['T', 'F', 'P', 'L', 'M', 'N', 'W', 'V', 'P', 'H', 'T', 'M'])

    print(f'stack1 before: {stack1.items}')
    print(f'stack2 before: {stack2.items}')

    to_move = stack1.remove(4)
    stack2.add(to_move)

    print(f'stack1 after: {stack1.items}')
    print(f'stack2 after: {stack2.items}')

    #args, inputs = args_and_inputs()
    #
    ## regex for a crate
    #r = re.compile(r'(\[\w\])')

    ## get the number of colums
    #cols = int(len(re.findall(r'([\w\W])', inputs[0])) / 3)

    #rows = []
    #columns = []
    #for line in inputs:
    #    if re.match(r'(^ \d)|(^\n)', line):
    #        break
    #    matches = [i for i in r.finditer(line)]
    #    crates = {int(m.span()[0]/4):m.group() for m in matches}
    #    print(crates)

    #    for i in range(0, cols):
    #        if crates.get(i):
    #            columns.append(crates.get(i))
    #        else:
    #            columns.append('')
    #    rows.append(columns)
    #    columns = []

    #stacks = []
    #for i in range(0, cols):
    #    stacks.append(Stack(i+1, [row[i] for row in rows]))

    ## regex for an instruction:
    #r = re.compile(r'^move')
    #instructions = []
    #for line in inputs:
    #    m = r.search(line)
    #    if m:
    #        instructions.append(Instruction(line))

    #print([i.items for i in stacks])
    #count = 1
    #for i in instructions:
    #    #print([i.items for i in stacks])
    #    for stack in stacks:
    #        print(f'{stack}: {stack.items}')
    #        #stack.print()
    #    print()
    #    print(f'{count}: move {i.num_crates} crates from stack {i.from_stack} to {i.to_stack}')
    #    count += 1
    #    to_move = stacks[i.from_stack-1].remove(i.num_crates)
    #    stacks[i.to_stack-1].add(to_move)

    #print(f'\n\nanswer: {"".join([s.top for s in stacks])}')

if __name__ == "__main__":
    main()
