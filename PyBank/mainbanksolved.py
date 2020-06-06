import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #Assign Varibles
    months = 0
    pltotal = 0
    previous = 0
    sumchange = 0
    poschange = 0
    negchange = 0
    posdate = ""
    negdate = ""

    # Loop through the data
    for row in csvreader:
        
        # calculations
        months += 1
        pltotal += int(row [1])
       
        # calculates change in P&L between rows
        if (previous == 0):
            change = int(row[1]) - int(row[1]) # if no previous row change is 0
        else: 
            change = int(row [1]) - previous
        
        sumchange += change
        
        # store value of largest positive change in P&L including date of change
        if (change > poschange):
            poschange = change
            posdate = str(row [0])

        # store value of largest negative change in P&L including date of change
        if (change < negchange):
            negchange = change
            negdate = str(row [0])

        change = 0  # resets change to 0 between iterations
        previous = int(row[1]) # sets previous to current value before iteration

    avgchange = sumchange /(months - 1)

    print ("Financial Analysis")
    print ("--------------------")            
    print ("Total Months: ",months)
    print ("Total P&L: $", format(pltotal, ",.0f"))
    print ("Average Change: $", format(avgchange, ",.2f"))
    print ("Greatest Monthly Increase in Profit: $", format (poschange, ",.0f"),"on", posdate)
    print ("Greatest Monthly Decrease in Profit: $", format (negchange, ",.0f"),"on", negdate)
    
#output txt file
output_file = os.path.join("pybank_financial_analysis.txt")  #confirmed syntax from https://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file
with open(output_file, "w") as file:
    
    file.write("Financial Analysis\n")
    file.write("--------------------\n")            
    file.write(f'Total Months: {months}\n')
    file.write(f'Total P&L: $ {pltotal:,}\n')
    file.write(f'Average Change: $ {avgchange:,.2f}\n')
    file.write(f'Greatest Monthly Increase in Profit: $ {poschange:,} on {posdate}\n')
    file.write(f'Greatest Monthly Decrease in Profit: $ {negchange:,} on {negdate}\n')



    
    

        

