import csv
with open("sample.csv",mode='r')as file:
    reader=csv.reader(file)
    for a in reader:
        print(a)
    