import sys
import traceback


def profiler(frame, event, arg):
    if event == 'c_call':
        line = traceback.extract_stack(frame)[0]
        print(arg)
        print(line.line)


sys.setprofile(profiler)
print('Hello world!')
