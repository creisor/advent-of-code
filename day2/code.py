#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(
        prog = 'skeleton',
        description = 'Advent of Code 2022: Day N ')

    parser.add_argument('skeleton')
    args = parser.parse_args()

if __name__ == "__main__":
    main()
