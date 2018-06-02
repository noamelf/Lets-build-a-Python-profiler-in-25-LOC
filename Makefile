1-profiling-demo:
	cd 1-profiling-demo && \
	pygmentize foo.py && \
	python -m cProfile foo.py

2-stack-access:
	cd 2-stack-access && \
	pygmentize stack_access.py && \
	python stack_access.py

3-detriminstic-profiler.set_profile:
	cd 3-detriminstic-profiler && \
	pygmentize d3_setprofile.py && \
	python d3_setprofile.py

3-detriminstic-profiler.recurison:
	cd 3-detriminstic-profiler && \
	pygmentize recursion.py && \
	time -f "%E elapsed" python recursion.py

3-detriminstic-profiler.recurison_w_profiler:
	cd 3-detriminstic-profiler && \
	time -f "%E elapsed" python -m cProfile recursion.py

4-statistical-profiler:
	cd 4-statistical-profiler && \
	python demo.py

5-flamegraph:
	python -m flamegraph  -F "%(fname)s:%(fun)s:%(line)s" -o perf.log foo.py
	sed -i 's#/home/noame/.virtualenvs/profiling-talk/lib/python3.6/site-packages##g' perf.log
	flamegraph.pl --title "MyScript CPU" perf.log > perf.svg
	chromium-browser perf.svg
