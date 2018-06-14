import multiprocessing
import time
import dill

from ..utils import progress_bar

##-----------------------------------------------------------------------------
## 
class Worker(multiprocessing.Process):
    def __init__(self):
        super(Worker, self).__init__()
        self.result = multiprocessing.Queue()
        
    @property
    def output(self):
        return self.result.get()

    def run(self):
        self.result.put(self.work())

##-----------------------------------------------------------------------------
## 
class FuncWorker(Worker):
    def __init__(self, func, *args, **kwargs):
        super(FuncWorker, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def work(self):
        return self.func(*self.args, **self.kwargs)


##-----------------------------------------------------------------------------
## 
def run_pool(workers, n_jobs=-1, sleep=0.1, show_status=False):
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
## 
def map_pool(process, args, n_jobs=-1, **kwargs):
    procs = [process(*arg, **kwargs) for arg in args]
    run_pool(procs, n_jobs=n_jobs)
    return [p.output for p in procs]


##-----------------------------------------------------------------------------
## 
def map_pool_kwargs(process, kwargs, n_jobs=-1):
    procs = [process(**args) for args in kwargs]
    run_pool(procs, n_jobs=n_jobs)
    return [p.output for p in procs]
 


##------------------------------------------------------------------------------
## simple class for parallel processing
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
