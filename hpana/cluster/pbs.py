
## stdlib
import subprocess
from subprocess import call
import getpass
import time, datetime

def print_table(table, sep='  '):
    # Reorganize data by columns
    cols = zip(*table)
    # Compute column widths by taking maximum length of values per column
    col_widths = [max(len(str(value)) for value in col) for col in cols]
    # Create a suitable format string
    format = sep.join(['%%-%ds' % width for width in col_widths])
    # Print each row using the computed format
    for row in table:
        print format % tuple(row)


"""
Simple Job class for handeling jobs summited to cluster.
"""    
class Job(object):

    def __init__(self, id, info):
        self.id = id
        self.info = info

    def __getattr__(self, attr):
        return self.info[attr]

    @property
    def name(self):
        return self.info['Job_Name']

    @property
    def hung(self):
        # is the wall time higher than the CPU time by 50%?
        return self.walltime > 1.5 * self.cputime and self.walltime > 60

    @property
    def healthy(self):
        return not self.hung

    @property
    def health_status(self):
        # is the wall time higher than the CPU time?
        if self.healthy:
            return 'GOOD'
        return 'HUNG'

    @property
    def cputime(self):
        if 'resources_used.cput' not in self.info:
            return 0
        x = map(int, self.info['resources_used.cput'].split(':'))
        return datetime.timedelta(hours=x[0],minutes=x[1],seconds=x[2]).total_seconds()

    @property
    def walltime(self):
        if 'resources_used.walltime' not in self.info:
            return 0
        x = map(int, self.info['resources_used.walltime'].split(':'))
        return datetime.timedelta(hours=x[0],minutes=x[1],seconds=x[2]).total_seconds()

    @property
    def host(self):
        if 'exec_host' in self.info:
            return self.info['exec_host']
        return '-'

    @property
    def status(self):
        return (self.id,
                self.info['job_state'],
                self.host,
                self.info['Job_Name'],
                self.cputime,
                self.walltime,
                self.health_status)

"""
A class to monitor the sumited jobs.
"""
class PBSMonitor(object):

    def __init__(self):
        self.user = getpass.getuser()
        self.jobs = {}
        self.job_names = {}
        self.update()

    def update(self):
        qstat = subprocess.Popen(
            ['qstat', '-f', '-1'],
            stdout=subprocess.PIPE).communicate()[0]
        jobs = qstat.split('\n\n')
        self.jobs = {}
        for block in jobs:
            if not block:
                continue
            block = block.split('\n')
            user = block[2].split(' = ')[-1].split('@')[0]
            if self.user != user:
                continue
            info = {}
            jobid = block[0].split(': ')[-1]
            for line in block[1:]:
                param, value = line.split(' = ')
                info[param.strip()] = value.strip()
            job = Job(jobid, info)
            self.job_names[job.name] = jobid
            self.jobs[jobid] = job

    def has_jobname(self, name):
        return name in self.job_names

    def print_jobs(self):
        rows = []
        for id, job in sorted(self.jobs.items(),
                key=lambda item: int(item[0].split('.')[0])):
            rows.append(job.status)
        print_table(rows)


## job monitoring 
#MONITOR = PBSMonitor()

def qsub(cmd,
         queue='medium',
         ncpus=1,
         stderr_path=None,
         stdout_path=None,
         name=None,
         dry_run=False):
    MONITOR.update()
    kwargs = {}
    if name is not None:
        if MONITOR.has_jobname(name):
            print "a job with the name %s already exists" % name
            return
        kwargs['-N'] = name
    if stderr_path is not None:
        kwargs['-e'] = stderr_path
    if stdout_path is not None:
        kwargs['-o'] = stdout_path
    args = ' '.join(['%s "%s"' % arg for arg in kwargs.items()])
    cmd = "echo '%s' | qsub -q %s %s -l ncpus=%d" % (
           cmd, queue, args, ncpus)
    print cmd
    if not dry_run:
        call(cmd, shell=True)
    #MONITOR.print_jobs() 
