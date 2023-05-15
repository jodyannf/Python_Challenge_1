
import os
import csv

os.chdir("/Users/jody-annfrazer/Desktop/Class_Modules_Github/Python_Challenge_1/PyBank/Resources")
#print(os.getcwd())

Budget_path = os.path.join('..',"Resources", "budget_data.csv")

#Open and read csv file 
with open(Budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)
#Read the header row first 
    #csv_header = next(csvreader)
    #print(f" CSV Header: {csv_header}")
    print("Financial Analysis")

    for row in csvreader:
    #print(row)
     lines= len(list(csvreader))
     print("Total Months:" + str(lines))


