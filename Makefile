1-profiling-demo:
	python -m cProfile foo.py

2-extract-stack-trace:
	python extract_stack_trace.py

3-recursion:
	time -f "\t%E elapsed" python recursion.py

4-recursion-with-tracing:
	time -f "\t%E elapsed" python -m cProfile recursion.py

5-stack-sampler-demo:
	python stacksampler-demo.py

6-comparision:
	@echo "Without profiler:"
	time -f "\n%E elapsed\n" python recursion.py

	@echo "With tracing profiler:"
	time -f "\n%E elapsed\n" python -m cProfile recursion.py

	@echo "With sampling profiler:"
	time -f "\n%E elapsed\n" python recursion_with_sampler.py


7-flamegraph:
	python -m flamegraph  -F "%(fname)s:%(fun)s:%(line)s" -o perf.log foo.py
	sed -i 's#/home/noame/.virtualenvs/profiling-talk/lib/python3.6/site-packages##g' perf.log
	flamegraph.pl --title "MyScript CPU" perf.log > perf.svg
	chromium-browser perf.svg
