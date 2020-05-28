import os
import csv

  
    
budget_data = os.path.join("../PyBank", "budget_data.csv")

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    
    total = 0
    uniqueMonths = []
    biggestIncrease = 0
    biggestIncreaseMonth = []
    biggestDecrease = 0
    biggestDecreaseMonth = []
    
    for row in csvreader:
    #stores unique months in list 
        if str(row[0]) not in uniqueMonths:         
            uniqueMonths.append(row[0])
        
    #Adds up profit and loss column for entire period
        pnl = int(row[1])                          
        total = total + pnl

    #Average of Changes in Profit and Loss during the period
        averageChange = total / (len(uniqueMonths))

    #Calculate Greatest increase in Profit
        if int(row[1]) > int(biggestIncrease):
            biggestIncrease = (row[1])
            biggestIncreaseMonth = (row[0])

    #Calculate Greatest Decrease in Profit
        if int(row[1]) < int(biggestDecrease):
            biggestDecrease = (row[1])
            biggestDecreaseMonth = (row[0])

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(uniqueMonths)}")
    print(f"Total: {total}")
    print(f"Average Change: {averageChange}")
    print(f"Greatest Increase in Profits: {biggestIncreaseMonth} (${biggestIncrease})")
    print(f"Greatest Decrease in Profits: {biggestDecreaseMonth} (${biggestDecrease})")

 