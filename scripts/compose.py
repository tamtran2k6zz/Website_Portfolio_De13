#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[1]
FILES = ['compose.yaml', 'compose.monitoring.yaml', 'compose.logging.yaml']

def command(stage):
    if stage not in (1,2,3): raise ValueError('stage must be 1, 2 or 3')
    return ['docker','compose', *sum((['-f',name] for name in FILES[:stage]), [])]

if __name__ == '__main__':
    if len(sys.argv) < 3: raise SystemExit('Usage: python3 scripts/compose.py STAGE COMMAND [ARGS]')
    raise SystemExit(subprocess.call(command(int(sys.argv[1])) + sys.argv[2:], cwd=ROOT))
