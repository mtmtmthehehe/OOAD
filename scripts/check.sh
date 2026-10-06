#!/usr/bin/env bash
set -u
fail=0

echo "== 1. Bảng lệch cột =="
for f in $(find docs -name '*.md'); do
  awk -v f="$f" '/^\|/ {n=gsub(/\|/,"|"); if(!h){h=n} else if(n!=h){print f": dòng "NR" lệch cột"} next} {h=0}' "$f"
done

echo "== 2. Truy vết BR/FR/UC/CLS/TC (kèm số lượng, link, độ mới PNG) =="
python3 scripts/check_trace.py || fail=1

echo "== 3. Cú pháp PlantUML =="
for f in $(find docs -name '*.puml'); do
  java -jar scripts/plantuml.jar -checkonly "$f" >/dev/null 2>&1 || { echo "lỗi cú pháp: $f"; fail=1; }
done

echo "== 4. Số liệu nghiệp vụ không kèm mã BR ở dòng đang dùng =="
python3 - <<'PY'
import re, pathlib, sys
ok = True
MA_BR = re.compile(r'\b(14 ngày|30 ngày|5\.000đ|100\.000đ|2 lần|7 ngày|12 tháng)')
for md in pathlib.Path('docs').rglob('*.md'):
    if md.name in ('bien-ban-phong-van.md','nhat-ky-nhom.md','00-tong-quan.md','README.md'): continue
    for i, line in enumerate(md.read_text(encoding='utf-8').splitlines(), 1):
        if MA_BR.search(line) and 'BR-' not in line and not re.search(r'\bQ[1-9]\b', line):
            print(f'{md}:{i}: {line.strip()[:80]}'); ok = False
sys.exit(0 if ok else 1)
PY
[ $? -ne 0 ] && fail=1

exit $fail
