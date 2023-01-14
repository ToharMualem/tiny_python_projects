#!/usr/bin/env python
"""
Author : Tohar Muaelm <toharm7@gmail.com>
Date   : 2023-01-14
Purpose: Bottles of beer
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='int',
                        type=int,
                        default=10)
    args = parser.parse_args()

    if args.num <= 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


def verse(bottle):
    """sing a verse"""
    bottle_str = 'bottles' if bottle > 1 else 'bottle'
    _verse = f'{bottle} {bottle_str} of beer on the wall,\n' \
             f'{bottle} {bottle_str} of beer,\n' \
             f'Take one down, pass it around,\n'
    bottle -= 1
    bottle_str = 'bottles' if bottle > 1 else 'bottle'
    _verse += f'{bottle} {bottle_str} of beer on the wall!\n' if bottle > 0\
        else f'No more bottles of beer on the wall!'
    return _verse


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for num in list(reversed(range(1, args.num + 1))):
        print(verse(num))


# --------------------------------------------------
if __name__ == '__main__':
    main()
