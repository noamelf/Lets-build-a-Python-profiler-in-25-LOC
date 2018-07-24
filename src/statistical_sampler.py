# statistical_sampler.py
import signal, time, traceback

def handler(signum, call_stack):
    line = traceback.extract_stack(call_stack)[0]
    print(f'line: {line.line} (signum={signum})')
    signal.alarm(1)

signal.signal(signal.SIGALRM, handler)
signal.alarm(1)

time.sleep(3)

signal.alarm(0)
