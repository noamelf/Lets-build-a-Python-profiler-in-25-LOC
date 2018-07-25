---

# Let’s Build a Python Profiler in 25 LOC! 
by Noam Elfanbaum

---

## About me

- Data Engineering lead at Bluevine
- Help organise [PywebIL](https://www.meetup.com/PyWeb-IL/) & [Pycon Israel](https://il.pycon.org/)
- Find me online at [@noamelf](https://twitter.com/noamelf) & [noamelf.com](https://noamelf.com)

Note:
- I'm working in a fintech startup called Bluevine
- I help organize the monthly Python meetup, and the yearly Israel Pycon (this year we had our 3 one)

---

## What is a program profile?

> A profile is a set of statistics that describes how often and for how long various parts of the program executed. 

Note:
- We can use profiling to debug slow programs, monitor our production environment and more.

---

## Python’s (stdlib) profilers

@ul

- Python has 2 builtin profilers in stdlib:
  - profile - an early pure Python implementation
  - cProfile - a C extended profiler for better performance

@ulend

Note:

- The best way to understand what is a the profiler is to see it in action.

---?code=src/profiling_demo.py&lang=python&title=Profiling demo 
@[2-3](Power a number twice)
@[6-7](Count the number of digits)
@[10-12](Run the functions)

Note:

- Run the code
- It takes quite some time, which part if the code is taking the most time?
- To see where does the program slows down, let's run the code and sort it by total time:
python -m cProfile foo.py
- This shows different parameters, but we want to know which function is taking the most total time
  So we can add the -s tottime and see it clearly.
- How can we make the count digit function more efficient?

---?code=src/optimized_demo.py&lang=python&title=Optimized demo 
@[9-10](Use log10 instead)

---

## It's magic! Right?

@ul

- When inside a Python program you have pretty easy access to its stack. 
- Most profilers run as part of your Python process. 

@ulend

Note: 
- So one of the most satisfying things for me in programming is to figure out how things actually work, 
and we're going to do just that!

---?code=src/stack_access.py&lang=python&title=Accessing the process call stack
@[6](Easily access the stack)
@[7](Extract the stack into a list of frames)
@[8-9](Print each frame line name, number, function name and actual code)
@[11-14](Call the code through some hierarchy)

Note:
- We saw we have a pretty easy way to understand where our program is at every given time, now let’s see 
how we trigger that functionality.

---

## Types of triggers -> type of profiles

- There are two types of profilers that differ upon their triggers: 
    - Deterministic profilers - triggered on function/line called (like profile/cProfile)
    - Statistical profilers - triggered on a time interval

---

## How do deterministic profilers work?

@ul

- Python let you specify a callback that gets run when interpreter events happen:
    - `sys.setprofile` - triggered when a function or a line of code is called
    - `sys.settrace` - triggered only when a function is called  
- When the callback gets called, it records the stack for later analysis.

@ulend

---?code=src/setprofile.py&lang=python&title=Using setprofile
@[6-8](Define a callback function)
@[11](Hook it to setprofile)
@[12](Execute some code)

---

## How do statistical profilers work?

@ul

- Statistical profilers sample the program on a given interval.   
- One way to implement the sampling is to ask the OS kernel to interrupt the program on a given interval.

@ulend

---?code=src/statistical_sampling.py&lang=python&title=Using OS signals to trigger sampling
@[4-6](A callback method that prints the current line)
@[8-11](Set the OS signal)
@[9](The handler will run each time SIGPROF will be recevied)
@[10](Set the start time and interval in which the signal will fire)
@[11-12](Nullify the alarm upon exit)
@[13](Set the sampler)
@[14-15](Run complex calculations)

Note:
- What do you think, when should we use which profiler?

---

## When to use which profiler?

@ul

- Statistical profilers:
  - Low, controllable and predicted overhead is possible by optimizing the sampling interval
  - Less accurate result since it, by design, misses function/line calls.
  - More suitable for continuous, low impact production monitoring.

@ulend
    
---

@ul

- Deterministic profilers:
  - Introduces a fixed amount of latency for every function call / line of code executed.
  - Collects the exact program execution stack
  - More suitable for interactive/local debugging.
  
@ulend

---

# Now, let’s build a (naive) statistical profiler in 25 LOC!

Note:
- We have all our pieces together now, to build our own statistical profiler, the only thing we need to think about is 
how to present the output.
- For this, there is a really cool project called flame graph that receives a fairly simple relative input, and produces 
beautiful graphs. 

---?code=src/sfProfiler.py&lang=python&title=Statistical Flame graph Profiler
@[15-19](The sampler trigger is set like before)
@[9-12](The sampler is collecting statistics about the stack visits)
@[10-11](Formatting the stack into a string, each level separated by a semi colon)
@[12](Counting the times the program spent in that call_stack)
@[22-26](Formatting the stats in Flame graph format - "some;stack count" )

Note:
- First let's see I'm not cheating: `cat sfProfiler.py | wc -l` 
- And this is with generous spacings!

---?code=src/sfp_demo1.py&lang=python&title=Simple usage of sfProfiler
@[4-10](main() calls calc() with 2 different numbers)
@[13-15](Starting the profiler, running the code, and printing the stats)

Note:
- The results are pretty clear,we can see that calc 100K took x time of our sampling and 200K took y time
- Now let’s visualize it: `python demo1.py | flamegraph | browser`

---?code=src/sfp_demo2.py&lang=python&title=A more complex example
@[7](Define cotroversial peps)
@[10-15](Download ans save peps to temp file)
@[18-21](Call save PEP on our predefined list)
@[24-26](Run under the profiler)

Note:
- The results for more complex programs are harder to understand, practically impossible but with flagraph 
visualization tool they are easy.
- python demo2.py | flamegraph | browser 

---

## Reference

@ul

- Brendan Gregg's [Flame Graph](https://github.com/brendangregg/FlameGraph) tool 
- Juila Evans [post](https://jvns.ca/blog/2017/12/17/how-do-ruby---python-profilers-work-/) about Ruby and Python profilers
- Nylas performance [post](https://www.nylas.com/blog/performance/) where they explain how they built a homemade performance monitoring service (recommended!).
- Python's [profilers](https://docs.python.org/3/library/profile.html) [docs](https://docs.python.org/3/library/sys.html#sys.setprofile)
- This talk can be found on [Github](https://github.com/noamelf/Lets-build-a-Python-profiler-in-25-LOC)

@ulend

---

Thanks!
