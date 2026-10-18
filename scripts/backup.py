#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import subprocess
from compose import command, ROOT

folder = ROOT / 'backups'
folder.mkdir(mode=0o700, exist_ok=True)
destination = folder / ('portfolio-' + datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S') + '.sql')
cmd = command(1) + ['exec','-T','mysql','sh','-c', 'MYSQL_PWD="$MYSQL_ROOT_PASSWORD" exec mysqldump -uroot --single-transaction --no-tablespaces --set-gtid-purged=OFF --default-character-set=utf8mb4 portfolio']
with destination.open('wb') as out:
    result = subprocess.run(cmd, cwd=ROOT, stdout=out)
if result.returncode:
    destination.unlink(missing_ok=True)
    raise SystemExit(result.returncode)
destination.chmod(0o600)
print('Backup created:', destination.name)
