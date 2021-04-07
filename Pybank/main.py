#%%

import os
import csv

# Path to collect data from the Resources folder
csv_path = os.path.join('Resources','budget_data.csv')

# Create initial variables
total_number_months = 0
net_total_profit_loss = 0
#budget_profit_loss = 0
#previous_budget_profit_loss = 0
#greatest_profit_increase = 0
#greatest_profit_decrease = 0
#total_change_profit_loss = 0
#change_profit_loss = 0


#Read in the csv file
with open(csv_path,'r') as csvfile:
        #split the data on commas
        csvreader = csv.reader(csvfile,delimiter=',')
        header = next(csvreader)

        for row in csvreader:
                #add to the number of months as 1 for each month
                total_number_months = total_number_months + 1
                #print(total_number_months)
                #read the profit or loss from this month and add to the total of profit or loss
                net_total_profit_loss += row[1]
                print(net_total_profit_loss)
                #read in the change in profit loss from previous month to this month
                #change_profit_loss = row[1] - row-1[1]
                #add this change to the total change
                #total_change_profit_loss = total_change_profit_loss + change_profit_loss
                #Greatest increase in profits (date and amount) over entire period
                #if change_profit_loss > greatest_profit_increase:
                #        greatest_profict_increase = change_profit_loss
                #Greatest decrease in losses (date and amount) over entire period
                #if change_profit_loss < greatest_profit_decrease:
                #        greatest_profit_decrease = change_profit_loss
                

#Define function and have it accept the 'profit_loss_data' as its sole parameter
#def print_profit_loss_totals(profit_loss_data):
#average_change_profit_loss = total_change_profit_loss / total_number_months
#print(average_change_profit_loss)

#%%