import csv

with open('data.csv') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)

import csv

with open('data.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        print(row['nombre'], row['edad'])