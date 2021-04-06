#%%

import os
import csv

# Path to collect data from the Resources folder
csv_path = os.path.join('Resources','budget_data.csv')

#Read in the csv file
with open(csv_path,'r') as csvfile:
        #split the data on commas
        csvreader = csv.reader(csvfile,delimiter=',')
        header = next(csvreader)

        for row in csvreader:
                print(row)

#Define function and have it accept the 'profit_loss_data' as its sole parameter
#def print_profit_loss_totals(profit_loss_data):
        #Assign values to variables
        budget_date = csv_path[0]
        budget_profit_loss = csv_path[1]
        greatest_profit_increase = 0
        greatest_profit_decrease = 0
        net_total_profit_loss = 0
        change_profit_loss = 0

        #Total number of months included in the dataset
        num_rows = 0

        for row in open(csv_path):
                num_rows += 1
                 #Total number of months included in the dataset
                total_number_months = num_rows
                 #Net total amount of profit/loss over the entire period
                net_total_profit_loss = net_total_profit_loss + net_total_profit_loss
                #Average of the changes in profit/loss over the enitre period
                change_profit_loss = budget_profit_loss #need to subtract previous budget_profit_loss from previous record
                #Greatest increase in profits (date and amount) over entire period
                if change_profit_loss > greatest_profit_increase:
                        greatest_profict_increase = change_profit_loss
                #Greatest decrease in losses (date and amount) over entire period
                if change_profit_loss < greatest_profit_decrease:
                        greatest_profit_decrease = change_profit_loss
                total_change_profit_loss = total_change_profit_loss + change_profit_loss

        average_change_profit_loss = total_change_profit_loss / total_number_months

#%%