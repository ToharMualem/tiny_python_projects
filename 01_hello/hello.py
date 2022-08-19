#! /usr/bin/env python
"""
Tohar Mualem
Purpose: Say hello
"""

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    print("Hello, " + args.name + "!")


if __name__ == '__main__':
    main()
