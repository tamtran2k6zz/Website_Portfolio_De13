#!/usr/bin/env python3
"""HTTP checks against your local Docker deployment; no database mocking."""
import argparse
import http.cookiejar
import re
import urllib.request
import urllib.parse
import urllib.error
import ssl
from compose import ROOT

parser = argparse.ArgumentParser()
parser.add_argument('--base', default='http://localhost:8080')
parser.add_argument('--ca-file', help='Trust the local self-signed certificate for HTTPS checks')
args = parser.parse_args()
env = dict(line.split('=',1) for line in (ROOT/'.env').read_text().splitlines() if '=' in line and not line.startswith('#'))
jar = http.cookiejar.CookieJar()
handlers = [urllib.request.HTTPCookieProcessor(jar)]
if args.ca_file:
    handlers.append(urllib.request.HTTPSHandler(context=ssl.create_default_context(cafile=args.ca_file)))
client = urllib.request.build_opener(*handlers)

def request(path, values=None):
    data = urllib.parse.urlencode(values).encode() if values is not None else None
    try:
        response = client.open(args.base.rstrip('/')+path, data, timeout=15)
    except urllib.error.HTTPError as error: response = error
    return response.status, response.read().decode(), response.headers

status, body, headers = request('/')
assert status == 200
assert headers.get('X-Content-Type-Options') == 'nosniff'
assert headers.get('Content-Security-Policy')
assert request('/health')[0] == 200
assert request('/not-found-demo')[0] == 404
assert request('/admin')[0] == 403
status, body, _ = request('/login')
token = re.search(r'name="_csrf" value="([a-f0-9]+)"', body).group(1)
assert request('/login', {'username':'admin','password':'invalid'})[0] == 403
status, body, _ = request('/login', {'_csrf':token,'username':env['ADMIN_USERNAME'],'password':env['ADMIN_INITIAL_PASSWORD']})
assert status == 200 and 'Quản trị Portfolio' in body, 'Login failed. If you changed the admin password, run browser checks instead.'
print('PASS: public page, health, headers, 404, admin access control, CSRF and admin login. Screenshots and metrics/log checks remain manual.')
