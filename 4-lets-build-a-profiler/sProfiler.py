import atexit
import collections
import signal
import traceback

INTERVAL = 0.005

stats = collections.defaultdict(int)


def _sample(signum, frame):
    stack = traceback.extract_stack(frame)
    formatted_stack = ';'.join(line.line for line in stack)
    stats[formatted_stack] += 1


def start(interval=INTERVAL):
    signal.signal(signal.SIGPROF, _sample)
    signal.setitimer(signal.ITIMER_PROF, interval, interval)
    atexit.register(lambda: signal.setitimer(signal.ITIMER_PROF, 0))


def format_stats():
    stack_count = [f'{stack} {count}' for stack, count in stats.items()]
    return '\n'.join(stack_count)
