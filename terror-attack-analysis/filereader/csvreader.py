import csv
from database import attackmodel

def readCsvFile(filename, func):
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            func(row)
    return
