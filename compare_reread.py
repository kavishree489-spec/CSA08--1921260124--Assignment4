# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""Task 2 - Alternative concept: re-read all files per student vs single pass."""
import os
import tempfile
import time
from collections import defaultdict

S, F, L = 50, 10, 200
folder = tempfile.mkdtemp()
students = ["%d" % (1000 + i) for i in range(S)]
files = []
for k in range(F):
    p = os.path.join(folder, "day%02d.txt" % k)
    with open(p, "w") as f:
        for i in range(L):
            f.write("%s,2026-10-%02d,%s\n" % (students[i % S], k + 1, "PA"[i % 3 == 0]))
    files.append(p)


def reread():
    result = {}
    for s in students:                       # s
        p_cnt = t_cnt = 0
        for path in files:                   # f
            with open(path) as fh:
                for line in fh:              # l
                    reg, _, st = line.strip().split(",")
                    if reg == s:
                        t_cnt += 1
                        p_cnt += st == "P"
        result[s] = 100 * p_cnt / t_cnt
    return result


def single_pass():
    present, total = defaultdict(int), defaultdict(int)
    for path in files:                       # f
        with open(path) as fh:
            for line in fh:                  # l
                reg, _, st = line.strip().split(",")
                total[reg] += 1
                present[reg] += st == "P"
    return {r: 100 * present[r] / total[r] for r in total}


t = time.perf_counter(); a = reread(); t1 = time.perf_counter() - t
t = time.perf_counter(); b = single_pass(); t2 = time.perf_counter() - t
print("same result:", a == b)
print("re-read per student: %.4f s   O(s*f*l)" % t1)
print("single pass        : %.4f s   O(f*l)" % t2)
print("speed-up: about %.0f times" % (t1 / t2))
