# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""Task 2 - monthly attendance from daily biometric files.

Usage:  python attendance_monthly.py [folder]      (default folder: data)
Outputs: below75.txt  and  damaged.log
"""
import sys
from collections import defaultdict
from pathlib import Path


def process_month(folder):
    present = defaultdict(int)
    total = defaultdict(int)
    damaged = []                                   # (file name, line no, reason/text)
    folder = Path(folder)
    if not folder.is_dir():
        raise FileNotFoundError("folder not found: %s" % folder)

    for path in sorted(folder.glob("*.txt")):
        try:
            with open(path, encoding="utf-8") as f:
                for line_no, line in enumerate(f, start=1):
                    text = line.strip()
                    if not text:
                        continue
                    parts = text.split(",")
                    if len(parts) != 3 or parts[2] not in ("P", "A"):
                        damaged.append((path.name, line_no, text))
                        continue
                    total[parts[0]] += 1
                    if parts[2] == "P":
                        present[parts[0]] += 1
        except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
            damaged.append((path.name, 0, type(e).__name__))
    return present, total, damaged


def write_reports(present, total, damaged, below_file="below75.txt",
                  log_file="damaged.log"):
    pct = {reg: 100 * present[reg] / total[reg] for reg in total}   # total[reg] >= 1
    with open(below_file, "w", encoding="utf-8") as f:
        for reg, value in sorted(pct.items()):
            if value < 75:
                f.write("%s,%.1f\n" % (reg, value))
    with open(log_file, "w", encoding="utf-8") as f:
        for name, no, text in damaged:
            f.write("%s | line %d | %s\n" % (name, no, text))
    return pct


if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "data"
    try:
        present, total, damaged = process_month(folder)
    except FileNotFoundError as e:
        print("Cannot continue:", e)
        sys.exit(1)
    pct = write_reports(present, total, damaged)
    print("Percentages:", pct)
    print("Below 75%:", sorted(r for r, v in pct.items() if v < 75))
    print("Damaged:", damaged)
