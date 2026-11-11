# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""reader module."""

def read_records(path):
    """Read 'register,date,status' lines into lists."""
    with open(path, encoding="utf-8") as f:
        return [l.strip().split(",") for l in f if l.strip()]
