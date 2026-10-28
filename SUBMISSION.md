# Nộp bài

## Repo

- Tạo repo **private** mới, đặt tên `K4-LabCoach-Trial-HoVaTen-MSSV`. Mời hội đồng (tài khoản do N1 cung cấp) với quyền đọc.
- Không fork `samples/` hay `clinic-repo/`, và không commit hai thư mục này vào repo nộp.
- Không commit bản sao `clinic-repo/` đã sửa.

## Cấu trúc

```text
K4-LabCoach-Trial-HoVaTen-MSSV/
├── INFO.md                 # họ tên, MSSV, giờ bắt đầu và kết thúc từng CP
├── day18/                  # repo Day18 của bạn sau CP1 (hoặc git submodule trỏ tới commit mới)
│   ├── evidence/pipeline_run.log
│   ├── reports/ragas_report.json
│   └── analysis/failure_analysis.md
├── grading/
│   ├── scores.csv
│   └── notes.md
├── clinic/
│   ├── diagnosis.md
│   └── feedback.md
├── authoring/
│   ├── CHECKPOINT.md
│   ├── test_checkpoint.py
│   └── RUBRIC_ROW.md
├── REFLECTION.md
└── AI_USAGE.md
```

Trước khi nộp, tự chạy:

```bash
python check_trial_submission.py <đường-dẫn-repo>
```

Script này do hội đồng gửi kèm đề. Nó chỉ kiểm tra cấu trúc, không chấm điểm.

## Hạn nộp

- **48 giờ** kể từ lúc nhận đề, theo giờ Asia/Ho_Chi_Minh. Ghi commit SHA cuối cùng vào form nộp.
- Không force-push sau hạn. Nếu cần bổ sung, tạo commit mới và ghi lý do trong `INFO.md`. Hội đồng chấm theo SHA trong form.
- Lịch Phần B được hẹn sau khi hội đồng chấm xong Phần A, thường trong vòng 3 ngày làm việc.
