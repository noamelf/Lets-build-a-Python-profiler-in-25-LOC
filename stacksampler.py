import atexit
import collections
import signal
import time


class Sampler:
    """
    A simple stack sampler for low-overhead CPU profiling: samples the call
    stack every `interval` seconds and keeps track of counts by frame. Because
    this uses signals, it only works on the main thread.
    """

    def __init__(self, interval=0.005):
        self.interval = interval
        self._started = None
        self._stack_counts = collections.defaultdict(int)

    def start(self):
        self._started = time.time()
        signal.signal(signal.SIGVTALRM, self._sample)

        signal.setitimer(signal.ITIMER_VIRTUAL, self.interval)
        atexit.register(self.stop)

    def _sample(self, signum, frame):
        stack = []
        while frame is not None:
            stack.append(self._format_frame(frame))
            frame = frame.f_back

        stack = ';'.join(reversed(stack))
        self._stack_counts[stack] += 1
        signal.setitimer(signal.ITIMER_VIRTUAL, self.interval)

    def _format_frame(self, frame):
        return '{}({})'.format(frame.f_code.co_name,
                               frame.f_globals.get('__name__'))

    def output_stats(self):
        if self._started is None:
            return ''
        elapsed = time.time() - self._started
        lines = ['elapsed {}'.format(elapsed),
                 'granularity {}'.format(self.interval)]
        ordered_stacks = sorted(self._stack_counts.items(),
                                key=lambda kv: kv[1], reverse=True)
        lines.extend(['{} {}'.format(frame, count)
                      for frame, count in ordered_stacks])
        return '\n'.join(lines) + '\n'

    def reset(self):
        self._started = time.time()
        self._stack_counts = collections.defaultdict(int)

    def stop(self):
        self.reset()
        signal.setitimer(signal.ITIMER_VIRTUAL, 0)

    def __del__(self):
        self.stop()
