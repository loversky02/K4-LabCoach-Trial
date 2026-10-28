# Checkpoints: Phần A (180 phút)

Mỗi CP có bốn mục: **Làm**, **Sản phẩm**, **Tự kiểm tra**, **Bí thì làm gì**.

---

## CP1. Đo lại có bằng chứng (35 phút)

**Làm**

1. Chạy lại pipeline Day18 trên repo của bạn và ghi toàn bộ output ra file:

   ```bash
   python src/pipeline.py 2>&1 | tee evidence/pipeline_run.log
   ```

2. Nếu có API key do hội đồng cấp, chạy RAGAS thật. `reports/ragas_report.json` phải có `num_questions` > 0.
3. Viết lại `analysis/failure_analysis.md`:
   - Mỗi con số phải ghi nguồn ngay cạnh nó, dạng `(evidence/pipeline_run.log:L123)` hoặc `(reports/ragas_report.json → failures[0].score)`.
   - Số nào không đo được thì ghi `chưa đo` kèm lý do. Ví dụ: "không có key, `evaluate_ragas` trả về 0".
4. Thêm mục **"Sai lệch so với bản nộp 05/10"**: liệt kê từng số trong bản cũ không có nguồn, và giải thích ngắn vì sao đã có những số đó.

**Sản phẩm:** `evidence/pipeline_run.log`, `reports/ragas_report.json`, `analysis/failure_analysis.md`

**Tự kiểm tra:** chạy lệnh dưới đây. Mọi dòng có số thực phải có trích dẫn nguồn trên cùng dòng.

```bash
grep -nE "[0-9]\.[0-9]{2}" analysis/failure_analysis.md
```

**Bí thì làm gì:** không có key thì đi theo hướng "chưa đo". Hướng này vẫn được điểm (xem RUBRIC). Tự điền số vào thì trượt cả bài.

---

## CP2. Hiệu chuẩn chấm (50 phút)

**Làm**

1. Với mỗi bài trong `samples/S1`, `samples/S2`, `samples/S3`, chấm 11 tiêu chí theo `RUBRIC.md` của Day18:
   - M1 đến M5;
   - Pipeline, RAGAS, Failure analysis;
   - 3 mục Reflection.
2. Được chạy test của từng bài trong sandbox. Không được sửa code của bài.
3. Ghi kết quả vào `grading/scores.csv` theo đúng header:

   ```text
   sample_id,criterion_id,score,max_score,evidence,confidence
   ```

   - `criterion_id` lấy trong tập `m1,m2,m3,m4,m5,pipeline,ragas,failure,refl_mapping,refl_debug,refl_plan`.
   - `evidence` là `path:line` hoặc trích một dòng log.
   - `confidence` là một trong ba giá trị `high|medium|low`.
4. Viết `grading/notes.md`, mỗi bài 3–5 dòng:
   - các ca biên khi chấm;
   - chỗ rubric mơ hồ và bạn đã quyết định thế nào;
   - có cần chuyển cho người chấm thứ hai không.

**Sản phẩm:** `grading/scores.csv` (33 dòng dữ liệu), `grading/notes.md`

**Tự kiểm tra:** chạy lệnh dưới đây. Kết quả phải là 34 (gồm 1 dòng header). Không ô `evidence` nào để trống.

```bash
python -c "import csv;r=list(csv.DictReader(open('grading/scores.csv')));print(len(r)+1)"
```

**Bí thì làm gì:** nếu một tiêu chí không phân định được, cho điểm theo bằng chứng đang có, đặt `confidence=low` và ghi lý do vào `notes.md`. Đừng bỏ trống.

---

## CP3. Debug clinic (45 phút)

Tình huống: một học viên nhắn *"em chạy hết test rồi mà kết quả RAG vẫn sai, report toàn số 0"*. Repo của học viên là `clinic-repo/`.

**Làm**

1. Tìm lỗi. Repo có đúng 3 lỗi gài sẵn. Không cần tìm lỗi khác.
2. Với mỗi lỗi, ghi vào `clinic/diagnosis.md`:
   - **Triệu chứng:** học viên thấy gì.
   - **Lệnh tái hiện:** một lệnh chạy được, kèm output quan sát được.
   - **Nguyên nhân gốc:** `file:line` và giải thích.
   - **Vì sao test hiện có không bắt được.**
