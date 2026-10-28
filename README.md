# K4 LabCoach Trial — Coaching Lab Day18 Production RAG (Track 3)

Bài thử năng lực cho ứng viên labcoach. Làm **cá nhân**. Gồm hai phần:

- **Phần A, làm ở nhà:** 180 phút làm việc, nộp trong vòng 48 giờ kể từ lúc nhận đề.
- **Phần B, trực tiếp:** 30 phút với hội đồng N1.

Tổng **100 điểm**, không có bonus.

Bài này không kiểm tra lại việc bạn làm được lab Day18 hay không. Bài kiểm tra những việc một labcoach làm hằng ngày:

- chấm bài đúng rubric và có bằng chứng;
- tìm lỗi trong repo của học viên;
- gợi ý mà không đưa lời giải;
- soạn thêm một checkpoint cho lab;
- dạy một đoạn ngắn;
- báo cáo số liệu trung thực.

## Mục tiêu (đo được)

Sau bài này, ứng viên chứng minh được 6 năng lực:

| # | Năng lực | Điều kiện | Mức đạt |
|---|---|---|---|
| O1 | **Chấm** 3 bài Day18 đã ẩn danh theo `RUBRIC.md` của Day18 | Không dùng AI để ra điểm. Có repo và đầu ra của grader | Tổng điểm mỗi bài lệch không quá 5 điểm (trên thang 100) so với khóa chấm. Điểm từng tiêu chí đều có trích dẫn `path:line` hoặc log |
| O2 | **Chẩn đoán** lỗi trong một repo học viên có lỗi gài sẵn | Được chạy code trong sandbox | Tìm được ít nhất 2/3 lỗi. Mỗi lỗi có lệnh tái hiện và nguyên nhân gốc |
| O3 | **Viết phản hồi** cho học viên đó | Theo mẫu trong `CHECKPOINTS.md` | Mỗi lỗi có thang gợi ý 3 mức. Không mức nào chứa code sửa hoàn chỉnh |
| O4 | **Soạn** một checkpoint mới cho Day18 theo labflow K4 | Kèm đúng 1 test tự động | Test pass trên bài đúng và fail trên repo lỗi. Mục tiêu, hoạt động và cách chấm khớp nhau |
| O5 | **Báo cáo** số đo RAGAS trên repo Day18 của chính mình | Chỉ dùng số lấy từ lần chạy có log | Mỗi con số truy được về file và dòng log. Số nào chưa đo thì ghi rõ "chưa đo" |
| O6 | **Dạy** 8 phút một đoạn Day18 bằng live coding | Trực tiếp, có 1 câu hỏi tình huống | Dưới 3 mục "cần cải thiện" theo rubric teaching demo |

## Đọc theo thứ tự

| File | Nội dung |
|---|---|
| `README.md` | Tổng quan (file này) |
| `CHECKPOINTS.md` | Các bước, thời gian, sản phẩm, cách tự kiểm tra, điều kiện đạt |
| `RUBRIC.md` | Thang điểm, điều kiện trượt, quy tắc ra quyết định |
| `RULES.md` | Liêm chính, mức dùng AI, secret, dữ liệu học viên |
| `SUBMISSION.md` | Cấu trúc repo nộp, tên repo, hạn nộp |
| `check_trial_submission.py` | Script tự kiểm tra cấu trúc repo nộp trước khi nộp |

## Chuẩn bị (không tính giờ)

1. Nhận từ hội đồng ba thứ: `samples/` (3 bài ẩn danh), `clinic-repo/` (repo có lỗi gài sẵn), và cách lấy API key có giới hạn chi phí, nếu hội đồng cấp.
2. Dùng repo Day18 Track3B của chính bạn với Python 3.11 và `pip install -r requirements.txt`.
3. Chạy smoke test. Kết quả mong đợi là 37 passed:

   ```bash
   python -m pytest tests -q
   ```

   Nếu lỗi môi trường, báo hội đồng **trước khi** bắt đầu tính giờ.

## Các bước (Phần A: 180 phút)

| CP | Phút | Sản phẩm | Đạt khi |
|---|---:|---|---|
| CP1 Đo lại có bằng chứng | 35 | `evidence/` + `reports/ragas_report.json` + `analysis/failure_analysis.md` đã sửa | Mọi số trong `failure_analysis.md` có nguồn. Không có số nào tự viết ra |
| CP2 Hiệu chuẩn chấm | 50 | `grading/scores.csv` + `grading/notes.md` | Đủ 3 bài × 11 tiêu chí, mỗi điểm có bằng chứng |
| CP3 Debug clinic | 45 | `clinic/diagnosis.md` + `clinic/feedback.md` | Mỗi lỗi có lệnh tái hiện, nguyên nhân gốc, gợi ý 3 mức |
| CP4 Soạn checkpoint | 35 | `authoring/CHECKPOINT.md` + `authoring/test_checkpoint.py` + `authoring/RUBRIC_ROW.md` | Test pass trên bài đúng, fail trên `clinic-repo/` |
| CP5 Tổng kết | 15 | `REFLECTION.md` + `AI_USAGE.md` | Có cả hai file và đủ các mục |

Nên chừa khoảng 20% thời gian dự phòng. Nếu một CP vượt quá 1,5 lần số phút dự kiến, ghi lại trong `REFLECTION.md` rồi làm tiếp CP sau.

## Phần B: trực tiếp (30 phút)

| Phút | Hoạt động |
|---:|---|
| 0–8 | Dạy một đoạn Day18 (ứng viên tự chọn M2 RRF hoặc M3 rerank). Gõ code trực tiếp, không dán sẵn |
| 8–13 | Hội đồng đóng vai học viên hỏi một câu tình huống. Ứng viên trả lời như khi coach |
| 13–28 | Phỏng vấn có cấu trúc: câu hỏi cố định, chấm theo thang có mô tả hành vi |
| 28–30 | Ứng viên tự nhận xét phần dạy của mình |

Xem cách tính điểm và quy tắc ra quyết định trong `RUBRIC.md`.
