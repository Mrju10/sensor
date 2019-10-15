import csv
 
results = []
with open('tabla.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
    print results