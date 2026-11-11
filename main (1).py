# CSA08 Assignment 4 | Kavishree | Reg No: 1921260124
from reader import read_records
from stats import percentages, absent_three_days
from report import write_report, write_absent_report

if __name__ == "__main__":
    records = read_records("sample_data.txt")
    write_report(percentages(records), "report.txt")
    write_absent_report(absent_three_days(records), "absent3.txt")
    print("report.txt and absent3.txt written")
