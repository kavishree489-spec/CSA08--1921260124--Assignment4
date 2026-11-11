# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""Task 3.4 - misuse of 'except Exception: pass' hides a typing error."""
lines = ["1,2026-10-08,P", "2,2026-10-08,P"]
present = 0
for line in lines:
    try:
        parts = line.split(",")
        if parts[2] == "P":
            presnt += 1            # typo: should be 'present'
    except Exception:
        pass                       # UnboundLocalError is silently swallowed
print(present)                     # prints 0 although two students were present
