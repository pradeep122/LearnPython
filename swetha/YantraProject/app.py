import csv
import os
import math
folderName = "CSV_Files"
path = "/Users/deepster/Sites/LearnPython/swetha/YantraProject/CSV_Files"
csvData = []
months = {'1': 'Jan',
          '2': 'Feb',
          '3': 'Mar',
          '4': 'Apr',
          '5': 'May',
          '6': 'Jun',
          '7': 'Jul',
          '8': 'Aug',
          '9': 'Sep',
          '10': 'Oct',
          '11': 'Nov',
          '12': 'Dec'}


def formatOfNumber(number):
    return float(format(float(number), '.2f'))


def extractMonthYear(filename):
    result = filename.split('_')
    return (months[result[1]], result[2])


def readCsvFile(filename):
    filePath = os.path.join(path, filename)
    with open(filePath, 'r') as csvFile:
        reader = csv.reader(csvFile)
        totalCost = 0
        for row in reader:
            if row[3] == 'LinkedLineItem' and row[12] == 'AmazonES':
                totalCost += float(row[28])
        return filename[:-4], totalCost
        csvFile.close()


def processFolder(folderName):
    csvFiles = [f for f in os.listdir(path) if f.endswith(".csv")]
    arr = []
    for file in csvFiles:
        arr.append(readCsvFile(file))
    return arr


csvData.append(["Month_Year", "Monthly Cost"])
totalCost = 0
for tuple in processFolder(folderName):
    csvData.append([extractMonthYear(tuple[0]), formatOfNumber(tuple[1])])
    # print(formatOfNumber(tuple[1]))
    totalCost += tuple[1]

roundedCost = math.ceil(totalCost * 100) / 100
# print(formatOfNumber(roundedCost))
csvData.append(["Total Cost", formatOfNumber(roundedCost)])

with open(path + '/summary.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()


# Clean Code
# Monthly cost should be rounded to 2 decimals
# Month Year shoud be formatted as "Feb, 2018"
