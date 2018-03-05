import sys
import traceback


def bar():
    foo()


def foo():
    for _, frame in sys._current_frames().items():
        for line in reversed(traceback.extract_stack(frame)):
            print(line)


bar()
