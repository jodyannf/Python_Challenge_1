
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
    election_data = list(csvreader)
    #print(f" CSV Header: {csv_header}")
    print("Election results")
    
    #Find the total number of votes
    total_count = 0

    #Find the total number of votes each candidate got and the percentage vote
    candiate_name = list()
    candidates_votes= list()
    percetage_votes = list()
    
    for row in csvreader:
      count = count + 1
      
    
    

    print(len(election_data))
    #print("Charles Casper Stockham:")
    #print("Diana Degette:")
    #print("Raymon Anthony Doane:")
    print