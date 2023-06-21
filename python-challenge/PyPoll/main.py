import os
import csv

'''
A set of poll data called election_data.csv is given in the Resources ddirectory. 
The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
The output of this Python script analyzes the votes and calculates each of the following values:
    - The total number of votes cast
    - A complete list of candidates who received votes
    - The percentage of votes each candidate won
    - The total number of votes each candidate won
    - The winner of the election based on popular vote
    
The out pull will both be written in the terminal and will be saved in "analysis\analysis.txt"
'''

# The path to the data set
file_path = os.path.join('python-challenge','PyPoll','Resources', 'election_data.csv')

#  Read the data set
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    #  Store the headers
    headers = next(csv_reader)
    
    #  Save the ballot ids in a list
    ballot_id = []
    #  save the counties of votes (not required in this challenge)
    counties = []
    #  Save candidate names and increment the number of their votes if tey are voted
    candidates = dict()
    
    for row in csv_reader:
        ballot_id.append(row[0])
        if row[1] not in counties:
            counties.append(str(row[1]))
        if row[2] not in candidates.keys():
            candidates[str(row[2])] = 1
        else:
            candidates[str(row[2])] += 1
            
#  Calculate total number of votes
total_votes = len(ballot_id)

# Write the analysis to the terminal as well as the .txt file
out_put_path = os.path.join('python-challenge','PyPoll','analysis', 'analysis.txt')
with open(out_put_path, 'w') as text:
    text.write('Election Results')
    print('Election Results')
    
    text.write('\n-------------------------')
    print('-------------------------')
    
    text.write('\nTotal Votes: ' + str(total_votes))
    print(f'Total Votes: {total_votes}')
    
    text.write('\n-------------------------')
    print('-------------------------')
    
    for candidate in candidates.keys():
        text.write('\n' + str(candidate) + ': ' \
            + str(round(100*candidates[candidate]/total_votes,3)) + '% (' + str(candidates[candidate])+')')
        print(f'{candidate}: {round(100*candidates[candidate]/total_votes,3)}% ({candidates[candidate]})')
    
    text.write('\n-------------------------')
    print('-------------------------')
    
    text.write('\nWinner: ' + str(max(candidates, key=candidates.get)))
    print(f'Winner: {max(candidates, key=candidates.get)}')
    
    text.write('\n-------------------------')
    print('-------------------------')