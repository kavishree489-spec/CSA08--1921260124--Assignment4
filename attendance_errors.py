# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""Task 3 - Complete the Code (TODO 1 and TODO 2 solved) + complete try statement."""
import os
import tempfile


class InvalidRecord(Exception):
    """Raised when a line of the attendance file is not in the expected format."""


def parse_line(line):
    """'192311001,2026-10-08,P' -> ('192311001', '2026-10-08', 'P')"""
    parts = line.strip().split(",")
    # TODO 1 (solved)
    if len(parts) != 3:
        raise InvalidRecord("expected 3 fields, found %d" % len(parts))
    if parts[2] not in ("P", "A"):
        raise InvalidRecord("invalid status %r" % parts[2])
    return tuple(parts)


def summarise(path):
    present, absent, errors = 0, 0, []
    # TODO 2 (solved)
    try:
        with open(path, encoding="utf-8") as f:
            for no, line in enumerate(f, start=1):
                try:
                    reg, date, status = parse_line(line)
                except InvalidRecord as e:
                    errors.append((no, str(e)))
                else:
                    if status == "P":
                        present += 1
                    else:
                        absent += 1
    except FileNotFoundError:
        errors.append((0, "file not found: %s" % path))
    except PermissionError:
        errors.append((0, "permission denied: %s" % path))
    except UnicodeDecodeError as e:
        raise InvalidRecord("file is not valid UTF-8") from e   # keeps original cause
    return present, absent, errors


def summarise_full(path):
    """Task 3.3 - try / except / else / finally with raise ... from ..."""
    present = absent = 0
    f = None
    try:
        f = open(path, encoding="utf-8")
        lines = f.readlines()
    except FileNotFoundError as e:
        raise InvalidRecord("cannot read " + path) from e
    except UnicodeDecodeError as e:
        raise InvalidRecord("file is not valid UTF-8") from e
    else:
        for line in lines:
            try:
                status = parse_line(line)[2]
            except InvalidRecord:
                continue
            present += status == "P"
            absent += status == "A"
        print("file processed without error")
    finally:
        if f:
            f.close()                      # runs in every case
    return present, absent


if __name__ == "__main__":
    data = ("192311001,2026-10-08,P\n192311002,2026-10-08,A\n"
            "192311003,2026-10-08\n192311004,2026-10-08,L\n")
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False,
                                     encoding="utf-8") as tmp:
        tmp.write(data)
    print(summarise(tmp.name))
    print(summarise_full(tmp.name))
    os.remove(tmp.name)
    print(summarise("no_such_file.csv"))          # missing file handled
    try:
        summarise_full("no_such_file.csv")
    except InvalidRecord as e:
        print("InvalidRecord:", e, "| caused by:", repr(e.__cause__))
