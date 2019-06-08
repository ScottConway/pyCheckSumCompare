#!/usr/bin/env python3

import sys
import argparse


def readFile(filename):
    file = open(filename, "r")
    checksums = {}
    for line in file:
        line_split = line.split()
        if len(line_split) > 1:
            checksums[line_split[0]] = line_split[1]
    return checksums


def compareCheckSums(sourceFileName, checkFileName):
    sourceDictionary = readFile(sourceFileName)
    checkDictionary = readFile(checkFileName)

    for k, v in checkDictionary.items():
        checksum = sourceDictionary.get(k)
        if checksum is None:
            print(f'Did not find {k} in source file')
        elif v != checksum:
            print(f'Checksums do not match for {k}')


def main():
    parser = argparse.ArgumentParser(
        description='check the contents of two files containing lists of checksums for differences')
    parser.add_argument('-s', action='store', dest='sourceFileName',
                        help='Contains the largest(Superset) list of files with checksums.')
    parser.add_argument('-c', action='store', dest='subSetFileName',
                        help='File you wish to check values against source file.')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.1')

    args = parser.parse_args(sys.argv[1:])
    print(f'source = {args.sourceFileName}')
    print(f'check = {args.subSetFileName}')

    compareCheckSums(sourceFileName=args.sourceFileName, checkFileName=args.subSetFileName)


if __name__ == '__main__':
    main()
