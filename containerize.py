#!/usr/bin/env python3

# docker run image <cmd> <params>

# containerize.py run <cmd> <params>


import os, sys, ctypes
import subprocess
import shutil


def setns():
    f = None
    libc = ctypes.CDLL('libc.so.6')
    myfd = os.open('/proc/1/ns/mnt', os.O_RDONLY)
    libc.setns(myfd, 0)



CLONE_NEWCGROUP = 0x02000000 #	/* New cgroup namespace */
CLONE_NEWUTS	= 0x04000000 #	/* New utsname namespace */
CLONE_NEWIPC    = 0x08000000 #	/* New ipc namespace */
CLONE_NEWUSER	= 0x10000000 #	/* New user namespace */
CLONE_NEWPID    = 0x20000000 #	/* New pid namespace */
CLONE_NEWNET	= 0x40000000 #	/* New network namespace */

    
def unshare(i):
    libc = ctypes.CDLL('libc.so.6')
    libc.unshare(i)

    
def sethostname(newname):
    libc = ctypes.CDLL('libc.so.6')
    libc.sethostname(newname, len(newname))

    
def run():
    path = shutil.which(sys.argv[2])
    if path is None:
        print("could not find ", argv[2], file=sys.stderr)
        exit(0)

    pid = os.fork()
    if pid == 0:
        unshare(CLONE_NEWUTS)
#        unshare(CLONE_NEWPID)
        sethostname(b'container')
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
