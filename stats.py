# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""stats module."""
from datetime import date, timedelta


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
