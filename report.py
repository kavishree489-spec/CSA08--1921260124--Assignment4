# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""report module."""

def write_report(pct, out):
    with open(out, "w", encoding="utf-8") as f:
        for r, v in sorted(pct.items()):
            f.write("%s,%.1f\n" % (r, v))


def write_absent_report(regs, out):
    """Task 5.2 - second report."""
    with open(out, "w", encoding="utf-8") as f:
        for r in regs:
            f.write(r + "\n")
