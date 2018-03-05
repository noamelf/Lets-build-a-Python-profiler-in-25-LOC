profiling-demo:
	python foo.py

extract-stack-trace:
	python extract_stack_trace.py

recursion:
	time -f "\t%E elapsed" python recursion.py

recursion-with-tracing:
	time -f "\t%E elapsed" python -m cProfile recursion.py

stack-sampler-demo:
	python stacksampler-demo.py

recursion-with-sampler:
	time -f "\t%E elapsed" python recursion_with_sampler.py

flamegraph:
	python -m flamegraph  -F "%(fname)s:%(fun)s:%(line)s" -o perf.log foo.py
	sed -i 's#/home/noame/.virtualenvs/profiling-talk/lib/python3.6/site-packages##g' perf.log
	flamegraph.pl --title "MyScript CPU" perf.log > perf.svg
	chromium-browser perf.svg
