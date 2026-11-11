# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""Task 2.4 - trace of one small file containing a damaged line."""
from attendance_monthly import process_month
import shutil, tempfile, pathlib

tmp = pathlib.Path(tempfile.mkdtemp())
shutil.copy("data/2026-10-08.txt", tmp)
present, total, damaged = process_month(tmp)
print({r: 100 * present[r] / total[r] for r in total})
print(damaged)
shutil.rmtree(tmp)
