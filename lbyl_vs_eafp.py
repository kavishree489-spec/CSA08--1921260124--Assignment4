# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""Task 3 - Alternative concept: LBYL (if) versus EAFP (try/except)."""
import time


def make(n, bad_ratio):
    k = int(1 / bad_ratio) if bad_ratio else 0
    return ["1,2026-10-08" if k and i % k == 0 else "1,2026-10-08,P" for i in range(n)]


def eafp(lines):
    good = bad = 0
    for line in lines:
        parts = line.split(",")
        try:
            if parts[2] == "P":
                good += 1
        except IndexError:
            bad += 1
    return good, bad


def lbyl(lines):
    good = bad = 0
    for line in lines:
        parts = line.split(",")
        if len(parts) == 3:
            if parts[2] == "P":
                good += 1
        else:
            bad += 1
    return good, bad


N = 200000
print("%-14s %-12s %s" % ("Bad lines", "try/except", "if-check"))
for label, ratio in (("0.1% (rare)", 0.001), ("50% (common)", 0.5)):
    lines = make(N, ratio)
    t = time.perf_counter(); eafp(lines); a = time.perf_counter() - t
    t = time.perf_counter(); lbyl(lines); b = time.perf_counter() - t
    print("%-14s %-12s %.4f s" % (label, "%.4f s" % a, b))
