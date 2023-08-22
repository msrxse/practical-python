# pcost.py
#
import gzip

# Exercise 1.27
with open("Work/Data/portfolio.csv", "rt") as f:
    headers = next(f)
    result = 0
    for line in f:
        row = line.split(",")
        result += int(row[1]) * float(row[2])
    print(result)

with gzip.open("Work/Data/portfolio.csv.gz", "rt") as f:
    for line in f:
        print(line, end="")
