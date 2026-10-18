#!/usr/bin/env python3
"""Restore into a separate database; never overwrite portfolio."""
from pathlib import Path
import subprocess
import sys
from compose import command, ROOT

if len(sys.argv) != 2: raise SystemExit('Usage: python3 scripts/restore-test.py backups/FILE.sql')
backup = Path(sys.argv[1]).resolve()
if not backup.is_file(): raise SystemExit('Backup file not found')
base = command(1) + ['exec','-T','mysql','sh','-c']
# CREATE without IF NOT EXISTS prevents accidental reuse/overwrite.
subprocess.run(base + ['MYSQL_PWD="$MYSQL_ROOT_PASSWORD" exec mysql -uroot -e "CREATE DATABASE portfolio_restore_test CHARACTER SET utf8mb4"'], cwd=ROOT, check=True)
with backup.open('rb') as source:
    subprocess.run(base + ['MYSQL_PWD="$MYSQL_ROOT_PASSWORD" exec mysql -uroot --default-character-set=utf8mb4 portfolio_restore_test'], cwd=ROOT, stdin=source, check=True)
subprocess.run(base + ['MYSQL_PWD="$MYSQL_ROOT_PASSWORD" exec mysql -uroot -e "SELECT COUNT(*) AS restored_projects FROM portfolio_restore_test.projects; SELECT COUNT(*) AS restored_skills FROM portfolio_restore_test.skills; SELECT COUNT(*) AS source_projects FROM portfolio.projects"'], cwd=ROOT, check=True)
print('Restored to portfolio_restore_test. Compare table counts/content; portfolio is unchanged.')
