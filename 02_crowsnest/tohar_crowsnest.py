#!/usr/bin/env python
"""
Author : ToharMualem <toharm7@gmail.com>
Date   : 2022-08-25
Purpose: Ahoy, Captain...
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Prints Ahoy message by a given word',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-w',
                        '--word',
                        help='A named string argument',
                        metavar='word',
                        type=str,
                        default='tohar')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    word = args.word
    print(word)


# --------------------------------------------------
if __name__ == '__main__':
    main()
