#!/usr/bin/env python
"""
Author : Tohar Mualem <toharm7@gmail.com>
Date   : 2023-01-04
Purpose: Howler
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file name',
                        metavar='str',
                        type=str,
                        default=None)

    parser.add_argument('text',
                        metavar='str',
                        help='A text argument')
    args = parser.parse_args()

    # reading text from file in case file exists, else the text stays the same as given.
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    # getting args
    args = get_args()
    text = args.text
    out_path = args.outfile

    # upper content.
    text = text.upper()
    # printing to file or to console.
    out_handler = sys.stdout
    if out_path is not None:
        out_handler = open(out_path, "wt")
    out_handler.write(text + '\n')
    out_handler.close()




# --------------------------------------------------
if __name__ == '__main__':
    main()
