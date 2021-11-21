#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-11-07
Purpose: Calculate Fibonacci
gen0 = 0
gen1 = 1
gen2 = 1 + gen0 + gen1//2 = 1
gen3 = 1 + gen1 + gen2//2 = 2
gen4 = 1 + gen0 + gen2 + gen3//2 = 3
gen5 = 1 + gen1 + gen3 + gen4//2 = 5
gen6 = 1 + gen2 + gen4 + gen5//2 = doesn't work
gen0 = 0
gen1 = 1 + gen0 + gen0//2 = 1
gen2 = 0 + gen1 + gen1//2 = 1
gen3 = 1 + gen2 + gen2//2 = 2
gen4 = 0 + gen3 + gen3//2 = 3
gen5 = 1 + gen4 + gen4//2 = 5
gen6 = 0 + gen5 + gen5//2 = doesn't work
gen0 = 0
gen1 = 1
gen2 = 1
gen3 = gen2 + gen2//2 + remainder = 2
gen4 = gen3 + gen3//2 + rem = 3
gen5 = gen4 + gen4//2 + rem = 5
gen6 = gen5 + gen5//2 + rem = 8
gen7 = gen6 + gen6//2 + rem = doesn't work
"""

import argparse
from typing import NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    generations: int
    litter: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Calculate Fibonacci',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('gen',
                        help='integer generation number',
                        metavar='generations',
                        type=int,
                        default=1)

    parser.add_argument('lit',
                        help='integer litter size for each generation',
                        metavar='litter',
                        type=int,
                        default=1)

    args = parser.parse_args()

    if not (1 <= args.gen <= 40):
        parser.error(f'generations "{args.gen}" must be between 1 and 40')

    if not (1 <= args.lit <= 5):
        parser.error(f'litter "{args.lit}" must be between 1 and 5')

    return Args(generations=args.gen, litter=args.lit)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    gen = args.generations
    lit = args.litter
    end = gen
    start0 = 0
    start1 = 1
    while (end > 1):
        sum = start0 * lit + start1
        start0 = start1
        start1 = sum
        end -= 1
    print(start1)

    def fib(n: int) -> None:
        nums = [0, 1]
        for _ in range(n - 1):
            nums.append((nums[-2] * lit) + nums[-1])
        print(nums[-1])
    # fib(gen)


# --------------------------------------------------
if __name__ == '__main__':
    main()
