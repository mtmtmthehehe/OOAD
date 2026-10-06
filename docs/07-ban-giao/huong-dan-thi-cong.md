# Hướng dẫn bàn giao thi công

Repo này chỉ gồm **tài liệu thiết kế**, chưa có ứng dụng chạy.

## Thứ tự thi công đề xuất
1. CSDL theo `docs/04-thiet-ke/erd.puml` + `data-dictionary.md`.
2. Module mượn/trả/gia hạn (UC-03, UC-04, UC-05) theo sequence diagram.
3. Tính phạt & đặt trước (UC-06, UC-07, UC-08) theo BR trong `docs/02-nghiep-vu/quy-tac-nghiep-vu.md`.
4. UC-12 cron job nhắc hạn, UC-11 báo cáo.
5. Map test case trong `docs/05-ke-hoach/ca-kiem-thu.md` sang automation test.

## Chạy kiểm tra tài liệu
```bash
bash scripts/check.sh        # truy vết BR/FR/UC/TC + cú pháp PlantUML
bash scripts/render-all.sh   # render lại toàn bộ PNG
```
