import csv
import os
import math

# def readCSVFile(filename) returns (month_year, totalCost)
# - open the file
# - go through every row and pick the ones with AmazonES product code
# - extract the total cost  and keep addig it to the final cose
# return month_year string and total cost


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


# def processFolder(foldername) return [(month,year, totalCost)]
# - extract all  csv files in the folder
# - for every csv file call readCSVFile
# - Add all tuples in an array and return
folderName = "CSV_Files"
path = "/Users/deepster/Sites/LearnPython/swetha/YantraProject/CSV_Files"

csvData = []


def processFolder(folderName):
    csvFiles = [f for f in os.listdir(path) if f.endswith(".csv")]
    arr = []
    for file in csvFiles:
        arr.append(readCsvFile(file))
    return arr


# To print MONTH_YEAR and MONTHLY_COST headers in Output csv file.
# print("Month Year  --  Monthly_Cost")
csvData.append(["Month_Year", "Monthly Cost"])
totalCost = 0
for tuple in processFolder(folderName):
    # print(f"({tuple[0]} -- {tuple[1]})")
    csvData.append([tuple[0], tuple[1]])
    totalCost += tuple[1]

roundedCost = math.ceil(totalCost * 100) / 100

# print(f"Total Cost - {roundedCost}")
csvData.append(["Total Cost", roundedCost])

with open(path + '/summary.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()


# To get the output in csv file


# Clean Code
# Monthly cost should be rounded to 2 decimals
# Month Year shoud be formatted as "Feb, 2018"
