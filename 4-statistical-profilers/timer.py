import signal
from urllib.request import urlopen

TIMEOUT = 3


def handler(signum, call_stack):
    raise TimeoutError(f'Connection took more than {TIMEOUT} seconds')


signal.signal(signal.SIGALRM, handler)
signal.alarm(TIMEOUT)

urlopen('http://localhost:5000')

signal.alarm(0)
