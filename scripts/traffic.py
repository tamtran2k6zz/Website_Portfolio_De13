#!/usr/bin/env python3
"""Generate bounded local traffic for dashboard and 404 log evidence."""
import argparse
import urllib.request
import urllib.error
from urllib.parse import urlparse
parser = argparse.ArgumentParser()
parser.add_argument('--base', default='http://localhost:8080')
parser.add_argument('--count', type=int, default=30)
args=parser.parse_args()
if urlparse(args.base).hostname not in ('localhost','127.0.0.1'): raise SystemExit('This demo script only targets localhost/127.0.0.1')
if not 1 <= args.count <= 100: raise SystemExit('count must be between 1 and 100')
counts={}
for i in range(args.count):
    path='/demo-missing-page' if i % 5 == 0 else '/'
    try:
        with urllib.request.urlopen(args.base.rstrip('/')+path, timeout=10) as response: status=response.status
    except urllib.error.HTTPError as response: status=response.code
    counts[status]=counts.get(status,0)+1
print('Requests complete:', counts)
