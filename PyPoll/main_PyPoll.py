import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

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
# Looping through the candidates to calculate the percentage votes
for candidate in dict_candidate:
    percentage_vote = round(float(dict_candidate[candidate])/float(total_number_votes), 2)

    votes = dict_candidate[candidate]
    if votes > winning_vote:
            winning_vote = votes
            winner = candidate

    output = "Analysis/election_results.txt"
    with open(output, "w") as txtfile:

# Writing the voting resutls to text file
        txtfile.write(f"Election Results" + "\n")
        txtfile.write(f"--------------------------------------" + "\n")
        txtfile.write(f"Total Votes: {total_number_votes}" + "\n")
        txtfile.write(f"--------------------------------------" + "\n")
        txtfile.write(f"{candidate}: {percentage_vote} {dict_candidate[candidate]}\n")
    #datafile.write(f"{candidate}: {percentage:.3%} ({dict_candidate[candidate]})\n")

# Printing the voting results for viewing
    print(f"Election Results")
    print(f"--------------------------------------")
    print(f"Total Votes: {total_number_votes}")
    print(f"--------------------------------------")
    print(f"{candidate}: {percentage_vote} {dict_candidate[candidate]}")
