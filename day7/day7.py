#!/usr/bin/env python3

import argparse
import re

VERBOSE = False

class File(object):
    def __init__(self, listing: str):
        self.listing = listing

    @property
    def name(self):
        return self.listing.split()[1]

    @property
    def size(self):
        return int(self.listing.split()[0])

class Directory(object):
    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def pwd(self):
        return self.name

    @property
    def files(self):
        return [f for f in children if isinstance(f, File)]

    @property
    def directories(self):
        return self.__directories

    @property
    def size(self):
        filesizes = []
        for f in self.files:
            filesizes.append(f.size)
        for d in self.directories:
            for f in d.files:
                filesizes.append(f.size)
        return sum(filesizes)

class Command(object):
    def __init__(self, cmd: str):
        self.__cmd = cmd.strip('$ ')

    @property
    def cmd(self):
        return self.__cmd.split()[0]

    @property
    def args(self):
        return self.__cmd.split()[1:]


def args_and_inputs():
    parser = argparse.ArgumentParser(
        prog = 'skeleton',
        description = 'Advent of Code 2022: Day N ')

    parser.add_argument('filename', help='The inputs file to process')
    parser.add_argument('-n', '--number', default=100000, type=int, help='Size to search for')
    args = parser.parse_args()

    inputs = []
    with open(args.filename) as f:
        for line in f.readlines():
            inputs.append(line.rstrip('\n'))

    return args, inputs

def main():
    args, inputs = args_and_inputs()

    filesystem = {}

    re_cd = re.compile(r'^\$ cd (?P<dirname>.+)')
    re_dir = re.compile(r'^dir (?P<dirname>.+)')
    re_file = re.compile(r'^(?P<size>\d+) (?P<filename>.+)')

    cur_dir = None
    prev_dir = None
    for line in inputs:
        #print(line)
        # is it a directory?
        m = re_cd.search(line)
        if m:
            new_prev_dir = cur_dir
            if m['dirname'] == '..':
                cur_dir = prev_dir
                prev_dir = new_prev_dir
            else:
                prev_dir = cur_dir
                cur_dir = m['dirname']
            if cur_dir not in filesystem:
                filesystem[cur_dir] = []
            print(f'cur_dir: {cur_dir}')
            print(f'prev_dir: {prev_dir}')

        #m = re_dir.search(line)
        #if m:


"""
- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
"""


    ##re_file = re.compile(r'^(?P<size>\d+) (?P<filename>.+)')
    ##re_file = re.compile(r'^\d+')

    #directories = {} 

    #cwd = None
    #for line in inputs:
    #    if line.startswith('$'):
    #        cmd = Command(line)

    #        if cmd.cmd == 'cd':
    #            if VERBOSE:
    #                print(f'cmd: {cmd.cmd}, args: {cmd.args}')
    #            dirname = cmd.args[0]

    #            if dirname == '..':
    #                if cwd.parent:
    #                    cwd = directories[cwd.parent.name]
    #                else:
    #                    cwd = directories['/']
    #                continue

    #            elif dirname not in directories:
    #                directories[dirname] = (Directory(dirname, cwd))
    #            cwd = directories[dirname]

    #    elif line.startswith('dir'):
    #        dirname = line.split()[-1]
    #        if dirname not in directories:
    #            directories[dirname] = Directory(dirname, cwd)
    #            directories[cwd.name].directories.append(directories[dirname])
    #        else:
    #            directories[cwd.name].directories.append(directories[dirname])

    #    else:
    #        cwd.files.append(File(line))


    #if VERBOSE:
    #    for d in directories.values():
    #        print(f'{d.name} directories: {[s.name for s in d.directories]}')
    #        print(f'{d.name} files: {[f.name for f in d.files]}')
    #        print(f'{d.name} size: {d.size}')

    #candidates = [d for d in directories.values() if d.size <= args.number and d.name != '/']

    #print(f'{[d.size for d in candidates]}')
    #print(f'{sum([d.size for d in candidates])}')
    ## 1403066 is too low, apparently

if __name__ == "__main__":
    main()
