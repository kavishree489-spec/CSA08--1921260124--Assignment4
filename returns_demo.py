# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""Task 4 - library returns log: buggy version, evidence test, repaired version."""
import logging
import os

for name in ("bad.log", "returns.log", "errors.log"):
    if os.path.exists(name):
        os.remove(name)


# ---------------- original (buggy) ----------------
def save_returns_bad(books):
    log = open("bad.log", "w")             # "w" truncates: earlier days lost
    for b in books:
        log.write(b)                       # no newline: books joined together
    log.close()                            # skipped if write() fails


def process_bad(day_file):
    try:
        books = open(day_file).read().split("\n")      # never closed explicitly
        save_returns_bad(books)
    except FileNotFoundError:
        print("missing")                   # nothing saved to a file


# ---------------- repaired ----------------
logging.basicConfig(filename="errors.log", level=logging.ERROR)


def save_returns(books, log_name="returns.log"):
    with open(log_name, "a", encoding="utf-8") as log:     # append + with
        for b in books:
            log.write(b + "\n")


def process(day_file, log_name="returns.log"):
    try:
        with open(day_file, encoding="utf-8") as f:
            books = [l.strip() for l in f if l.strip()]
        save_returns(books, log_name)
    except FileNotFoundError:
        logging.error("missing file: %s", day_file)
    except OSError as e:
        logging.error("cannot process %s: %s", day_file, e)


# ---------------- evidence test: three days ----------------
days = [["Book A", "Book B"], ["Book C"], ["Book D", "Book E"]]
for i, names in enumerate(days, 1):
    with open("day%d.txt" % i, "w") as f:
        f.write("\n".join(names) + "\n")

print("--- BAD version ---")
for i in (1, 2, 3):
    process_bad("day%d.txt" % i)
print(repr(open("bad.log").read()))

print("--- FIXED version ---")
for i in (1, 2, 3):
    process("day%d.txt" % i)
process("day9.txt")                        # missing day -> recorded in errors.log
print(open("returns.log").read())
print("error log:", open("errors.log").read().strip())
