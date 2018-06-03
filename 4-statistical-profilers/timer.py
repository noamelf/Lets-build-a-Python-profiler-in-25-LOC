import signal
from urllib.request import urlopen


def handler(signum, frame):
    raise ConnectionError('Too long to connect')


signal.signal(signal.SIGALRM, handler)
signal.alarm(2)

urlopen('http://localhost:5000')

signal.alarm(0)
