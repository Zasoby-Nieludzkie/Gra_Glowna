#!/usr/bin/env python3
"""Konfiguruje GitHub Projects i opcjonalnie początkowe Issues przez GH CLI.

Bez --apply: DRY RUN. Nie przechowuje ani nie prosi o token GitHub.
Uruchom z root folderu paczki/istniejącego repo, np.
python scripts/setup_github.py --repo ORG/REPO --project-owner ORG --apply --seed-issues
"""
import argparse
import csv
import json
import shutil
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SEED = BASE / 'project-template' / 'initial-issues.csv'
LABELS = {
  'io': ('7251B5', 'Praca rozliczana na Inżynierii Oprogramowania'),
  'io-deliverable': ('A372E3', 'Materiał do oddania na PZE'),
  'engineering': ('2563EB', 'Programowanie i rozwiązania techniczne'),
  'game-design': ('009D73', 'Projektowanie mechanik i zawartości'),
  'art': ('EA71B0', 'Grafika i animacja'),
  'audio': ('CF8C25', 'Dźwięk i muzyka'),
  'qa': ('E6AC39', 'Testy i jakość'),
  'documentation': ('64748B', 'Dokumentacja, raporty, prezentacje'),
  'production': ('B45309', 'Zarządzanie produkcją'),
  'bug': ('C73838', 'Usterka oprogramowania'),
}
FIELDS = [
 ('Priority', 'SINGLE_SELECT', 'P0,P1,P2,P3'),
 ('Workstream', 'SINGLE_SELECT', 'Engineering,Game Design,Art,Audio,QA,Documentation,Production'),
 ('Estimated hours', 'NUMBER', None),
 ('Actual hours', 'NUMBER', None),
 ('Target date', 'DATE', None),
]

def run(args, fatal=True):
    print('> ' + ' '.join(args), flush=True)
    r = subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode and fatal:
        print(r.stderr.strip(), file=sys.stderr)
        raise RuntimeError('Polecenie nie zostało wykonane')
    if r.returncode:
        print('OSTRZEŻENIE: ' + r.stderr.strip(), file=sys.stderr)
    return r

p=argparse.ArgumentParser(description='GitHub Project starter: IO + game development')
p.add_argument('--repo', required=True, help='OWNER/REPO z istniejącym projektem Unity')
p.add_argument('--project-owner', required=True, help='Login organizacji lub właściciela GitHub Project')
p.add_argument('--project-number', type=int, help='Jeżeli projekt już istnieje, podaj jego numer')
p.add_argument('--project-title', default='Game Production – IO + Cyberiada')
p.add_argument('--seed-issues', action='store_true', help='Dodaj początkowe Issues z CSV')
p.add_argument('--apply', action='store_true', help='Wykonaj działania na GitHub (bez tego podgląd)')
a=p.parse_args()

if a.repo.count('/') != 1:
    p.error('--repo musi mieć postać OWNER/REPO')
if not a.apply:
    print('PODGLĄD – żadne operacje nie zostaną wykonane na GitHubie.')
    print(f'Repo: {a.repo}; Project owner: {a.project_owner}; existing project number: {a.project_number or "nowy"}')
    print('Zostaną utworzone brakujące etykiety i pola Project (jeśli uda się je utworzyć).')
    if a.seed_issues:
        with SEED.open(encoding='utf-8-sig',newline='') as f:
            rows=list(csv.DictReader(f))
        print(f'Seed issues: {len(rows)}')
        for x in rows: print(' - '+x['title'])
    print('Zastosuj: dodaj --apply. Ewentualne widoki ustaw ręcznie w UI GitHub.')
    sys.exit(0)
if not shutil.which('gh'):
    p.error('Brak gh CLI w PATH. Zainstaluj https://cli.github.com/')
run(['gh','auth','status'])
# Sprawdź dostęp do repo przed tworzeniem zasobów.
run(['gh','repo','view',a.repo,'--json','name'])
print('\n== Etykiety ==')
for name,(color,description) in LABELS.items():
    run(['gh','label','create',name,'--repo',a.repo,'--color',color,'--description',description],fatal=False)

if a.project_number:
    project_num = a.project_number
    run(['gh','project','view',str(project_num),'--owner',a.project_owner])
else:
    print('\n== Tworzenie nowego Project ==')
    result = run(['gh','project','create','--owner',a.project_owner,'--title',a.project_title,'--format','json'])
    try: project_num = int(json.loads(result.stdout)['number'])
    except Exception as exc: raise RuntimeError('Nie udało się odczytać numeru Project z gh CLI') from exc
print('Project number:',project_num)
run(['gh','project','link',str(project_num),'--owner',a.project_owner,'--repo',a.repo],fatal=False)

print('\n== Pola ==')
for name,typ,values in FIELDS:
    cmd=['gh','project','field-create',str(project_num),'--owner',a.project_owner,'--name',name,'--data-type',typ]
    if values: cmd+=['--single-select-options',values]
    run(cmd,fatal=False)

if a.seed_issues:
    print('\n== Pierwsze Issues ==')
    all_issues=run(['gh','issue','list','--repo',a.repo,'--state','all','--limit','500','--json','title'])
    existing={x['title'] for x in json.loads(all_issues.stdout)}
    with SEED.open(encoding='utf-8-sig',newline='') as f:
        rows=list(csv.DictReader(f))
    for entry in rows:
        if entry['title'] in existing:
            print('SKIP (istniejący tytuł):',entry['title']);continue
        labels=entry['labels'].split(';')
        body=f"""**Zakres:** {entry['description']}

**Kryteria ukończenia:** {entry['acceptance_criteria']}

**Sugerowany odpowiedzialny:** {entry['suggested_owner']} (do zatwierdzenia)

**Termin:** {entry['target_date']}

**Estymata:** do uzupełnienia przed rozpoczęciem prac.
**Ewidencja czasu:** komentarze zgodnie z docs/IO/02-time-tracking.md (jeśli dotyczy).

_Seed: {entry['key']}. Wartości są propozycją, zespół może je zmienić._
"""
        args=['gh','issue','create','--repo',a.repo,'--title',entry['title'],'--body',body]
        for label in labels: args+=['--label',label]
        r=run(args,fatal=False)
        if r.returncode: continue
        url=r.stdout.strip().splitlines()[-1]
        if not url.startswith('http'):
            print('Nie rozpoznano URL Issue, uzupełnij Project ręcznie',file=sys.stderr);continue
        if run(['gh','project','item-add',str(project_num),'--owner',a.project_owner,'--url',url],fatal=False).returncode:
            print('Dodaj ręcznie Issue do Projects:',url,file=sys.stderr);continue
        for field,value in [('Priority',entry['priority'])]:
            run(['gh','project','item-edit',str(project_num),'--owner',a.project_owner,'--url',url,'--field',field,'--value',value],fatal=False)
        run(['gh','project','item-edit',str(project_num),'--owner',a.project_owner,'--url',url,'--field','Target date','--date',entry['target_date']],fatal=False)

print('\nGotowe. Ręcznie ustaw widoki w GitHub Projects wg project-template/PROJECT-SETUP.md.')
print('Szczegółowe przypisania i estymaty pozostawiono zespołowi; nie wstawiono fikcyjnych godzin.')
