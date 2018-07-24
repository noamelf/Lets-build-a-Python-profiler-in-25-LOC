import sys
import tempfile
import urllib.request

from src import sfProfiler


def local_pep(pep):
    with urllib.request.urlopen(f'https://www.python.org/dev/peps/pep-{pep:04}') as request:
        html = request.read()
    with tempfile.TemporaryFile('wb') as f:
        f.write(html)


def main():
    for pep in range(1, 4):
        local_pep(pep)
        print(f'Download pep {pep} successfully', file=sys.stderr)


sfProfiler.start()
main()
print(sfProfiler.format_stats())
