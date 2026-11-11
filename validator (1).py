# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
from .reader import DamagedLine


def valid_email(e):
    if e.count("@") != 1 or " " in e:
        return False
    user, domain = e.split("@")
    return bool(user) and "." in domain and not domain.startswith(".") \
        and not domain.endswith(".")


def parse(line):
    parts = [p.strip() for p in line.split(",")]
    if len(parts) != 5:
        raise DamagedLine("expected 5 fields, found %d" % len(parts))
    reg, name, dept, email, events = parts
    if not reg.isdigit() or not name:
        raise DamagedLine("bad register number or empty name")
    if not valid_email(email):
        raise ValueError("invalid e-mail %r" % email)
    evs = [e.strip().title() for e in events.split(";") if e.strip()]
    if not evs:
        raise DamagedLine("no events chosen")
    return reg, name, dept, email.lower(), evs
