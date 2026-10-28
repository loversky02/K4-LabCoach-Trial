"""Check the structure of a LabCoach trial submission. Does not grade.

Usage: python check_trial_submission.py <submission-repo>
Exit code 0 when every check passes, 1 otherwise.
"""
import csv
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

REQUIRED_FILES = [
    "INFO.md",
    "day18/evidence/pipeline_run.log",
    "day18/reports/ragas_report.json",
    "day18/analysis/failure_analysis.md",
    "grading/scores.csv",
    "grading/notes.md",
    "clinic/diagnosis.md",
    "clinic/feedback.md",
    "authoring/CHECKPOINT.md",
    "authoring/test_checkpoint.py",
    "authoring/RUBRIC_ROW.md",
    "REFLECTION.md",
    "AI_USAGE.md",
]
FORBIDDEN_DIRS = ["samples", "clinic-repo"]
CSV_HEADER = ["sample_id", "criterion_id", "score", "max_score", "evidence", "confidence"]
SAMPLES = {"S1", "S2", "S3"}
CRITERIA = {"m1", "m2", "m3", "m4", "m5", "pipeline", "ragas", "failure",
            "refl_mapping", "refl_debug", "refl_plan"}
CONFIDENCE = {"high", "medium", "low"}
BANNED_PHRASES = ["chỉ cần", "dễ mà"]
SECRET_PATTERN = re.compile(r"sk-[A-Za-z0-9_-]{10,}")


def check_files(root: Path) -> list[str]:
    errors = [f"thiếu file: {name}" for name in REQUIRED_FILES if not (root / name).is_file()]
    errors += [f"không được nộp thư mục: {name}/" for name in FORBIDDEN_DIRS if (root / name).exists()]
    if (root / ".env").exists() and not _gitignored(root, ".env"):
        errors.append(".env có trong repo nhưng không nằm trong .gitignore")
    return errors


def check_scores(root: Path) -> list[str]:
    path = root / "grading/scores.csv"
    if not path.is_file():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != CSV_HEADER:
            return [f"scores.csv sai header: {reader.fieldnames}"]
        rows = list(reader)
    errors = []
    if len(rows) != len(SAMPLES) * len(CRITERIA):
        errors.append(f"scores.csv có {len(rows)} dòng dữ liệu, cần {len(SAMPLES) * len(CRITERIA)}")
    seen = set()
    for i, row in enumerate(rows, start=2):
        key = (row["sample_id"], row["criterion_id"])
        if row["sample_id"] not in SAMPLES:
            errors.append(f"scores.csv:{i} sample_id không hợp lệ: {row['sample_id']}")
        if row["criterion_id"] not in CRITERIA:
            errors.append(f"scores.csv:{i} criterion_id không hợp lệ: {row['criterion_id']}")
        if key in seen:
            errors.append(f"scores.csv:{i} trùng {key}")
        seen.add(key)
        if not row["evidence"].strip():
            errors.append(f"scores.csv:{i} evidence trống")
        if row["confidence"] not in CONFIDENCE:
            errors.append(f"scores.csv:{i} confidence phải là high|medium|low")
        try:
            score, max_score = float(row["score"]), float(row["max_score"])
            if not 0 <= score <= max_score:
                errors.append(f"scores.csv:{i} score ngoài khoảng 0..max_score")
        except ValueError:
            errors.append(f"scores.csv:{i} score hoặc max_score không phải số")
    return errors


def check_feedback(root: Path) -> list[str]:
    path = root / "clinic/feedback.md"
    if not path.is_file():
        return []
    text = unicodedata.normalize("NFC", path.read_text(encoding="utf-8")).lower()
    return [f"clinic/feedback.md có cụm từ cần tránh: \"{p}\"" for p in BANNED_PHRASES if p in text]


def check_secrets(root: Path) -> list[str]:
    if not (root / ".git").exists():
        return ["không phải git repo, không kiểm tra được lịch sử commit"]
    log = subprocess.run(["git", "-C", str(root), "log", "-p", "--all"],
                         capture_output=True, text=True, errors="replace").stdout
    return ["lịch sử git có chuỗi giống API key (sk-...)"] if SECRET_PATTERN.search(log) else []


def _gitignored(root: Path, name: str) -> bool:
    result = subprocess.run(["git", "-C", str(root), "check-ignore", "-q", name])
    return result.returncode == 0


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    root = Path(sys.argv[1]).resolve()
    errors = check_files(root) + check_scores(root) + check_feedback(root) + check_secrets(root)
    for e in errors:
        print(f"FAIL  {e}")
    print("OK" if not errors else f"{len(errors)} lỗi cấu trúc")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
