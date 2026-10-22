#!/usr/bin/env python3
"""Import the owner's project catalog without deleting existing projects."""
import json
import subprocess
from compose import ROOT, command

catalog = json.loads((ROOT / 'db/portfolio-projects.json').read_text(encoding='utf-8'))
assert len({item['link'] for item in catalog}) == len(catalog)
code = r'''
import mysql from 'mysql2/promise';
let input = ''; for await (const chunk of process.stdin) input += chunk;
const projects = JSON.parse(input);
const db = await mysql.createConnection({host: process.env.DB_HOST || 'mysql', user: 'portfolio_app', password: process.env.APP_DB_PASSWORD, database: 'portfolio', charset: 'utf8mb4'});
try {
  await db.beginTransaction();
  const [original] = await db.execute('SELECT id FROM projects WHERE id=7');
  if (!original.length) throw new Error('Portfolio project 7 is missing');
  await db.execute('UPDATE projects SET title=?, link=? WHERE id=7', ['Dự án Portfolio và quản trị hệ thống', 'https://github.com/tamtran2k6zz/Website_Portfolio_De13']);
  for (const project of projects) {
    const values = [project.title, project.description, project.stack, project.link];
    const [existing] = await db.execute('SELECT id FROM projects WHERE link=?', [project.link]);
    if (existing.length) await db.execute('UPDATE projects SET title=?, description=?, stack=?, link=? WHERE id=?', [...values, existing[0].id]);
    else await db.execute('INSERT INTO projects(title,description,stack,link) VALUES(?,?,?,?)', values);
  }
  await db.commit();
  console.log('Updated portfolio title and synchronized ' + projects.length + ' GitHub projects.');
} catch (error) { await db.rollback(); throw error; }
finally { await db.end(); }
'''
subprocess.run(command(3) + ['exec', '-T', 'app', 'node', '--input-type=module', '-e', code], input=json.dumps(catalog).encode(), cwd=ROOT, check=True)
