#!/usr/bin/env python3

# docker run image <cmd> <params>

# containerize.py run <cmd> <params>


import os, sys


def run():
    print("running ", sys.argv[2:])

def main():
    if sys.argv[1] == 'run':
        run()
    else:
        print("unimplemented command " + sys.argv[1], file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()
