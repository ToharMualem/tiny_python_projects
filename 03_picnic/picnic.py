#!/usr/bin/env python
"""
Author : Tohar Mualem
Date   : 2022-10-21
Purpose: Bringing items to picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring for the picnic')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    items = args.items

    # sort items according to sorted boolean
    if args.sorted:
        items.sort()

    bringing = ""
    length = len(items)
    if length == 1:
        bringing = items[0]
    elif length == 2:
        bringing = " and ".join(items)
    elif length > 2:
        bringing = ", ".join(items[:length-1]) + ", and " + items[-1]

    print("You are bringing {}.".format(bringing))


# --------------------------------------------------
if __name__ == '__main__':
    main()
