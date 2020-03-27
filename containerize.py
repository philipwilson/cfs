#!/usr/bin/env python3

# docker run image <cmd> <params>

# containerize.py run <cmd> <params>


import os, sys
import shutil
from libc_bindings import *
from cg_utils import cg
    
def run():
    path = shutil.which(sys.argv[2])
    if path is None:
        print("could not find ", argv[2], file=sys.stderr)
        exit(0)

    pid = os.fork()
    if pid == 0:
        cg()
        unshare(CLONE_NEWUTS)
#        unshare(CLONE_NEWPID)
        sethostname(b'container')
        os.chroot('/home/vagrant/ubuntu-fs')
        os.chdir('/')
        unshare(CLONE_NEWNS)
        mount('proc', '/proc', 'proc')
        os.execv(path, sys.argv[2:])
    else:
        status = os.wait()

    
def main():
    if sys.argv[1] == 'run':
        run()

    else:
        print("unimplemented command " + sys.argv[1], file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()
