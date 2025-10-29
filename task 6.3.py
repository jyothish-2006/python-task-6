import csv
reader = csv.reader(open("d:\students.csv"))
for row in reader:
    print(row)
