# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""Task 5(b) - library module (no main block)."""
from datetime import date, timedelta


def read_records(path):
    """Read 'register,date,status' lines into lists."""
    with open(path, encoding="utf-8") as f:
        return [l.strip().split(",") for l in f if l.strip()]


def percentages(records):
    total, present = {}, {}
    for reg, date, st in records:
        total[reg] = total.get(reg, 0) + 1
        present[reg] = present.get(reg, 0) + (st == "P")
    return {r: 100 * present[r] / total[r] for r in total}


def absent_three_days(records):
    """Task 5.2 - register numbers absent on three consecutive dates."""
    days = {}
    for reg, d, st in records:
        days.setdefault(reg, []).append((date.fromisoformat(d), st))
    result = []
    for reg, lst in sorted(days.items()):
        lst.sort()
        run, prev = 0, None
        for d, st in lst:
            if st == "A":
                run = run + 1 if (prev is not None and run > 0
                                  and d - prev == timedelta(days=1)) else 1
            else:
                run = 0
            prev = d
            if run >= 3:
                result.append(reg)
                break
    return result


def write_report(pct, out):
    with open(out, "w", encoding="utf-8") as f:
        for r, v in sorted(pct.items()):
            f.write("%s,%.1f\n" % (r, v))


def write_absent_report(regs, out):
    """Task 5.2 - second report."""
    with open(out, "w", encoding="utf-8") as f:
        for r in regs:
            f.write(r + "\n")
