#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-10-23
Purpose: Tetranucleotide frequency
"""

import argparse
import os
from typing import NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    dna: str

# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna',
                        metavar='DNA',
                        help='A DNA input sequence argument')

    args = parser.parse_args()

    # https://pythonexamples.org/python-check-if-path-is-file-or-directory/
    # https://www.pythontutorial.net/python-basics/python-read-text-file/
    if os.path.isfile(args.dna):
        with open(args.dna) as f:
            args.dna = f.read().rstrip()
            f.close()

    return Args(args.dna)

# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    # print(args.dna / 2)
    pos_arg = args.dna

    # excess code:
    # print(f'positional argument dna = "{pos_arg}"')

    # https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string
    countA = pos_arg.count('A')
    countC = pos_arg.count('C')
    countG = pos_arg.count('G')
    countT = pos_arg.count('T')
    print(countA, countC, countG, countT)

# --------------------------------------------------
if __name__ == '__main__':
    main()
