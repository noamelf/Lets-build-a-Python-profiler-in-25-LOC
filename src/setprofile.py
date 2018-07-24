# setprofile.py
import sys
import traceback


def profiler(call_stack, event, arg):
    line = traceback.extract_stack(call_stack)[0]
    print(f'arg: {arg} | event: {event} | line: {line.line}')


sys.setprofile(profiler)
print('Hello world!')
