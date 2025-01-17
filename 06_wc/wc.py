#!/usr/bin/env python
"""
Author : Tohar Mualem <toharm7@gmail.com>
Date   : 2023-01-05
Purpose: Emulates wc (word count)
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Word Count',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('r'),
                        default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_lines, total_words, total_bytes = 0, 0, 0
    for file_handler in args.file:
        num_lines, num_words, num_bytes = 0, 0, 0
        for line in file_handler:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)
        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes
        # print the counting of one file
        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {file_handler.name}')

    if len(args.file) > 1:
        # print total counting
        print(f'{total_lines:8}{total_words:8}{total_bytes:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
