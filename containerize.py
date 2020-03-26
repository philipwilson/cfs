#!/usr/bin/env python3

# docker run image <cmd> <params>

# containerize.py run <cmd> <params>


import os, sys


def lex(text):
    return text.rstrip().split()

def resolve_path(progname):
    for directory in os.environ["PATH"].split(':'):
        testpath = '/'.join([directory, progname])
        if os.path.isfile(testpath):
            return testpath

    return None


def run():
    path = resolve_path(sys.argv[2])
    if path:
        pid = os.fork()
        if pid == 0:
            os.execv(path, sys.argv[2:])
        else:
            status = os.wait()
    else:
        sys.stdout.write("command not found\n")

    
#    print("running ", sys.argv[2:])






    
def main():
    if sys.argv[1] == 'run':
        run()
    else:
        print("unimplemented command " + sys.argv[1], file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()
