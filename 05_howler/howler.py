#!/usr/bin/env python
"""
Author : Tohar Mualem <toharm7@gmail.com>
Date   : 2023-01-04
Purpose: Howler
"""

import argparse
import io
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

    # opening a file handler of args.text in case file exists, else we open a StringIO file handler.
    if os.path.isfile(args.text):
        args.text = open(args.text)
    else:
        args.text = io.StringIO(args.text + '\n')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    # getting args
    args = get_args()
    text = args.text
    out_path = args.outfile

    out_file_handler = open(out_path, "wt") if out_path else sys.stdout
    for line in text:
        out_file_handler.write(line.upper())
    out_file_handler.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
