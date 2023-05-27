
import os
import csv

os.chdir("/Users/jody-annfrazer/Desktop/Class_Modules_Github/Python_Challenge_1/PyPoll/Resources")
# print(os.getcwd())

election_path = os.path.join('..', "Resources", "election_data.csv")

# Find the total number of votes
count = 0

# Start counters for each candidate vote
Charles_count = 0
Diana_count = 0
Raymon_count = 0

# Start percentages for each candidate's vote count
Charles_percent = 0
Diana_percent = 0
Raymon_percent = 0

# Open and read csv file
with open(election_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)
    # Read the header row first
    csv_header = next(csvreader)
    # election_data = list(csvreader)
    # print(f" CSV Header: {csv_header}")
    print("Election results")
    print("----------------------------")

    for row in csvreader:
      count = count + 1

      #Candidate = row[2]

      if row[2] == "Charles Casper Stockham":
            Charles_count += 1
      elif row[2] == "Diana DeGette":
            Diana_count += 1
      elif row[2] == "Raymon Anthony Doane":
            Raymon_count += 1

    # create a dictionary
    # Loop through dictionary to get candidate name as key and votes as value
      Results = {"Charles Casper Stockham": Charles_count,
               "Diana DeGette": Diana_count, "Raymon Anthony Doane": Raymon_count}

   # Calculate candiates percentages and round to 3dp
Charles_percent = round((Charles_count /count) * 100, 3)
Diana_percent = round((Diana_count /count) * 100, 3)
Raymon_percent = round((Raymon_count /count) * 100, 3)

    # Find the most popular votefrom the values in the dictionary and return its key
Winner = max(Results, key=Results.get)

 # Results
data = f"""
Total Votes: {count}
Charles Casper Stockham:{Charles_percent}% {Charles_count}
Diana Degette:{Diana_count}
Raymon Anthony Doane:{Raymon_count}
Winner: {Winner}"""

print(data)

output_file = os.path.join('..',"Analysis", "election_analysis.txt")
with open(output_file,"w") as txtfile:
    txtfile.write(data)