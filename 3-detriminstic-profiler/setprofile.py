import sys
import traceback


def profiler(call_stack, event, arg):
    if event == 'c_call':
        line = traceback.extract_stack(call_stack)[0]
        print(arg)
        print(line.line)


sys.setprofile(profiler)
print('Hello world!')
