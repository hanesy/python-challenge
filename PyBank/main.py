# ## PyBank

# ![Revenue](Images/revenue-per-lead.png)

# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# import os module 
import os

#import csv module
import csv

#set path
pybankpath = os.path.join('Resources', 'budget_data.csv')

# * Your task is to create a Python script that analyzes the records to calculate each of the following:
#   * The total number of months included in the dataset
months = []
#   * The net total amount of "Profit/Losses" over the entire period
#   * The average of the changes in "Profit/Losses" over the entire period
profitloss = []

#open and read
with open (pybankpath, newline='') as analysisfile:

    filereader = csv.reader(analysisfile, delimiter = ',')
    file_header = next (filereader)
    #check if header is loaded
    #print(f"headers: {file_header}")
    
    for row in filereader:
        #check if rows are loaded
        #print(row)
        months.append(row[0])
        profitloss.append(int(row[1]))

num_months = 0
for month in months:
    num_months += 1

net_total = 0
changes = []
#note that changes[] and months[] will have different indices

i = 0
j = len (profitloss)
for i in range (j):
    current_amount = int (profitloss[i])
    net_total = net_total+ current_amount
    
    if i > 0:
        previous_amount = int(profitloss[i-1])
        change_amount = current_amount - previous_amount
        changes.append(change_amount)

#   * The greatest increase in profits (date and amount) over the entire period
#   * The greatest decrease in losses (date and amount) over the entire period
k = 0
l = len (changes)

total_change = 0

increase_index = 0
decrease_index = 0
greatest_increase = 0
greatest_decrease = 0

for k in range (l):
    total_change = total_change + int(changes[k])
    if changes[k] > greatest_increase:
        greatest_increase = changes[k]
        increase_index = k
    if changes[k] < greatest_decrease:
        greatest_decrease = changes[k]
        decrease_index = k


average_change= round(total_change / (l), 2)

increase_month = months[increase_index+1]
decrease_month = months[decrease_index+1]

print (f"""
Financial Analysis
----------------------------
Total Months: {num_months}
Total: ${net_total}
Average Change: ${average_change}
Greatest Increase in Profits: {increase_month} (${greatest_increase})
Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})

""")

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.


output_path = os.path.join("pybank_output.csv")
with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row 
    csvwriter.writerow(['Financial Analysis', 'Month Info', 'Fin Info'])
    csvwriter.writerow(['Total Months', num_months])
    csvwriter.writerow(['Total','', net_total])
    csvwriter.writerow(['Average Change','', average_change])
    csvwriter.writerow(['Greatest Increase in Profits', increase_month, greatest_increase])
    csvwriter.writerow(['Greatest Decrease in Profits', decrease_month, greatest_decrease])


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