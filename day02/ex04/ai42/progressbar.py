from time import sleep
import time


def ft_progress(lst):
    fmt = "ETA: {:.2f}s [{:3d}%][{}] {}/{}| elapsed time {:.2f}s"
    total = len(lst) - 1
    start = time.time()
    for i, el in enumerate(lst):
        now = time.time()
        elapsed = now - start
        eta = elapsed * ((total+1) / (i+1)) - elapsed
        percent = int(i/total*100)
        bar_count = int(percent/4)
        bar = "="*bar_count + ">"*(bar_count < 25) + " "*(24-bar_count)
        print('\r'+fmt.format(eta, percent, bar, i+1, total+1, elapsed), end='')
        yield el
