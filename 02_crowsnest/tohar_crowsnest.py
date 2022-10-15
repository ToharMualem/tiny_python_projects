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

    parser.add_argument('word', metavar='word', help='Word')
    return parser.parse_args()


def concat_ahoy_sentence(word):
    first_char = word[0].lower()
    article = 'an' if first_char in 'aeiou' else 'a'
    return 'Ahoy, Captain, {} {} off the larboard bow!'.format(article, word)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    word = args.word
    print(concat_ahoy_sentence(word))


# --------------------------------------------------
if __name__ == '__main__':
    main()
