## challenge 1: pybank

#* In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company.
# [budget_data.csv] (pybank/resources/budget_data.csv).
# The dataset is composed of two columns: "Date" and "Profit/Losses".

#* Your task is to create a Python script that analyzes the records to calculate each of the following values:
# 1. The total number of months included in the dataset
# 2. The net total amount of "Profit/Losses" over the entire period
# 3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
# 4. The greatest increase in profits (date and amount) over the entire period
# 5.  The greatest decrease in profits (date and amount) over the entire period
#* Your analysis should align with the following results:

  #Financial Analysis
  #-------------------------
  #Total Months: 86
  #Total: $22564198
  #Average Change: $ -8311.11
  #Greatest Increase in Profits: Aug-16 ($1862002)
  #Greatest Decrease in Profits: Feb-14 ($-1825558)

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.  
#-------------------------------------------------------------------------------------------------------------------------

# ------------------------
#   Solution
# ------------------------

# Notes to self: Write one script for each of the provide datasets.
# Run each script separately to make sure that the code works for it respective dataset
# Submit assignment on gitlab


# Objective 1: Import modules os and csv

import csv 
import os

# objective 2: set the path for the file in PyBank

PyBank = os.path.join("Resources","budget_data.csv")

#Objective 3: Create the lists to store data

profit = []
monthly_changes = []
date = []

# initalize the variables as required.

count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# read the csv file
with open(budget_data) as csvfile:

    csvreader = csv.reader(budget_data,delimiter=',')
    header = next(csvreader)

    # conducting the ask
    for row in csvreader:
        # use count to count the numbers in this dataset
        count = count + 1

        # will need it when collecting the greatest increase and decrease in profits
        date.append(row[0])

        # append the profit information & calculate the total profit
        profit. append(row[1])
        total_profit = total_profit + int(row[1])

        #calculate the average change inprofits from month to month. Then calculate the average change in profits
        final_profit = int(row[1])
        monthly_change_profits = final_project - initial_project

        #store these monthly changes in a list
        monthly_changes.append(monthly_change_profits)

        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit

        #calculate the average change in profits
        average_change_profits = (total_change_profits/count)

        #find the max and min change in profits and the corresponding dates these changes were observed
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_increase_profits)]

    print("------------------------------------------------------------------")
    print("Financial Analysis")
    print("------------------------------------------------------------------")
    print("Total months: " + str(count))
    print("Total profits: " + "$" + str(total_profit))
    print("Average change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_data) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_data) + " ($" + str(greatest_decrease_profits) +")")
    print("------------------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("--------------------------------------------------------------------\n")
    text.write("    Financial Analysis"+ "\n")
    text.write("---------------------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " +"$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_data) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_data) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------------------\n")
