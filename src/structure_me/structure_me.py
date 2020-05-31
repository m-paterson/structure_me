#!/usr/bin/env python3
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v', 
        '--verbose', 
        help='include tips and directions on files. If no argument is passed, the'
             ' program will create a similar structure but the files will not '
             'contain any text.',
        action='store_true',
    )

    args = parser.parse_args()

    if args.verbose:
        print('verbose structure')
    else:
        print('just give me some structure.')

if __name__ == "__main__":
    main()