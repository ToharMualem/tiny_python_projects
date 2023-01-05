#!/usr/bin/env python
"""
Author : Tohar Mualem <toharm7@gmail.com>
Date   : 2023-01-05
Purpose: Apples and bananas
"""

import argparse
import os.path


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='A text or a text file path')

    parser.add_argument('-v',
                        '--vowel',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    def new_char(char):
        return args.vowel if char in 'aeoiu' else args.vowel.upper() if char in 'AEOIU' else char

    print(''.join([new_char(c) for c in args.text]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
