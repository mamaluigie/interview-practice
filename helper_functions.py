import datetime
import pdb

def trunc(n):
    return(n * 100 // 1 * 0.01)

def time_for_func_to_run(*args):
    now = datetime.datetime.now().timestamp()
    func = args[0]
    output = func(*args[1:])
    return datetime.datetime.now().timestamp() - now
