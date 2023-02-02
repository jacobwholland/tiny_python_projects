#!/usr/bin/env python3
"""
Author : jacobholland <jacobholland@localhost>
Date   : 2023-01-31
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-n',
                        '--name',
                        help='name to greet',
                        metavar='name',
                        type=str,
                        default='Everyone')



    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    person = args.name
    print(f'Hello, {person}!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
