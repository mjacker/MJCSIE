## This is a script example to use argparse
# From terminal run:
# `python mjargparse.py -n 10 20`

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--numbers", type=float, nargs=2, help="The number to be added.")

args = parser.parse_args()

print(args)
print(args.numbers)

if args.numbers is not None:
    print(args.numbers[0] + args.numbers[1])

