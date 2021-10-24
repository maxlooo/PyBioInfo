#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-10-24
Purpose: Transcribe DNA to RNA
"""

import argparse
import os
from typing import NamedTuple, TextIO, List


class Args(NamedTuple):
    """ Command-line arguments """
    files: List[TextIO]
    outdir: str
    # int_arg: int
    # file: TextIO
    # on: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Transcribe DNA to RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='str, Now FILE string',
                        help='A positional argument: Input DNA file(s)',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--out_dir',
                        help='A named string argument, USE FOR: Output DIR name',
                        metavar='str',
                        type=str,
                        default='out')

    parser.add_argument('-i',
                        '--int',
                        help='NOT IN USE: A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-f',
                        '--file0',
                        help='NOT IN USE: A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-b',
                        '--on',
                        help='NOT IN USE: A boolean flag',
                        action='store_true')

    args = parser.parse_args()

    # args.out_dir is only used in this function
    # no need for files= and outdir=
    # just to be clear
    return Args(files=args.file, outdir=args.out_dir) # , args.int, args.file0, args.on)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    # args.out_dir becomes args.outdir here because get_args() takes NamedTuple
    str_arg = args.outdir
    # int_arg = args.int_arg
    # file_arg = args.file0
    # flag_arg = args.on
    pos_arg = args.files

    # print(f'str_arg args.outdir = "{str_arg}"')
    # print(f'int_arg = "{int_arg}"')
    # print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    # print(f'flag_arg = "{flag_arg}"')
    # print(f'positional args.file  = "{pos_arg}"')

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    num_files, num_seqs = 0, 0
    for fh in args.files:
        # changing to `num_files += 2` requires changing assert statements in rna_test.py
        num_files += 2
        # print(os.path.dirname(fh.name))
        # print(os.path.basename(fh.name))
        out_file = os.path.join(args.outdir, os.path.basename(fh.name))
        # print(fh.name, '->', out_file)
        out_fh = open(out_file, 'wt')
        out_fh2 = open(out_file[:-4]+'2'+out_file[-4:], 'wt')
        for dna in fh:
            num_seqs += 1
            # print(dna.rstrip())
            dna2 = dna.replace('T', 'U')
            # print(dna2.rstrip())
            print(dna2.rstrip(), file=out_fh)
            out_fh2.write(dna2)
        out_fh.close()
        out_fh2.close()

        # cannot do another `for dna in fh`
        """
        for dna in fh:
            dna2 = dna.replace('T', 'U')
            out_fh2.write(dna2)
        """

    print(f'Done, wrote {num_seqs} sequence{"" if num_seqs == 1 else "s"} '
          f'in {num_files} file{"" if num_files == 1 else "s"} '
          f'to directory "{args.outdir}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
