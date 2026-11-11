# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""Task 6 - Alternative concept: duplicate detection with a list vs a set."""
import time


def with_list(regs):
    seen = []
    for r in regs:
        if r in seen:              # O(k) scan
            continue
        seen.append(r)


def with_set(regs):
    seen = set()
    for r in regs:
        if r in seen:              # O(1) average
            continue
        seen.add(r)


print("%-8s %-10s %s" % ("n", "List (s)", "Set (s)"))
for n in (2000, 4000, 8000):
    regs = [str(i) for i in range(n)]
    t = time.perf_counter(); with_list(regs); a = time.perf_counter() - t
    t = time.perf_counter(); with_set(regs); b = time.perf_counter() - t
    print("%-8d %-10.4f %.5f" % (n, a, b))
