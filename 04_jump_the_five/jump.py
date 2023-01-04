#!/usr/bin/env python
"""
Author : Tohar Mualem <toharm7@gmail.com>
Date   : 2023-01-04
Purpose: Jump the five!
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump The Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    encoding_table = {'1': '9',
                      '2': '8',
                      '3': '7',
                      '4': '6',
                      '5': '0',
                      '6': '4',
                      '7': '3',
                      '8': '2',
                      '9': '1',
                      '0': '5'}
    args = get_args()
    input_text = args.text
    encoded_text = ''
    for c in input_text:
        encoded_text += encoding_table.get(c, c)

    print(encoded_text)



# --------------------------------------------------
if __name__ == '__main__':
    main()
