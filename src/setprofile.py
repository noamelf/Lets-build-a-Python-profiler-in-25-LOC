# setprofile.py
import sys
import traceback

def profiler(call_stack, event, arg):
    # if event == 'c_call':
        line = traceback.extract_stack(call_stack)[0]
        print(f'Function is: {arg}')
        print(f'Line executed is: {line.line}')

sys.setprofile(profiler)
print('Hello world!')
