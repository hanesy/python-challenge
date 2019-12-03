
# ## PyBank
# ![Revenue](Images/revenue-per-lead.png)
# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)
# * Your task is to create a Python script that analyzes the records to calculate each of the following:
#   * The total number of months included in the dataset
#   * The net total amount of "Profit/Losses" over the entire period
#   * The average of the changes in "Profit/Losses" over the entire period
#   * The greatest increase in profits (date and amount) over the entire period
#   * The greatest decrease in losses (date and amount) over the entire period
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

# import os and csv modules, set path
import os
import csv
pybankpath = os.path.join('Resources', 'budget_data.csv')

#declare initial variables
months = []
profitloss = []
net_total = 0
# indices in changes[] will be lagging by 1 month from months[] and profitloss[].
changes = []
total_change = 0
increase_index = 0
decrease_index = 0
greatest_increase = 0
greatest_decrease = 0

#open and read
with open (pybankpath, newline='') as analysisfile:

    filereader = csv.reader(analysisfile, delimiter = ',')
    file_header = next (filereader)
    #check if header is loaded
    #print(f"headers: {file_header}")
    
    for row in filereader:
        months.append(row[0])
        profitloss.append(int(row[1]))
        #check if rows are loaded
        #print(row)

#   * The total number of months included in the dataset
num_months = len(months)

#   * The net total amount of "Profit/Losses" over the entire period
i = 0
j = len (profitloss)
for i in range (j):
    current_amount = int (profitloss[i])
    net_total = net_total+ current_amount
    
    if i > 0:
        previous_amount = int(profitloss[i-1])
        change_amount = current_amount - previous_amount
        changes.append(change_amount)
    

#   * The average of the changes in "Profit/Losses" over the entire period
#   * The greatest increase in profits (date and amount) over the entire period
#   * The greatest decrease in losses (date and amount) over the entire period
k = 0
l = len (changes) 

for k in range (l):
    total_change = total_change + int(changes[k])
    if changes[k] > greatest_increase:
        greatest_increase = changes[k]
        # add one to index to make sure the indices correspond to the correct month
        increase_index = k + 1
    if changes[k] < greatest_decrease:
        greatest_decrease = changes[k]
        # add one to index to make sure the indices correspond to the correct month
        decrease_index = k + 1


average_change= round(total_change / (l), 2)

increase_month = months[increase_index]
decrease_month = months[decrease_index]

print (f"""
Financial Analysis
----------------------------
Total Months: {num_months}
Total: ${net_total}
Average Change: ${average_change}
Greatest Increase in Profits: {increase_month} (${greatest_increase})
Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})

""")

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

output_path = os.path.join("pybank_output.txt")
with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row 
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow('----------------------------')
    csvwriter.writerow(['Total Months: ', num_months])
    csvwriter.writerow(['Total: ', net_total])
    csvwriter.writerow(['Average Change: ', average_change])
    csvwriter.writerow(['Greatest Increase in Profits: ', increase_month, greatest_increase])
    csvwriter.writerow(['Greatest Decrease in Profits: ', decrease_month, greatest_decrease])
