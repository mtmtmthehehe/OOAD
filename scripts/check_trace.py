#!/usr/bin/env python3
"""Kiểm tra truy vết BR -> FR -> UC -> CLS -> TC giữa các bảng."""
import re, sys, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
docs = ROOT / 'docs'

def rows(path, prefix):
    out = []
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith('| ' + prefix):
            out.append([c.strip() for c in line.strip().strip('|').split('|')])
    return out

def ids(s): return set(re.findall(r'(?:BR|FR|NFR|UC|CLS|TC)-\d+', s))

# Danh sách chuẩn từ nguồn khai báo
brs = {r[0] for r in rows(docs/'02-nghiep-vu/quy-tac-nghiep-vu.md', 'BR-')}
frs = {r[0]: r for r in rows(docs/'01-yeu-cau/yeu-cau-chuc-nang.md', 'FR-')}
nfrs = {r[0] for r in rows(docs/'01-yeu-cau/yeu-cau-phi-chuc-nang.md', 'NFR-')}
ucs = {r[0] for r in rows(docs/'01-yeu-cau/mo-hinh-use-case.md', 'UC-')}
classes = {r[0] for r in rows(docs/'04-thiet-ke/danh-sach-lop.md', 'CLS-')}
tcs = {r[0]: r for r in rows(docs/'05-ke-hoach/ca-kiem-thu.md', 'TC-')}

# FR gốc theo file FR: cột 4 là "BR gốc"
fr_goc = {}
for r in rows(docs/'01-yeu-cau/yeu-cau-chuc-nang.md', 'FR-'):
    fr_goc[r[0]] = set() if r[3] in ('—','-','') else ids(r[3])

errors = []
def err(msg): errors.append(msg)

# Ma trận
matrix_rows = rows(docs/'06-truy-vet/ma-tran-truy-vet.md', 'BR-')
# Bỏ qua nếu file dùng bảng phụ FR — chỉ xử lý hàng bắt đầu bằng BR-
BR_of_TC, FRs_of_BR, UCs_of_BR, CLSs_of_BR, TCs_of_BR = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
for r in matrix_rows:
    br, frs_c, ucs_c, clss_c, tcs_c = r[0], r[1], r[2], r[3], r[4]
    if br not in brs: err(f'Ma trận: {br} không có trong quy-tac')
    FRs_of_BR[br] |= ids(frs_c); UCs_of_BR[br] |= ids(ucs_c); CLSs_of_BR[br] |= ids(clss_c); TCs_of_BR[br] |= ids(tcs_c)
    for t in ids(tcs_c): BR_of_TC[t].add(br)

fr_tab_rows = [r for r in rows(docs/'06-truy-vet/ma-tran-truy-vet.md', 'FR-')]
fr_tab_ids = {r[0] for r in fr_tab_rows}

matrix_fr_has_br = collections.defaultdict(set)
for br, frs_c in FRs_of_BR.items():
    for f in frs_c: matrix_fr_has_br[f].add(br)


# (1) Mỗi TC trích BR thì hàng BR trong ma trận phải liệt kê TC; mỗi FR của TC phải nằm trong cột FR của các hàng BR đó
for tc, r in tcs.items():
    cited = ids(r[2])
    cited_brs = {x for x in cited if x.startswith('BR-')}
    cited_frs = {x for x in cited if x.startswith('FR-')}
    for b in cited_brs:
        if tc not in TCs_of_BR.get(b, set()):
            err(f'{tc} trích {b} nhưng ma trận hàng {b} không có {tc}')
    for f in cited_frs:
        if f not in frs: err(f'{tc} trích {f} nhưng {f} không tồn tại trong FR')
        for b in cited_brs or set():
            if f not in FRs_of_BR.get(b, set()):
                err(f'{tc} trích {f} {b} nhưng ma trận hàng {b} không có {f}')
        if not cited_brs and f not in matrix_fr_has_br and f not in fr_tab_ids:
            err(f'{tc} trích {f} nhưng {f} không xuất hiện trong ma trận (BR-table lẫn bảng phụ)')

# (2) FR↔BR hai chiều giữa FR file và ma trận
for f, goc in fr_goc.items():
    in_BR = matrix_fr_has_br.get(f, set())
    in_FR_tab = f in fr_tab_ids
    if goc:
        if goc != in_BR or in_FR_tab: err(f'{f}: BR gốc FR file = {sorted(goc)} nhưng ma trận gắn BR={sorted(in_BR)}, trong bảng phụ={in_FR_tab}')
    else:
        if in_BR or not in_FR_tab: err(f'{f}: FR không có BR gốc nhưng ở BR-table={sorted(in_BR)}, trong bảng phụ={in_FR_tab}')

# (5) Mọi TC phải xuất hiện ở ít nhất một hàng (BR-table hoặc FR-table) của ma trận
fr_tab_rows = [r for r in rows(docs/'06-truy-vet/ma-tran-truy-vet.md', 'FR-')]
fr_tab_ids = {r[0] for r in fr_tab_rows}
fr_tab_tcs = set()
for r in fr_tab_rows:
    fr_tab_tcs |= ids(r[3])
all_matrix_tcs = (set().union(*TCs_of_BR.values()) if TCs_of_BR else set()) | fr_tab_tcs

