#!/usr/bin/env python
"""
Author : Tohar Mualem <toharm7@gmail.com>
Date   : 2023-01-05
Purpose: Gashlycrumb
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='An input text file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='gashlycrumb.txt')

    parser.add_argument('letter',
                        metavar='str',
                        help='letter(s) to search for sentences.',
                        nargs="+")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # construct the letters:sentences table
    letters_dict = {line[0].upper(): line.rstrip() for line in args.file}

    # output to user the sentences starting with the given letters
    sentences = [letters_dict.get(c.upper(), f'I do not know "{c.upper()}".') for c in args.letter]
    for sentence in sentences:
        print(sentence)


# --------------------------------------------------
if __name__ == '__main__':
    main()
