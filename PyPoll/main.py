# ## PyPoll
# ![Vote-Counting](Images/Vote_counting.png)
# * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.
# * As an example, your analysis should look similar to the one below:
#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```
# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# import os and csv modules, set path
import os
import csv
pypollpath = os.path.join('Resources', 'election_data.csv')

#declare initial variables
voter_id=[]
county=[]
voted_for=[]

#open and read
with open (pypollpath, newline='') as analysisfile:

    filereader = csv.reader(analysisfile, delimiter = ',')
    file_header = next (filereader)
    #check if header is loaded
    #print(f"headers: {file_header}")
    
    for row in filereader:
        #check if rows are loaded
        #print(row)
        voter_id.append(row[0])
        county.append((row[1]))
        voted_for.append((row[2]))

#   * The total number of votes cast
total_votes = len (voter_id)

#   * A complete list of unique candidates who received votes
candidate_list = []
i = 0
for name in voted_for:
    if name not in candidate_list:
        candidate_list.append(voted_for[i])
    i += 1

# see unique candidates
# for name in candidate_list:
#     print (name)

#   * The total number of votes each candidate won
candidate_votes = []
c_max = len (candidate_list)
for j in range (c_max):
    candidate_votes.append(0)
    for k in range (total_votes):
        if candidate_list[j] == voted_for [k]:
            candidate_votes[j] = int(candidate_votes[j]) + 1
#see number of votes
#for number in candidate_votes:
#    print (str(number))

#   * The percentage of votes each candidate won
candidate_percent = []
list_max = len (candidate_votes)
for j in range (list_max):
    percent =  format(float(((candidate_votes[j])/total_votes)*100), '.3f')
    candidate_percent.append(percent)

#see % of votes
#for item in candidate_percent:
#   print (str(item))

#   * The winner of the election based on popular vote.
winner_index = 0
for j in range (c_max):
    if candidate_votes[j] > candidate_votes[winner_index]:
        winner_index = j

winner = candidate_list[winner_index]

#print to terminal
print (f"""
Election Results
----------------------------
Total Votes: {total_votes}
----------------------------""")

for j in range(c_max):
    print (f"{candidate_list[j]}: {candidate_percent[j]}% ({candidate_votes[j]})")

print (f"""----------------------------
 Winner {winner}
----------------------------""")

#print to text file
output_path = os.path.join("pypoll_output.txt")
with open(output_path, 'a') as txt_file:
    txt_file.write (f"Election Results"+'\n')
    txt_file.write(f"-------------------------" + '\n')
    txt_file.write(f"Total Votes: {total_votes}" + '\n')
    for j in range(c_max):
        txt_file.write(f"{candidate_list[j]}: {candidate_percent[j]}% ({candidate_votes[j]})" + '\n')
    txt_file.write("--------------------------" + '\n')
    txt_file.write(f" Winner: {winner}")

