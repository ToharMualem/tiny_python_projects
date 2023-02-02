#!/usr/bin/env python
"""
Author : Tohar Mualem <toharm7@gmail.com>
Date   : 2023-01-31
Purpose: Create a ransom note
"""

import argparse
import os.path
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create a ransom note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def choose(char):
    return char.lower() if random.choice([True, False]) else char.upper()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    ransom_str = ''.join([choose(char) for char in args.text])
    print(ransom_str)


# --------------------------------------------------
if __name__ == '__main__':
    main()
