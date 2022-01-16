import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_number_votes = 0 
list_candidate = []
dict_candidate = {}

winning_vote = 0 
winner = ""

with open(csvpath, newline="") as csvfile:

        csvreader = csv.reader(csvfile, delimiter=",")
        reader = csv.reader(csvfile)
        next(reader, None)

        for row in reader:
            # start counting total votes    
            total_number_votes += 1 
        
            # get the reference to the candidate name from the row 
            candidate = row[2]

            # begin the if statement 
            if candidate not in list_candidate:
            # add the candidate to the list_candidate 
                list_candidate.append(candidate)
                dict_candidate[candidate] = 0

            
            dict_candidate[candidate] +=1 

output_file = 'Analysis/election_results.txt'
with open(output_file, "w", newline="") as txtfile:
