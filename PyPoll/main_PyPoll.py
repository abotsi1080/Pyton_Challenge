# Importing the operating system module
import os
# Importing the csv file needed to work with
import csv
#Calling or setting the csv file path
election_data_csv  = os.path.join("Resources", "election_data.csv")

# Defining the variable list
total_number_votes = 0
list_candidate = []
unique_candidate = []
Khan_Vote = 0
Correy_Vote = 0
Li_Vote = 0
OTooley_Vote = 0
vote_tally = [Khan_Vote, Correy_Vote, Li_Vote, OTooley_Vote]
# Open the csv file to read  
with open(election_data_csv ) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ',')
    csv_header = next(csv_reader)
    # Reading through each row of data after reading the header
    for row in csv_reader:
       # Counting the total votes casted  
       total_number_votes += 1

       #listing candidates with vote
       list_candidate.append(row[2])

# Looping through the candidates to calculate the percentage votes
for name in list_candidate:
        if name not in unique_candidate:
            unique_candidate.append(name)

        #starting new conditional statement to get the votes count for candidates
        if name == 'Khan':
            Khan_Vote += 1

        elif name == 'Correy':
            Correy_Vote += 1
        
        elif name == 'Li':
            Li_Vote += 1

        else:
            OTooley_Vote += 1

winning_vote_count = max(vote_tally)
winner = unique_candidate[vote_tally.index(winning_vote_count)]

 # Writing the voting resutls to text file
output = "Analysis/election_results.txt"
with open(output, "w") as txtfile:
    txtfile.write(f"Election Results" + "\n")
    txtfile.write(f"-------------------------" + "\n")  
    txtfile.write(f"Total Votes: {total_number_votes}" + "\n")
    txtfile.write(f"-------------------------" + "\n")
    txtfile.write(f"Khan: {round((Khan_Vote/total_number_votes)*100, )}% ({Khan_Vote})" + "\n")      
    txtfile.write(f"Correy: {round((Correy_Vote/total_number_votes)*100, 2)}% ({Correy_Vote})" + "\n")     
    txtfile.write(f"Li: {round((Li_Vote/total_number_votes)*100, 2)}% ({Li_Vote})" + "\n")     
    txtfile.write(f"O'Tooley: {round((OTooley_Vote/total_number_votes)*100, 2)}% ({OTooley_Vote})" + "\n")
    txtfile.write(f"-------------------------" + "\n") 
    txtfile.write(f"Winner: {winner}" + "\n")  
    txtfile.write(f"-------------------------" + "\n")

# Printing the voting results for viewing
    print("Election Results")
    print("-------------------------")  
    print(f"Total Votes: {total_number_votes}")
    print("-------------------------")
    print(f"Khan: {round((Khan_Vote/total_number_votes)*100, 2)}% ({Khan_Vote})")      
    print(f"Correy: {round((Correy_Vote/total_number_votes)*100, 2)}% ({Correy_Vote})")     
    print(f"Li: {round((Li_Vote/total_number_votes)*100, 2)}% ({Li_Vote})")     
    print(f"O'Tooley: {round((OTooley_Vote/total_number_votes)*100, 2)}% ({OTooley_Vote})")
    print("-------------------------") 
    print(f"Winner: {winner}")  
    print("-------------------------")
