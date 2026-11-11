# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""Task 1.2 - repaired mess-bill totaller."""
from decimal import Decimal, InvalidOperation
import logging

logging.basicConfig(filename="mess_errors.log", level=logging.WARNING,
                    format="%(message)s")


def total_bills(filename):
    """Return (total, report_lines, rejected) for a mess-bill file."""
    total = Decimal("0")
    report, rejected = [], []
    try:
        with open(filename, encoding="utf-8") as f:       # always closed
            for line_no, line in enumerate(f, start=1):   # one line at a time
                line = line.strip()
                if not line:                              # blank last line
                    continue
                parts = line.split(",")
                try:
                    if len(parts) != 3:
                        raise ValueError("expected 3 fields, found %d" % len(parts))
                    try:
                        amount = Decimal(parts[2].strip())    # exact paise
                    except InvalidOperation:
                        raise ValueError("invalid amount %r" % parts[2].strip())
                except ValueError as err:
                    rejected.append((line_no, line, str(err)))
                    logging.warning("line %d: %r (%s)", line_no, line, err)
                    continue
                total += amount
                report.append("%s %s" % (parts[1].strip(), amount))
    except FileNotFoundError:
        print("File not found:", filename)
    except PermissionError:
        print("No permission to read:", filename)
    return total, report, rejected


if __name__ == "__main__":
    with open("mess_oct.txt", "w", encoding="utf-8") as f:
        f.write("192311001,Arun,1250.50\n192311002,Bala,1300\n"
                "192311003,Chitra\n192311004,Devi,abc\n192311005,Eswar,980.25\n\n")
    total, report, rejected = total_bills("mess_oct.txt")
    print("\n".join(report))
    print("Total", total)
    print("Rejected:", rejected)
    print(total_bills("nofile.txt"))
