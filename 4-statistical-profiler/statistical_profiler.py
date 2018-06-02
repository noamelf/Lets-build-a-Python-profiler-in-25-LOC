import atexit
import collections
import signal
import traceback

INTERVAL = 0.005

stats = collections.defaultdict(int)


def start():
    signal.signal(signal.SIGVTALRM, sample)
    signal.setitimer(signal.ITIMER_VIRTUAL, INTERVAL)
    atexit.register(lambda: signal.setitimer(signal.ITIMER_VIRTUAL, 0))


def sample(signum, frame):
    stack = '; '.join(line.line for line in traceback.extract_stack(frame))
    stats[stack] += 1
    signal.setitimer(signal.ITIMER_VIRTUAL, INTERVAL)


def format_stats():
    stack_count = [f'[{stack}]: {count}' for stack, count in stats.items()]
    return '\n'.join(stack_count)
