import os

# Note that there is a python package called cgroup-utils that appears well-designed and complete.
# This package is just a quick demo


class ControlGroup():
    
    def __init__(self, name):
        self.name = name
        self.cgroups = '/sys/fs/cgroup'

    def set_pids(self, maxpids):

        pidspath = os.path.join(self.cgroups, 'pids')
        pidspath = os.path.join(pidspath, self.name)

        try:
            os.mkdir(pidspath)
        except Exception as e:
            pass

        with open(os.path.join(pidspath, 'pids.max'), 'w+') as f:
            f.write(str(maxpids))
        with open(os.path.join(pidspath, 'notify_on_release'), 'w+') as f:
            f.write('1')
        with open(os.path.join(pidspath, 'cgroup.procs'), 'w+') as f:
            f.write(str(os.getpid()))

    
    
