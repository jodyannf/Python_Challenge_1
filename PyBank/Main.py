
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
    csv_header = next(csvreader)
    print(f" CSV Header: {csv_header}")
    print("Financial Analysis")
    print("----------------------------")

    counter = 0 
    total = 0
    previous_profit = 1088983
    total_change = 0
    greatest_change = 0
    smallest_change = 0


    for row in csvreader:
        print (row[1])
        profit = int(row [1])
        month = row [0]

        counter = counter + 1
        total = total + profit
        Change = profit - previous_profit 
        previous_profit = profit
        total_change = total_change + Change

        if Change > greatest_change :
            greatest_change = Change
            greatest_month = month 

        if Change < smallest_change :
            smallest_change = Change 
            smallest_month = month

    print("Total Months:" +  str(counter))
    print ("Total: $" + str(total))
    print (f"Average Change: ${round (total_change/(counter-1), 2)}")
    print (f"Greatest Increase in profits: {greatest_month} ${greatest_change}")
    print (f"Greatest Decrease in profits: {smallest_month} ${smallest_change}")
