## stdlib
import time, os, sys, subprocess
import signal, multiprocessing, traceback, contextlib

## local 
from ..utils import progress_bar


##-----------------------------------------------------------------------------
## -- plain exception cacher 
##-----------------------------------------------------------------------------
class WorkerError(Exception):
    pass

##-----------------------------------------------------------------------------
## - - process class 
##-----------------------------------------------------------------------------
class Worker(multiprocessing.Process):
    def __init__(self):
        super(Worker, self).__init__()
        self.result = multiprocessing.Queue()
        
    @property
    def output(self):
        return self.result.get()
                
    def run(self):
        try:
            self.result.put(self.work())
        except Exception, err:
            t, v, tb = sys.exc_info()
            e = WorkerError()
            e.tb = traceback.format_tb(tb)
            self.result.put(e)
        
##-----------------------------------------------------------------------------
## - - process class with a work method 
##-----------------------------------------------------------------------------
class FuncWorker(Worker):
    def __init__(self, func, *args, **kwargs):
        super(FuncWorker, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def work(self):
        return self.func(*self.args, **self.kwargs)

##------------------------------------------------------------------------------
## - - simple class for parallel processing
##------------------------------------------------------------------------------
class Job(multiprocessing.Process):
    """
    simpel worker class for parallel
    processing. the run method is necessary to overload the run method of Procces.
    """
    
    def __init__(self, workfunc, *args, **kwargs):
        super(Job, self).__init__()
        self.workfunc = workfunc
        self.args = args
        self.kwargs = kwargs
        
    def run(self):
        return self.workfunc(*self.args, **self.kwargs)

    
##-----------------------------------------------------------------------------
## - - some helper functions
##-----------------------------------------------------------------------------
def run_pool(workers, n_jobs=-1, sleep=0.1, show_status=False):
    """
    """
    # defensive copy
    num_workers = len(workers)
    workers = workers[:]
    if n_jobs < 1:
        n_jobs = multiprocessing.cpu_count()
    processes = []
    p = None
    try:
        while True:
            active = multiprocessing.active_children()
            while len(active) < n_jobs and len(workers) > 0:
                p = workers.pop(0)
                p.start()
                processes.append(p)
                active = multiprocessing.active_children()
            if len(workers) == 0 and len(active) == 0:
                break
            time.sleep(sleep)
            if show_status:
                progress_bar(len(active), num_workers, prefix = 'active/all:', suffix = '', length = 50)
                
    except KeyboardInterrupt, SystemExit:
        if p is not None:
            p.terminate()
        for p in processes:
            p.terminate()
        raise

##-----------------------------------------------------------------------------
def map_pool(process, args, n_jobs=-1, **kwargs):
    """
    """
    procs = [process(*arg, **kwargs) for arg in args]
    run_pool(procs, n_jobs=n_jobs)
    return [p.output for p in procs]


##-----------------------------------------------------------------------------
def map_pool_kwargs(process, kwargs, n_jobs=-1):
    """
    """
    procs = [process(**args) for args in kwargs]
    run_pool(procs, n_jobs=n_jobs)
    return [p.output for p in procs]
 

##-----------------------------------------------------------------------------
def kill_child_processes(signum, frame):
    """ helper for killing all child processes. 
    """
    parent_id = os.getpid()
    ps_command = subprocess.Popen(
        "ps -o pid --ppid %d --noheaders" % parent_id, shell=True, stdout=subprocess.PIPE)
    ps_output = ps_command.stdout.read()
    retcode = ps_command.wait()
    for pid_str in ps_output.strip().split("\n")[:-1]:
        os.kill(int(pid_str), signal.SIGTERM)
    sys.exit()
    
##-----------------------------------------------------------------------------
def close_pool(pool):
    """
    """
    original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGINT, original_sigint_handler)
    try:
        with contextlib.closing(pool) as pll:
            yield pll
    except Exception as exc:
        syslog.syslog(syslog.LOG_WARNING,
                      "Terminate pool due to {0}".format(exc))
        pool.terminate()
        raise
    except SystemExit, KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating workers")
        pool.terminate()
    finally:
        pool.join() 
