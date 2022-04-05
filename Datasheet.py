import csv
with open('dane.csv', newline='') as f:
    csvreader_object=csv.reader(f)
    next(csvreader_object)
    reader = csv.reader(f)
    data = list(reader)

print(data)
f.close()