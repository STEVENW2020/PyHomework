
import os
import csv

# path to data file
poll_csv = os.path.join('Resources', 'election_data.csv')


#variables
total_votes = 0 # sum of rows of votes cast
candidatelist = ["Khan", "Correy", "Li", "O'Tooley"]  # list of unique candidate names
candidate_vote_count = [0, 0, 0, 0]  # list of vote count

#read the csv file
with open(poll_csv, 'r') as csvfile:  # with open opens the file; as gives it an object name
    csvreader = csv.reader(csvfile, delimiter=",")  # CSV module reads the csv file and separates the test into columns by delimeter
    header = next(csvreader) # next is the current row in csvreader.  It is a header and is stored in a list called header.

    for row in csvreader:  # for iterates to subsequent rows.
        total_votes += 1  #This is the total votes cast, a count of rows
        
        candidate = (row[2]) # read in the candidate from column 3 of csv
        candidate_index = candidatelist.index(candidate)  # defines the index number of the candidate in candidate list
        candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1 # uses the candidate index and adds to the candidate's vote count
        

pct = [] # creates an empty list for percent
max_votes = candidate_vote_count[0]  # holding place fo the highest number of votes for a candidate
max_index = 0  # starts the loop through the list at the first item

for x in range(len(candidatelist)): # loop through each candidate
    #calculation to get the percentage   
    vote_pct = round(candidate_vote_count[x]/total_votes*100, 2) # calculates the vote % for each candidate, rounded 2 decimals
    pct.append(vote_pct) # adds the percent to the pct list
    
    if candidate_vote_count[x] > max_votes:  # determines which candidate gets the most votes
        max_votes = candidate_vote_count[x]  # candidate with most votes
        max_index = x                        # index of candidate with most votes

election_winner = candidatelist[max_index]  # identifies the election winner as candidate with most votes


#Prints to terminal

print('Results')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'Total Votes: {total_votes}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for x in range(len(candidatelist)):                            # prints each candidate and statistics
    print(f'{candidatelist[x]} : {pct[x]}% ({candidate_vote_count[x]})')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'Winner: {election_winner}')  #prints the winner 
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


#output txt file
output_file = os.path.join("pypoll_election_results.txt")  #confirmed syntax from https://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file
with open(output_file, "w") as file:
    
    file.write('Results\n')
    file.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    file.write(f'Total Votes: {total_votes}\n')
    file.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    for x in range(len(candidatelist)):
        file.write(f'{candidatelist[x]} : {pct[x]}% ({candidate_vote_count[x]})\n')
    file.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    file.write(f'Winner: {election_winner}\n')
    file.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    
