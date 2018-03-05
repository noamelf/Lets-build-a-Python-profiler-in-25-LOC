#!/usr/bin/env bash

echo "Without profiler:"
time -f "\n%E elapsed" python recursion.py

echo "With tracing profiler:"
time -f "\n%E elapsed" python -m cProfile recursion.py

echo "With sampling profiler:"
time -f "\n%E elapsed" python recursion_with_sampler.py

