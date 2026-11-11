# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""Demonstration: clean files, duplicate, invalid e-mail, damaged line, missing files."""
from festdesk.main import run

files = ["data/cse.txt", "data/ece.txt", "data/mech.txt",
         "data/civil.txt", "data/it.txt"]          # civil.txt and it.txt do not exist
print(run(files, out="out"))
