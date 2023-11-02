#!/usr/bin/env python3

import argparse
import re

VERBOSE = True

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

    @property
    def id(self):
        if not self.parent:
            id = 'root'
        else:
            id = f'{self.name}-{self.parent.id}'

        return id

    @property
    def files(self):
        return [f for f in children if isinstance(f, File)]

    @property
    def directories(self, recursive=False):
        dirs = [d for d in children if isinstance(f, Directory)]
        if not recursive:
            return dirs
        #for directory in dirs:

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

    #re_cd = re.compile(r'^\$ cd (?P<dirname>.+)')
    #re_dir = re.compile(r'^dir (?P<dirname>.+)')
    #re_file = re.compile(r'^(?P<size>\d+) (?P<filename>.+)')

    root = Directory('/')

    all_dirs = [root]

    cur_dir = None
    prev_dir = all_dirs[[i.id for i in all_dirs].index('root')]

    for line in inputs:
        if line.startswith('$'):
            cmd = Command(line)

            if cmd.cmd == 'cd':
                if VERBOSE:
                    print(f'cmd: {cmd.cmd}, args: {cmd.args}')
                dirname = cmd.args[0]

                if dirname != '..':
                    try:
                        directory = all_dirs[[i.id for i in all_dirs].index(dirname)]
                    except ValueError:
                        print(f'creating new directory: {dirname}')
                        directory = Directory(dirname, prev_dir)
                        all_dirs.append(directory)

                new_prev_dir = cur_dir
                if dirname == '..':
                    print(f'setting cur_dir to {prev_dir.id}')
                    cur_dir = prev_dir
                else:
                    #if dirname == 'a':
                    #    import pdb; pdb.set_trace()
                    print(f'setting cur_dir to {directory.id}')
                    cur_dir = directory

                if new_prev_dir:
                    print(f'setting prev_dir to {new_prev_dir.id}')
                else:
                    print(f'setting prev_dir to None')
                prev_dir = new_prev_dir

                if VERBOSE:
                    print(f'cur_dir: {cur_dir.id}')
                    if prev_dir:
                        print(f'prev_dir: {prev_dir.id}')

        elif line.startswith('dir'):
            dirname = line.split()[-1]



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
