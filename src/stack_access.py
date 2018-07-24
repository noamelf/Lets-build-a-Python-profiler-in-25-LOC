# stack_access.py
import sys
import traceback

def show_stack():
    for _, call_stack in sys._current_frames().items():
        for frame in traceback.extract_stack(call_stack):
            print(f'{frame.filename}:{frame.lineno}:'
                  f'{frame.name} - "{frame.line}"')

def bar():
    show_stack()

bar()