3. Viết `clinic/feedback.md` gửi học viên:
   - **Feed-up:** mục tiêu của module là gì.
   - **Feed-back:** hiện tại đang sai ở đâu, dựa trên bằng chứng.
   - **Feed-forward:** bước tiếp theo.
   - Với mỗi lỗi, một **thang gợi ý 3 mức**: (1) câu hỏi định hướng, (2) chỉ ra vùng code, (3) mô tả cách sửa bằng lời.
   - Không mức nào được chứa code sửa hoàn chỉnh.
   - Không dùng từ "chỉ cần" hay "dễ mà".

**Sản phẩm:** `clinic/diagnosis.md`, `clinic/feedback.md`

**Tự kiểm tra:** chạy lại lệnh tái hiện của từng lỗi trên một bản sao đã sửa. Triệu chứng phải biến mất. Không nộp bản sao đã sửa.

**Bí thì làm gì:** bắt đầu từ triệu chứng "report toàn số 0". Lần ngược từ `reports/ragas_report.json` về `src/m4_eval.py` và `src/pipeline.py`.

---

## CP4. Soạn một checkpoint mới (35 phút)

Lab Day18 hiện cho điểm RAGAS dựa trên report mà không kiểm tra report đó có thật sự được đo hay không. Hãy soạn **một checkpoint** để đóng lỗ hổng này, hoặc một lỗ hổng khác mà bạn thấy quan trọng hơn. Nếu chọn lỗ hổng khác, giải thích lý do trong `CHECKPOINT.md`.

**Làm**

1. Viết `authoring/CHECKPOINT.md` theo labflow K4: CP / Phút / Làm / Sản phẩm / Cần hiểu / Tự kiểm tra / Đạt khi. Có một mục tiêu viết theo ABCD và dùng động từ Bloom đo được.
2. Viết `authoring/test_checkpoint.py`: một test pytest **xác định** (không gọi mạng, không gọi LLM) kiểm tra đúng điều kiện "Đạt khi". Test đọc đường dẫn repo cần kiểm tra từ biến môi trường `TRIAL_REPO`, vì hội đồng sẽ chạy cùng một file test trên nhiều repo.
3. Viết `authoring/RUBRIC_ROW.md`: một dòng rubric gồm điểm, các mức điểm và bằng chứng. Ghi rõ dòng này **thay** hay **bổ sung** cho dòng #7 hiện tại, và có trừ điểm trùng hay không.

**Sản phẩm:** 3 file trong `authoring/`

**Tự kiểm tra:** test phải pass trên repo của bạn sau CP1 và fail trên `clinic-repo/`:

```bash
TRIAL_REPO=<đường-dẫn-repo> python -m pytest authoring/test_checkpoint.py -q
```

Nếu CP1 đi hướng "chưa đo", report của bạn toàn số 0 nên test sẽ fail trên repo của bạn. Khi đó, để tự kiểm tra, tạo một report hợp lệ trong thư mục tạm ngoài repo và chạy test trên thư mục đó. Report tạm này chỉ dùng để thử test: không nộp, không trích số từ nó vào `failure_analysis.md`.

**Bí thì làm gì:** một điều kiện tối thiểu đủ dùng là `num_questions` > 0, có ít nhất một giá trị trong `aggregate` khác 0, và `len(failures)` không vượt quá `num_questions`. Đọc `save_report` trong `src/m4_eval.py` để biết report có những trường nào.

---

## CP5. Tổng kết (15 phút)

- `REFLECTION.md`, tối đa 250 chữ:
  - CP nào khó nhất và vì sao;
  - thời gian thực tế so với dự kiến cho từng CP;
  - một điều bạn sẽ làm khác khi coach học viên ở Day18.
- `AI_USAGE.md`: dùng công cụ AI nào, ở CP nào, để làm gì, và bạn đã kiểm tra lại đầu ra ra sao.
