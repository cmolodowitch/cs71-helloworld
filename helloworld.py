"""CSCI E-71 Initial "hello world" assignment."""

import sys


def helloworld():
    name = sys.argv[1]
    print(f"Hello, {name}!")


if __name__ == '__main__':
    helloworld()
