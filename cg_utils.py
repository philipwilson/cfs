import os


def cg():
    cgroups = '/sys/fs/cgroup'
    pids = os.path.join(cgroups, 'pids')
    pids = os.path.join(pids, 'phil')

    try:
        os.mkdir(pids)
    except Exception as e:
        pass

    with open(os.path.join(pids, 'pids.max'), 'w+') as f:
        f.write('10')
    with open(os.path.join(pids, 'notify_on_release'), 'w+') as f:
        f.write('1')
    with open(os.path.join(pids, 'cgroup.procs'), 'w+') as f:
        f.write(str(os.getpid()))

    
    
