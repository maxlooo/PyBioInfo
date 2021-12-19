#!/usr/bin/env python3
""" Compute GC content """

import argparse
import sys
from typing import NamedTuple, TextIO, List, Tuple
from Bio import SeqIO


class Args(NamedTuple):
    """ Command-line arguments """
    file0: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='?',
                        default=sys.stdin,
                        help='Input sequence file')

    args = parser.parse_args()

    return Args(file0=args.file)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """
    args = get_args()
    # print(type(args))
    file0 = args.file0
    # print(type(file0))
    sequences = SeqIO.parse(file0, 'fasta')
    # print(type(sequences))
    results = []
    for record in sequences:
        gc_bases = 0
        for base in record.seq.upper():
            if base=='C' or base=='G':
                gc_bases += 1
        percentage_gc = (gc_bases / len(record.seq)) * 100
        results.append([percentage_gc, record.id])
    # print(results)
    max_gc_percentage = max(results)
    max_gc_percentage.reverse()
    print(f'{max_gc_percentage[0]} {max_gc_percentage[1]:0.6f}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
