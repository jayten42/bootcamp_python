import time
from random import randint


def log(function):
    def _log(*args, **kwargs):
        start = time.time()
        ret = function(*args, **kwargs)
        name = " ".join([word.capitalize() for word in function.__name__.split('_')])
        fmt = "(cmaxtime)Running: {:20s}\t[ exec-time = {:0.3f} {:2s} ]\n"
        with open("machine.log", 'a') as f:
            exec_time = time.time() - start
            f.write(fmt.format(name, exec_time, "s" if exec_time >= 1 else "ms"))
        return ret
    return _log
