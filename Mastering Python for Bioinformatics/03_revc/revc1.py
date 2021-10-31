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
    outdir: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--out_dir',
                        help='Output DIR name',
                        metavar='str',
                        type=str,
                        default='out')

    parser.add_argument('dna',
                        metavar='DNA',
                        help='A DNA input sequence or File')

    """parser.add_argument('-f',
                        '--file',
                        help='Input DNA file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        default=None)"""

    args = parser.parse_args()

    return Args(dna=args.dna, outdir=args.out_dir)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    dna_arg = args.dna
    outdir_arg = args.outdir
    rev_dna = ""

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    print(f'dna_arg = "{dna_arg}"')
    print(f'outdir_arg = "{outdir_arg}"')

    if os.path.isfile(dna_arg):
        fh = open(dna_arg)
        # dna = fh.read().rstrip()
        # print(f'fh = "{fh}"')
        out_file = os.path.join(outdir_arg, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')
        for dna in fh:
            rev_dna = reversed(dna.rstrip())
            out_fh.write(rev_dna)
        out_fh.close()
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
