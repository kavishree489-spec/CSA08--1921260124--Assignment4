# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
"""attendance package."""
from .reader import read_records
from .stats import percentages, absent_three_days
from .report import write_report, write_absent_report
