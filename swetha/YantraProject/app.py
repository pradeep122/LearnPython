import csv
import os

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
        return (f"Month_Year: {filename[:-4]},Total Cost: {totalCost}")
        csvFile.close()


# def processFolder(foldername) return [(month,year, totalCost)]
# - extract all  csv files in the folder
# - for every csv file call readCSVFile
# - Add all tuples in an array and return
folderName = "CSV_Files"
path = "/Users/deepster/Sites/LearnPython/swetha/YantraProject/CSV_Files"


def processFolder(folderName):
    csvFiles = [f for f in os.listdir(path) if f.endswith(".csv")]
    arr = []
    for file in csvFiles:
        arr.append(readCsvFile(file))
    return arr


print(processFolder(folderName))
