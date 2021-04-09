#%%
import os
import csv
import sys

# Path to collect data from the Resources folder
csv_path = os.path.join('Resources','budget_data.csv')

#Read in the csv file
with open(csv_path,'r') as csvfile:
    #split the data on commas
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    total_months = []
    total_profit = []
    month_start = 0
    total_change = 0
    row_count = 0
    monthly_profit_change = 0
    greatest_profit_increase = 0
    greatest_profit_decrease = 0

     #-------------- Loop to Read Data ------------------------
    for row in csvreader:
        #read total months       
        total_months.append(str(row[0]))
        #read total profit
        total_profit.append(int(row[1]))
        #read date
        record_date = (row[0])
        #read month end for change
        month_end = int(row[1])
        #testing
        row_count = row_count + 1

        if row_count > 1:
            #determine the profit change for the month over month
            monthly_profit_change = month_end - month_start
        #determine greatest profit increase    
        if monthly_profit_change > greatest_profit_increase:
            greatest_profit_increase = monthly_profit_change
            greatest_profit_increase_date = record_date
        #determine greatest profit decrease 
        if monthly_profit_change < greatest_profit_decrease:
            greatest_profit_decrease = monthly_profit_change
            greatest_profit_decrease_date = record_date    
        #add the profit change to the total profit change
        total_change = total_change + monthly_profit_change
        #set the start month back to ending profit
        month_start = month_end
    total_number_months = len(total_months)
    #-------------- Print to Screen ------------------------
    print(f"Financial Analysis")
    print(f"-----------------------------")
    print(f"Total Months: {(total_number_months)}")
    print(f"Total: ${sum(total_profit)}")
    average_change = total_change /(len(total_months)-1)
    print(f"Average Change: ${(average_change):.2f}")
    print(f"Greatest Increase in Profits: {(greatest_profit_increase_date)} (${(greatest_profit_increase)})")
    print(f"Greatest Decrease in Profits: {(greatest_profit_decrease_date)} (${(greatest_profit_decrease)})")
    #-------------- Print to Text File ------------------------
    original_stdout = sys.stdout
    with open('FinancialAnalysis.txt', 'w') as f:
        sys.stdout = f
        print(f"Financial Analysis")
        print(f"-----------------------------")
        print(f"Total Months: {(total_number_months)}")
        print(f"Total: ${sum(total_profit)}")
        average_change = total_change /(len(total_months)-1)
        print(f"Average Change: ${(average_change):.2f}")
        print(f"Greatest Increase in Profits: {(greatest_profit_increase_date)} (${(greatest_profit_increase)})")
        print(f"Greatest Decrease in Profits: {(greatest_profit_decrease_date)} (${(greatest_profit_decrease)})")
        sys.stdout = original_stdout
    





#%%