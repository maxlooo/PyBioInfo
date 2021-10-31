#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-10-31
Purpose: Print the reverse complement of DNA
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
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna',
                        metavar='DNA',
                        help='A DNA input sequence or File')

    args = parser.parse_args()

    return Args(dna=args.dna)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    dna_arg = args.dna
    working_dir = os.path.dirname(__file__)
    # print(f'working_dir = "{working_dir}"')
    abs_file_path = os.path.join(working_dir, dna_arg)
    # print(f'abs_file_path = "{abs_file_path}"')
    rev_dna = ""

    if os.path.isfile(abs_file_path):
        fh = open(abs_file_path)
        for dna in fh:
            rev_dna = reversed(dna.rstrip())
        fh.close()
        print(f'rev_dna = "{rev_dna}"')
    else:
        rev_dna = reversed(dna_arg)
        print(f'rev_dna = "{rev_dna}"')

def reversed(dna):
    new_dna = ""
    for base in dna:
        if base == 'A':
            new_dna = 'T' + new_dna
        elif base == 'a':
            new_dna = 't' + new_dna
        elif base == 'C':
            new_dna = 'G' + new_dna
        elif base == 'c':
            new_dna = 'g' + new_dna
        elif base == 'G':
            new_dna = 'C' + new_dna
        elif base == 'g':
            new_dna = 'c' + new_dna
        elif base == 'T':
            new_dna = 'A' + new_dna
        elif base == 't':
            new_dna = 'a' + new_dna
    return new_dna


# --------------------------------------------------
if __name__ == '__main__':
    main()
