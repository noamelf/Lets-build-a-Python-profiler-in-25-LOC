import sys
import traceback


def show_stack():
    for _, frame in sys._current_frames().items():
        for line in reversed(traceback.extract_stack(frame)):
            print(f'{line.filename}:{line.lineno}:{line.name} - "{line.line}"')


def bar():
    show_stack()


bar()
