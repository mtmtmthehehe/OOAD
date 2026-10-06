# Ma trận truy vết BR → FR → UC → CLS → TC

| Mã BR | FR liên quan | UC liên quan | CLS liên quan | TC liên quan |
|-------|--------------|--------------|---------------|--------------|
| BR-01 | FR-04 | UC-03, UC-13 | CLS-03, CLS-05, CLS-13, CLS-17 | TC-06 |
| BR-02 | FR-04 | UC-03, UC-13 | CLS-03, CLS-05, CLS-17 | TC-32 |
| BR-03 | FR-05 | UC-03 | CLS-05 | TC-05, TC-24 |
| BR-04 | FR-05 | UC-03 | CLS-05 | TC-07 |
| BR-05 | FR-06 | UC-03 | CLS-01, CLS-02 | TC-08, TC-53 |
| BR-06 | FR-07 | UC-05 | CLS-05, CLS-15, CLS-19 | TC-14, TC-15, TC-40, TC-48, TC-62 |
| BR-07 | FR-08 | UC-05 | CLS-05 | TC-16, TC-39 |
| BR-08 | FR-08 | UC-05 | CLS-05 | TC-17 |
| BR-09 | FR-08 | UC-05 | CLS-08 | TC-18 |
| BR-10 | FR-10 | UC-07, UC-04, UC-14 | CLS-07 | TC-11, TC-27, TC-51 |
| BR-11 | FR-10 | UC-07, UC-04, UC-12 | CLS-05, CLS-07 | TC-25, TC-11, TC-27 |
| BR-12 | FR-11, FR-17 | UC-07, UC-08, UC-13 | CLS-03, CLS-07, CLS-24 | TC-22, TC-28, TC-29, TC-23 |
| BR-13 | FR-11, FR-17 | UC-01, UC-07, UC-08, UC-10 | CLS-03, CLS-24 | TC-22, TC-23, TC-30, TC-54, TC-69 |
| BR-14 | FR-12 | UC-04, UC-14 | CLS-02, CLS-07 | TC-13, TC-52, TC-50 |
| BR-15 | FR-12 | UC-04, UC-14 | CLS-02, CLS-07 | TC-12 |
| BR-16 | FR-03 | UC-03, UC-13 | CLS-03, CLS-04 | TC-09, TC-35 |
| BR-17 | FR-13 | UC-06 | CLS-08, CLS-16, CLS-20 | TC-19, TC-20, TC-55 |
| BR-18 | FR-14 | UC-06, UC-04, UC-12 | CLS-08, CLS-16, CLS-20 | TC-21, TC-56 |
| BR-19 | FR-15 | UC-06 | CLS-08 | TC-47 |
| BR-20 | FR-22 | UC-07, UC-08 | CLS-07 | TC-46 |
| BR-21 | FR-17 | UC-10, UC-03, UC-13 | CLS-03, CLS-04 | TC-44, TC-59, TC-60, TC-37, TC-31 |
| BR-22 | FR-16 | UC-09 | CLS-02 | TC-45, TC-33, TC-34 |
| BR-23 | FR-13 | UC-06 | CLS-08, CLS-20 | TC-42 |

## Bảng bổ sung: FR chưa gán BR (nghiệp vụ chung)

| Mã FR | UC liên quan | CLS liên quan | TC liên quan |
|-------|--------------|---------------|--------------|
| FR-01 | UC-01 | CLS-01..CLS-20 (qua đăng nhập) | TC-01, TC-02, TC-43, TC-58 |
| FR-02 | UC-02 | CLS-01, CLS-11, CLS-12, CLS-16 | TC-03, TC-04 |
| FR-09 | UC-04 | CLS-02, CLS-05, CLS-14, CLS-18 | TC-10, TC-41, TC-49 |
| FR-18 | UC-11 | CLS-05, CLS-07 | TC-26 |
| FR-19 | UC-12 | CLS-05 | TC-24, TC-25, TC-61 |
| FR-20 | UC-02 | CLS-01 | TC-36 |
| FR-21 | UC-03 | CLS-05 | TC-38 |
| FR-23 | UC-11 | CLS-05, CLS-07 | TC-57 |

## Bảng bổ sung: NFR → thiết kế / kiểm thử

| Mã NFR | Thiết kế / ADR | TC liên quan |
|--------|----------------|--------------|
| NFR-01 | Chỉ mục full-text và ISBN (data-dictionary, mục Chỉ mục) | TC-03, TC-63 |
| NFR-02 | ADR-05 (kiến trúc 3 lớp, phục vụ đồng thời) | TC-64 |
| NFR-03 | ADR-05, bảng tai_khoan (mat_khau_hash, vai_tro) | TC-65 |
| NFR-04 | ADR-10 (sao lưu CSDL) | TC-66 |
| NFR-05 | Chỉ mục truy vấn mượn/trả (data-dictionary) | TC-67 |
| NFR-06 | ADR-05 (kiến trúc 3 lớp, mở rộng chi nhánh) | — |
| NFR-07 | thiet-ke-man-hinh.md | TC-68 |
| NFR-08 | ADR-09 (cron 07:00) | TC-24, TC-25, TC-61 |
| NFR-09 | UC-01 (luồng 2b) | TC-02, TC-58 |

