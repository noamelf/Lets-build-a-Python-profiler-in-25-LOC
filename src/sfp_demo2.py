import sys
import tempfile
import urllib.request

import sfProfiler

CONTROVERSIAL_PEPS = (3000, 572)


def save_pep(pep):
    url = f'https://www.python.org/dev/peps/pep-{pep:04}'
    with urllib.request.urlopen(url) as request:
        html = request.read()
    with tempfile.TemporaryFile('wb') as f:
        f.write(html)


def main():
    for pep in CONTROVERSIAL_PEPS:
        save_pep(pep)
        print(f'Download pep {pep} successfully', file=sys.stderr)


sfProfiler.start()
main()
print(sfProfiler.format_stats())
