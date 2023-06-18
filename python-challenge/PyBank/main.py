import os
import csv

'''
This script analyzes the financial records of a dummy company. 
The data set is provided is separate folder named as "Resources"
which is a csv file and contains two columns, Date and Profit/Losses.
The data presents the profit (postive values) or losses (negative values)
on a date.
The output of the script includes the following:
    - The total number of months included in the dataset
    - The net total amount of "Profit/Losses" over the entire period
    - The changes in "Profit/Losses" over the entire period, and then the 
      average of those changes
    - The greatest increase in profits (date and amount) over the entire period
    - The greatest decrease in profits (date and amount) over the entire period
The output will also be written in .txt file names as analysis.txt
in the analysis folder.
'''

# The path to the data set
csv_path = os.path.join('Resources','budget_data.csv')

#  Reading the csv file
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    #  Saving the headers
    csv_header = next(csv_reader)

    # saving the rows in variables of type list
    date = []
    profit_loss = []
    for row in csv_reader:
        date.append(row[0])
        profit_loss.append(int(row[1]))
    
    # Calcualting the Total months and Net Total
    total_months = len(date)
    net_total = sum(profit_loss)
    
    # Calcualting the changes, decreases and increases in profit/losses
    inc = []
    inc_idx = []
    dec = []
    dec_idx = []
    change = []
    for i in range(len(date)-1):
        # If the two consequtive rows are not equal then there is a change
        if profit_loss[i+1] != profit_loss[i]:
            change.append(profit_loss[i+1] - profit_loss[i])
            
        #  Checking for potential increases or decreases from row to row
        if profit_loss[i+1] > profit_loss[i]:
            inc.append(profit_loss[i+1]-profit_loss[i])
            inc_idx.append(i+1)
        elif profit_loss[i+1] < profit_loss[i]:
            dec.append(profit_loss[i]-profit_loss[i+1])
            dec_idx.append(i+1)

    # Writing the analysis in analysis\analysis.txt file
    output_path = 'analysis/analysis.txt'
    with open(output_path, 'w') as text:
        text.write('Financial Analysis')
        text.write('\n----------------------------')
        text.write('\nTotal Months: ' + str(total_months))
        text.write('\nTotal: $' + str(net_total))
        text.write('\nAverage Change: $' + str(round(sum(change)/len(change),2)))
        text.write('\nGreatest Increase in Profits: ' \
                   + str(date[inc_idx[inc.index(max(inc))]]) \
                   + ' (' + str(max(inc)) + ')')
        text.write('\nGreatest decrease in Profits: ' \
                   + str(date[dec_idx[dec.index(max(dec))]]) \
                   + ' ($-' + str(max(dec)) + ')')

# Printing the analysis in terminal
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')        
print(f'Average Change: ${round(sum(change)/len(change),2)}')
print(f'Greatest Increase in Profits: {date[inc_idx[inc.index(max(inc))]]} (${max(inc)})')
print(f'Greatest decrease in Profits: {date[dec_idx[dec.index(max(dec))]]} ($-{max(dec)})')
