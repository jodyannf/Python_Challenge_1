
import os
import csv

os.chdir("/Users/jody-annfrazer/Desktop/Class_Modules_Github/Python_Challenge_1/PyPoll/Resources")
#print(os.getcwd())

election_path = os.path.join('..',"Resources", "election_data.csv")

#Open and read csv file 
with open(election_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)
#Read the header row first 
    csv_header = next(csvreader)
    print(f" CSV Header: {csv_header}")

    for row in csvreader:
    #print(row)