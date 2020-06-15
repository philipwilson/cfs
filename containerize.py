#!/usr/bin/env python3

# docker run image <cmd> <params>

# containerize.py run <image_dir> <cmd> <params>


import os, sys
import shutil
from libc_bindings import *
from cg_utils import cg
    
def run(image_dir, cmd, params):
    cg()

    if os.path.exists(image_dir) and os.path.isdir(image_dir):
        os.chroot(image_dir)
        os.chdir('/')
        
    else:
        print("could not find ", image_dir, file=sys.stderr)
        exit(-1)
        
    path = shutil.which(cmd)
    if path is None:
        print("could not find ", cmd, file=sys.stderr)
        exit(-1)

    unshare(CLONE_NEWUTS | CLONE_NEWPID) 

    pid = os.fork()
    if pid == 0:
        mount('proc', '/proc', 'proc')
        sethostname('桜の花')
        os.execv(path, params)
    else:
        status = os.wait()
        umount('/proc')

    
def main():
    if sys.argv[1] == 'run':
        run(sys.argv[2], sys.argv[3], sys.argv[3:])

    else:
        print("unimplemented command " + sys.argv[1], file=sys.stderr)
        sys.exit(0)

if __name__ == "__main__":
    main()
