#!/usr/bin/env python3
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v', 
        '--verbose', 
        help='include tips and directions on files',
        action='store_true',
    )
    args = parser.parse_args()

    if args.verbose:
        print('verbose structure')
    else:
        print('just give me some structure.')

if __name__ == "__main__":
    main()