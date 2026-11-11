# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
import os


def write_master(path, students):
    with open(path, "w", encoding="utf-8") as f:
        for reg, (name, dept, email, evs) in sorted(students.items()):
            f.write("%s,%s,%s,%s,%s\n" % (reg, name, dept, email, ";".join(evs)))


def write_event_lists(folder, by_event):
    os.makedirs(folder, exist_ok=True)
    for ev, regs in by_event.items():
        with open(os.path.join(folder, ev.replace(" ", "_") + ".txt"), "w",
                  encoding="utf-8") as f:
            f.write("\n".join(sorted(regs)) + "\n")


def write_log(path, errors):
    with open(path, "w", encoding="utf-8") as f:
        for fname, no, msg in errors:
            f.write("%s | line %s | %s\n" % (fname, no, msg))
