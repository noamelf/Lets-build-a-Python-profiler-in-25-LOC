---

# Let’s Build a Python Profiler in 25 LOC! 
by Noam Elfanbaum

---

## About me

- Data Engineering lead at Bluevine
- Involved with [PywebIL](https://www.meetup.com/PyWeb-IL/) & [Pycon Israel](https://il.pycon.org/)
- Find me online at [@noamelf](https://twitter.com/noamelf) and [noamelf.com](https://noamelf.com)

---

## What is profiling?

> A profile is a set of statistics that describes how often and for how long various parts of the program executed. 

---

## Python’s profilers
- Python has 2 builtin CPU profilers in stdlib:
  - profile - an early pure Python implementation
  - cProfile - a C extended profiler for better performance

---?code=src/profiling_demo.py&lang=python&title=Profiling demo 
@[2-3](Power a number twice)
@[6-7](Count the number of digits)
@[10-12](Run the functions)

Note:

- It takes quite some time, which part if the code is taking the most time? -->
- To see where does the program slows down, let's run the code and sort it by total time:
python -m cProfile foo.py
TODO: Maybe shows all the columns?
- This shows different parameters, but we want to know which function is taking the most total time
  So we can add the -s tottime and see it clearly.

---?code=src/optimized_demo.py&lang=python&title=Optimized demo 
@[8-9](Use log10 instead)

---

## How do profilers work?

- If you’re inside a Python program you generally have pretty easy access to its stack. 
- Most profilers run inside your Python process. 

<!--
pygmentize stack_access.py
python stack_access.py
We saw we have a pretty easy way to understand where our program is at every given time, now let’s see how we trigger that functionality.
-->

---

## Types of profilers
There are two types of profilers that differ upon their triggers: 
- Deterministic profilers - triggered on function/line called (like profile/cProfile)
- Statistical profilers - triggered on a time interval

---

## How do deterministic profilers work?
Python let you specify a callback that gets run when interpreter events happen:
- `sys.setprofile` - triggered when a function or a line of code is called
- `sys.settrace` - triggered only when a function is called  

When the callback gets called, it records the stack for later analysis.

<!--
cd ../3-detriminstic-profiler
pygmentize setprofile.py 
python setprofile.py
-->

---

## Disadvantage of Deterministic profilers
- Introduces a fixed amount of latency for every function call / line of code executed.
Standard programs does not have so many function calls.
> “The interpreted nature of Python tends to add so much overhead to execution, that deterministic profiling tends to only add small processing overhead in typical applications”

<!--
Run:
But there is a disadvantage to using deterministic profilers in production settings, can any one think of one?
pygmentize bar.py
python bar.py
python -m cProfile bar.py
-->

---

## How do statistical profilers work?
- Statistical profilers sample the program on a given interval. 
- It has less overhead than deterministic profiler, but is also less accurate.  
- One way to implement the sampling is to ask the OS kernel to interrupt the program on a given interval.

<!--
Pygmentize alert.py
Python alert.py
-->

---

# Now, let’s build a (naive) statistical profiler in 25 LOC!

<!--
Let's connect all the dots to our own statistical profile in 25 LOC.
I wanted to write it live with you guys, but it I was afraid it wouldn’t work, so I wrote it down in advance.
First let’s see I’m not foolling you guys. 
pygmentize sProfiler.py | wc -l
pygmentize sProfiler.py
The output is built in such a way that we can visualize it easily with a tool called flamegraph.

To test our proflier we’re going to use a simple program called demo1
pygmentize demo1.py
python demo1.py
The results are pretty clear,we can see that calc 100K took x time of our sampling and 200K took y time
Now let’s visualize it:
python demo1.py | flamegraph | browser .

Now let’s run a more complex program
pygmentize demo2.py
python demo2.py
The results for more complex programs are harder to understand, practically impossible but with flagraph visualization tool they are easy.
python demo2.py | flamegraph | browser 
-->

---

## Reference
- Talk code repository
- Juila Evans blog post - https://jvns.ca/blog/2017/12/17/how-do-ruby---python-profilers-work-/
- Nylas blog post - https://www.nylas.com/blog/performance/
- Flame Graph by Brendan Gregg https://github.com/brendangregg/FlameGraph 
- Python documentation about profilers -
  - https://docs.python.org/3/library/profile.html
  - https://docs.python.org/3/library/sys.html#sys.setprofile

---

Thanks!
