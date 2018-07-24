import signal
import time


def handler(signum, call_stack):
    print(signum, call_stack)
    signal.alarm(1)


signal.signal(signal.SIGALRM, handler)
signal.alarm(1)

time.sleep(5)

signal.alarm(0)
