"""CSCI E-71 Initial "hello world" assignment."""

import sys


def helloworld():
    if len(sys.argv) < 2:
        raise ValueError("Expected at least 1 argument")

    for i in range(1, len(sys.argv)):
        name = sys.argv[i]
        print(f"Hello, {name}!")


if __name__ == '__main__':
    helloworld()
