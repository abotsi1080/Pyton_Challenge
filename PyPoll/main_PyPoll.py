import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')

total_number_votes = 0 
list_candidate = []
dict_candidate = {}

winning_vote = 0 
winner = ""

with open(election_data_csv) as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=",")
        csv_header = next(csv_reader)
 
        for row in csv_reader:
            # Counting the total votes casted    
            total_number_votes += 1 
        
            # Getting the candidate name from the row 
            candidate = row[2]

            # begin the conditional if statement 
            if candidate not in list_candidate:
            # add the candidate to the list_candidate 
                list_candidate.append(candidate)
                dict_candidate[candidate] = 0

            
            dict_candidate[candidate] +=1 

output = 'Analysis/election_results.txt'
with open(output, "w") as txtfile:
