# ## PyPoll

# ![Vote-Counting](Images/Vote_counting.png)

# * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 

# import os module 
import os

#import csv module
import csv

#set path
pypollpath = os.path.join('Resources', 'election_data.csv')


# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
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

#   * A complete list of candidates who received votes
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
    candidate_percent.append(round((int(candidate_votes[j])/total_votes)*100,3))
#see % of votes
#for item in candidate_percent:
#   print (str(item))

#   * The winner of the election based on popular vote.
winner_index = 0
for j in range (c_max):
    if candidate_votes[j] > candidate_votes[winner_index]:
        winner_index = j

winner = candidate_list[winner_index]

print (f"""
Election Results
----------------------------
Total Votes: {total_votes}
----------------------------
""")

for j in range(c_max):
    print (f"{candidate_list[j]}: {candidate_percent[j]}% ({candidate_votes[j]})")

print (f"""----------------------------
 Winner {winner}
----------------------------""")

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

results = zip (candidate_list, candidate_percent, candidate_votes)

output_path = os.path.join("pypoll_output.csv")
with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election REsults"])
    csvwriter.writerow(["Total Votes", total_votes])
    csvwriter.writerow(["Candidate", "Percent Votes", "Total Votes"])
    csvwriter.writerows(results)

# ## Hints and Considerations

# * Consider what we've learned so far. To date, we've learned how to import modules like `csv`; 
# to read and write files in various formats; 
# to store contents in variables, lists, and dictionaries; 
# to iterate through basic data structures; 
# and to debug along the way. 
# Using what we've learned, try to break down you tasks into discrete mini-objectives. 
# This will be a _much_ better course of action than attempting to Google Search for a miracle.

# * As you will discover, for some of these challenges, the datasets are quite large. 
# This was done purposefully, as it showcases one of the limits of Excel-based analysis. 
# While our first instinct, as data analysts, is often to head straight into Excel, 
# creating scripts in Python can provide us with more robust options for handling "big data".

# * Your scripts should work for each dataset provided. 
# Run your script for each dataset separately to make sure that the code works for different data.

# * Feel encouraged to work in groups, but don't shortchange yourself by copying someone else's work. 
# You get what you put in, and the art of programming is extremely unforgiving to moochers. 
# Dig your heels in, burn the night oil, and learn this while you can! 
# These are skills that will pay dividends in your future career.

# * Start early, and reach out for help often! Challenge yourself to identify _specific_ questions for your instructors and TAs. 
# Don't resign yourself to simply saying, "I'm totally lost." 
# Come prepared to show your effort and thought patterns, we'll be happy to help along the way.

# * Always commit your work and back it up with GitHub pushes. 
# You don't want to lose hours of your work because you didn't push it to GitHub every half hour or so.

#   * **Commit often**.