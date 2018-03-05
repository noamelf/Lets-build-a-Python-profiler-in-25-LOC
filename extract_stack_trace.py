import sys
import traceback

def bar():
    foo()

def foo():
    for _, frame in sys._current_frames().items():
        for line in traceback.extract_stack(frame):
            print(line)

bar()