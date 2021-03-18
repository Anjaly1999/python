import csv
with open('D:/anjaly/pyfiles.csv', 'r') as file:
 reader = csv.reader(file)
 for row in reader:
     print(row)