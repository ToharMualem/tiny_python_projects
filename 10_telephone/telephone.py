#!/usr/bin/env python
"""
Author : Tohar Mualem <toharm7@gmail.com>
Date   : 2023-01-07
Purpose: Telephone
"""

import argparse
import os
import string
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='An input text or a file path',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-m',
                        '--mutations',
                        help='Precentage of the number of the letters that should be altered. (0 - 1)',
                        metavar='float',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)
    args = parser.parse_args()

    if args.mutations > 1 or args.mutations < 0:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    # calculating the number of mutations
    mutations = round(len(text) * args.mutations)

    # getting letters collection
    letters_collection = ''.join(sorted(string.ascii_letters + string.punctuation))

    # random choosing indices
    random.seed(args.seed)
    indices = random.sample(range(len(text)), k=mutations)
    # constructing new_text
    new_text = text
    for index in indices:
        new_char = random.choice(letters_collection.replace(new_text[index], ''))
        new_text = new_text[:index] + new_char + new_text[index + 1:]

    print(f'You said: "{text}"\nI heard : "{new_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
