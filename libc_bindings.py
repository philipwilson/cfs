import ctypes, ctypes.util


_libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

def setns():
    myfd = os.open('/proc/1/ns/mnt', os.O_RDONLY)
    _libc.setns(myfd, 0)



CLONE_NEWCGROUP = 0x02000000 #	/* New cgroup namespace */
CLONE_NEWUTS	= 0x04000000 #	/* New utsname namespace */
CLONE_NEWIPC    = 0x08000000 #	/* New ipc namespace */
CLONE_NEWUSER	= 0x10000000 #	/* New user namespace */
CLONE_NEWPID    = 0x20000000 #	/* New pid namespace */
CLONE_NEWNET	= 0x40000000 #	/* New network namespace */

    
def unshare(i):
    _libc.unshare(i)

    
def sethostname(newname):
    _libc.sethostname(newname, len(newname))

