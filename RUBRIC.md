# Rubric: K4 LabCoach Trial

**Tổng: 100 điểm.** Phần A làm ở nhà, 80 điểm. Phần B trực tiếp, 20 điểm. Không có bonus.

Ứng viên được xem rubric này trước khi làm bài. Khóa chấm CP2 và danh sách lỗi gài ở CP3 thì không công bố.

## Điều kiện trượt (áp dụng bất kể tổng điểm)

| # | Điều kiện | Lý do |
|---|---|---|
| G1 | Có số liệu hoặc bằng chứng bịa ra: số không truy được về file hay log mà vẫn trình bày như số đo thật, hoặc trích `path:line` không tồn tại | Labcoach dạy học viên đánh giá có bằng chứng. Đây là tiêu chí cốt lõi của vai trò |
| G2 | Commit API key, token hoặc dữ liệu định danh học viên lên repo | An toàn dữ liệu |
| G3 | Sửa code trong `samples/`, tìm cách xem khóa chấm, hoặc nhờ người khác làm | Liêm chính |
| G4 | Ở Phần B, không giải thích được một phần trong bài mình đã nộp | Giống luật "không giải thích được phần mình làm thì 0 điểm" của Hackathon K4 |

## Phần A (80 điểm)

### CP1. Đo lại có bằng chứng (15 điểm)

| Mức | Điểm | Mô tả |
|---|---:|---|
| Đo thật | 15 | `num_questions` > 0. Mọi số trong `failure_analysis.md` trích được nguồn. Mục "Sai lệch so với bản nộp 05/10" liệt kê đủ các số cũ không có nguồn |
| Trung thực, chưa đo | 9 | Không có key. Các số ghi `chưa đo` và chỉ đúng nguyên nhân report bằng 0. Mục "Sai lệch" đầy đủ |
| Một phần | 4 | Có trích nguồn nhưng còn số thiếu nguồn, ghi là ước lượng chứ không phải số đo. Hoặc mục "Sai lệch" thiếu |
| Không có | 0 | Thiếu sản phẩm |

### CP2. Hiệu chuẩn chấm (25 điểm)

| Thành phần | Điểm | Cách tính |
|---|---:|---|
| Độ lệch tổng điểm | 15 | Mỗi bài được 5 điểm nếu lệch không quá 5 điểm so với khóa, 3 điểm nếu lệch không quá 10, còn lại 0. Có 3 bài |
| Khớp từng tiêu chí | 6 | Tỷ lệ khớp đúng trên 33 ô. Từ 85% trở lên được 6. Từ 70% trở lên được 4. Dưới 70% được 1 |
| Chất lượng bằng chứng | 4 | Hội đồng kiểm tra ngẫu nhiên 5 dòng. Cả 5 dòng đúng được 4. Đúng 3 hoặc 4 dòng được 2. Dưới 3 dòng được 0 |

Ngưỡng 5 điểm lấy theo cổng hiệu chuẩn của repo chấm (`docs/lab-package-standard.md`). Ngưỡng 70% khớp là mức hội đồng tự đặt cho vòng thử, vì ứng viên chưa được huấn luyện chấm. Nhiều tài liệu về độ tin cậy giữa người chấm lấy 80% làm mức tối thiểu cho người chấm đã được huấn luyện (McHugh 2012), nên phải từ 85% mới được điểm tối đa.

### CP3. Debug clinic (20 điểm)

| Thành phần | Điểm | Mô tả |
|---|---:|---|
| Chẩn đoán | 12 | Mỗi lỗi 4 điểm. Lệnh tái hiện chạy được: 1. Nguyên nhân gốc đúng `file:line`: 2. Giải thích vì sao test không bắt được: 1 |
| Thang gợi ý | 3 | Có đủ 3 mức cho mỗi lỗi, mức sau cụ thể hơn mức trước. Có code sửa hoàn chỉnh ở bất kỳ mức nào thì 0 |
| Cấu trúc phản hồi | 3 | Có đủ feed-up, feed-back, feed-forward, và mỗi nhận xét dựa trên bằng chứng |
| Ngôn ngữ | 2 | Tôn trọng, không quy lỗi cho học viên, không dùng "chỉ cần" hay "dễ mà" |

