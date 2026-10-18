#!/usr/bin/env python3
"""Create local-only secrets. Refuse to overwrite an initialized deployment."""
from pathlib import Path
import secrets
import os
ROOT = Path(__file__).resolve().parents[1]

def main():
    env = ROOT / '.env'
    secret_dir = ROOT / 'secrets'
    if env.exists() or (secret_dir / 'exporter.cnf').exists():
        raise SystemExit('Existing .env/secrets detected. Keep them; setup must run only once per fresh deployment.')
    values = {
        'MYSQL_ROOT_PASSWORD': secrets.token_hex(24),
        'APP_DB_PASSWORD': secrets.token_hex(24),
        'MYSQL_MONITOR_PASSWORD': secrets.token_hex(24),
        'SESSION_SECRET': secrets.token_hex(32),
        'ADMIN_USERNAME': 'admin',
        'ADMIN_INITIAL_PASSWORD': secrets.token_hex(16),
        'GRAFANA_ADMIN_PASSWORD': secrets.token_hex(16),
        'COOKIE_SECURE': 'false', 'WEB_PORT': '8080', 'PMA_PORT': '8081'
    }
    secret_dir.mkdir(mode=0o700, exist_ok=True)
    env.write_text(''.join(f'{key}={value}\n' for key,value in values.items()), encoding='utf-8')
    os.chmod(env, 0o600)
    cnf = secret_dir / 'exporter.cnf'
    cnf.write_text('[client]\nuser=exporter\npassword='+values['MYSQL_MONITOR_PASSWORD']+'\n', encoding='utf-8')
    # Exporter image runs as nobody; container bind mount must be readable.
    # The host parent directory is 0700 and this entire folder is gitignored.
    os.chmod(cnf, 0o644)
    print('Created .env and secrets/exporter.cnf. Open .env privately for login credentials. No secrets were printed.')

if __name__ == '__main__': main()