# (3) FR↔BR hai chiều giữa FR file và ma trận (chỉ áp dụng hàng BR trong ma trận)
matrix_fr_has_br = collections.defaultdict(set)
for br, frs_c in FRs_of_BR.items():
    for f in frs_c: matrix_fr_has_br[f].add(br)
for f, goc in fr_goc.items():
    in_BR = matrix_fr_has_br.get(f, set())
    in_FR_tab = f in fr_tab_ids
    if goc:
        if goc != in_BR or in_FR_tab: err(f'{f}: BR gốc FR file = {sorted(goc)} nhưng ma trận gắn BR={sorted(in_BR)}, trong bảng phụ={in_FR_tab}')
    else:
        if in_BR or not in_FR_tab: err(f'{f}: FR không có BR gốc nhưng ở BR-table={sorted(in_BR)}, trong bảng phụ={in_FR_tab}')

# (4) Tồn tại của BR/UC/CLS/TC được nhắc tới trong ma trận
for br in FRs_of_BR: 
    pass
for br, ucs_c in UCs_of_BR.items():
    for u in ucs_c: 
        if u not in ucs: err(f'Ma trận hàng {br}: {u} không tồn tại')
for br, clss_c in CLSs_of_BR.items():
    for c in clss_c:
        if c not in classes: err(f'Ma trận hàng {br}: {c} không tồn tại')
for t, brs_c in BR_of_TC.items():
    if t not in tcs: err(f'Ma trận nhắc {t} nhưng không tồn tại trong ca kiểm thử')

# (5b) Bảng NFR trong ma trận: mỗi NFR có thiết kế/ADR hoặc TC; TC tồn tại và được ghi nhận
nfr_rows = rows(docs/'06-truy-vet/ma-tran-truy-vet.md', 'NFR-')
nfr_seen = {r[0] for r in nfr_rows}
for n in nfrs:
    if n not in nfr_seen: err(f'{n} không có trong bảng NFR của ma trận')
for r in nfr_rows:
    if r[0] not in nfrs: err(f'Ma trận NFR: {r[0]} không tồn tại')
    if (r[1] in ('—','-','')) and (r[2] in ('—','-','')): err(f'{r[0]}: thiếu cả thiết kế/ADR lẫn TC')
    for tcid in ids(r[2]):
        if tcid not in tcs: err(f'Ma trận NFR {r[0]}: {tcid} không tồn tại')
        all_matrix_tcs.add(tcid)
for tc, r in tcs.items():
    for n in {x for x in ids(r[2]) if x.startswith('NFR-')}:
        if tc not in set().union(*[ids(x[2]) for x in nfr_rows if x[0]==n] or [set()]): err(f'{tc} trích {n} nhưng bảng NFR không liệt kê {tc}')

for tc in tcs:
    if tc not in all_matrix_tcs: err(f'{tc} không xuất hiện trong ma trận')

# (6) Số lượng đếm khớp tài liệu tổng quan
tongquan = (docs/'00-tong-quan.md').read_text(encoding='utf-8')
for label, actual in [('BR', len(brs)), ('FR', len(frs)), ('NFR', len(nfrs)), ('UC', len(ucs)), ('CLS', len(classes)), ('TC', len(tcs))]:
    m = re.search(rf'(\d+) (?:luật nghiệp vụ \(BR|yêu cầu chức năng \(FR|yêu cầu phi chức năng \(NFR|Use Case \(UC|lớp|test case \(TC)', tongquan)
# simpler: check từng số liệu xuất hiện đúng
expect = {'BR': len(brs), 'FR': len(frs), 'NFR': len(nfrs), 'UC': len(ucs), 'TC': len(tcs)}
for k, v in expect.items():
    if not re.search(rf'\b{v}\s+(?:luật nghiệp vụ|yêu cầu chức năng|yêu cầu phi chức năng|Use Case|test case)', tongquan):
        err(f'00-tong-quan.md: số lượng {k} ({v}) không khớp')

# (7) Link markdown nội bộ tồn tại
for md in docs.rglob('*.md'):
    for m in re.finditer(r'\]\(([^)#]+)(#[^)]*)?\)', md.read_text(encoding='utf-8')):
        target = m.group(1)
        if re.match(r'^[a-z]+://', target) or target.startswith('mailto:'): continue
        if not (md.parent / target).resolve().exists():
            err(f'{md.relative_to(ROOT)}: link hỏng → {target}')

# (8) PNG phải được cập nhật cùng PML (so theo git working tree; mtime không tin cậy sau khi clone)
import subprocess
try:
    changed = set(subprocess.run(['git','status','--porcelain'],cwd=ROOT,capture_output=True,text=True,check=True).stdout.split('\n'))
    changed = {l[3:].strip() for l in changed if len(l) > 3}
except Exception:
    changed = set()
for pml in docs.rglob('*.puml'):
    png = pml.with_suffix('.png')
    rp, rn = str(pml.relative_to(ROOT)), str(png.relative_to(ROOT))
    if png.exists() and rp in changed and rn not in changed:
        err(f'{rn} chưa render lại sau khi sửa {pml.name} — chạy render-all.sh')

if errors:
    print('\n'.join(errors)); sys.exit(1)
print('Truy vết OK: BR', len(brs), 'FR', len(frs), 'NFR', len(nfrs), 'UC', len(ucs), 'CLS', len(classes), 'TC', len(tcs))