### CP4. Soạn checkpoint (15 điểm)

| Thành phần | Điểm | Mô tả |
|---|---:|---|
| Test hoạt động | 6 | Hội đồng tự chạy. Pass trên bài đúng: 3. Fail trên `clinic-repo/`: 3. Gọi mạng, gọi LLM hoặc kết quả không ổn định thì 0 |
| Thẳng hàng | 5 | Mục tiêu viết theo ABCD và dùng động từ Bloom đo được. Hoạt động, test và dòng rubric cùng đo đúng động từ đó |
| Dòng rubric | 4 | Các mức mô tả được bằng quan sát. Ghi rõ thay hay bổ sung cho #7. Không trừ điểm hai lần cho cùng một lỗi |

### CP5. Tổng kết (5 điểm)

Có `REFLECTION.md` đủ 3 ý: 3 điểm. Có `AI_USAGE.md` ghi đủ công cụ, CP, mục đích và cách kiểm tra lại: 2 điểm.

## Phần B (20 điểm)

### Dạy 8 phút + câu hỏi tình huống (12 điểm)

Phỏng theo rubric teaching demo của The Carpentries. Bắt đầu từ 12 điểm, mỗi mục "cần cải thiện" trừ 2 điểm.

| Nhóm | Làm tốt | Cần cải thiện |
|---|---|---|
| Nội dung | Đặt vấn đề trước khi vào code, nói rõ vì sao học viên cần. Nội dung đúng | Vào code ngay, không có bối cảnh. Sai kiến thức mà không tự sửa |
| Trình bày | Gõ code trực tiếp và giải thích từng bước. Chữ đủ to. Tốc độ vừa phải. Biến lỗi của mình thành lúc dạy | Dán code sẵn. Gõ mà không giải thích. Lờ lỗi của mình đi. Dùng từ "chỉ cần" hay "dễ" |
| Trả lời học viên | Hỏi lại để tìm hiểu học viên đang hiểu đến đâu. Gợi ý theo bậc | Đưa luôn đáp án. Trả lời sai mà không kiểm chứng |

Có từ 3 mục "cần cải thiện" trở lên thì phải dạy lại, không xét đạt ở vòng này.

### Phỏng vấn có cấu trúc (8 điểm)

Hỏi 4 câu cố định, mỗi câu từ 0 đến 2 điểm theo thang có mô tả hành vi. Hội đồng giữ thang chi tiết.

## Quy tắc ra quyết định

| Kết quả | Điều kiện |
|---|---|
| **Đạt** | Tổng từ 75 trở lên. Không chạm G1–G4. CP2 từ 18/25 trở lên. Không phải dạy lại |
| **Đạt có điều kiện** | Tổng từ 60 đến 74. Hoặc CP1 ở mức "trung thực, chưa đo". Hoặc CP3 dưới 12. Khi đó: dự 2 buổi theo coach chính trước khi nhận việc, và điểm chấm trong 2 lab đầu phải có người chấm lại |
| **Không đạt** | Chạm G1–G4. Hoặc tổng dưới 60. Hoặc CP2 dưới 13/25. Hoặc phải dạy lại mà lần dạy lại vẫn không đạt |

## Đối chiếu với chuẩn quốc tế (Advance HE PSF 2023, mức D1)

| Chiều của PSF 2023 | Thể hiện ở đâu trong bài này |
|---|---|
| A1: thiết kế và lên kế hoạch hoạt động học | CP4 |
| A2: dạy và hỗ trợ việc học | Phần B, dạy 8 phút |
| A3: đánh giá và phản hồi | CP2, CP3 phản hồi |
| A4: hỗ trợ và hướng dẫn người học | CP3 thang gợi ý, câu hỏi tình huống |
| K1–K3: người học học thế nào; cách dạy; đánh giá có phản biện | CP3, CP4, CP5 |
| V1: tôn trọng từng người học | CP3 ngôn ngữ, Phần B |
| V3: dựa trên bằng chứng | CP1, G1 |

Mức D1 yêu cầu có bằng chứng cho V1, V3, K1–K3 và ít nhất 2 trong 5 Area of Activity. Bài này phủ 4 trên 5.
