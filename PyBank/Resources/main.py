#adding dependencies
import os 
import csv

#assign path and join in the file 
budget_data = os.path.join("budget_data.csv")

# #create empty output variables 
months = 0
ProfitLoss = 0
num = 0 
change = 0 
dates = []
Profit = []
OverallProfit = []

#open and read csv
with open(budget_data) as csv_file: 
    pybank_reader = csv.reader(csv_file, delimiter=",")
    #skip the first row because there is a header
    FirstRow = next(pybank_reader)
    #starting to loop through every row 
    for row in pybank_reader: 
        #adding months and profits/losses to get totals 
        months = months + 1
        ProfitLoss = ProfitLoss + int(row[1])

        #keeping track of the dates and profit with index 
        dates.append(row[0])
        Profit.append(row[1])

#finding the change 
i = 1
for i in range(months - 1):
    change = int(Profit[i + 1]) -  int(Profit[i])
    OverallProfit.append(change)
    i += 1
    AvgChange = round(sum(OverallProfit)/len(OverallProfit), 2)

#finding greatest increase value and date
GreatInc = max(OverallProfit)
IncIndex = OverallProfit.index(GreatInc)
IncDate = dates[IncIndex]

#finding greatest decease value and date 
GreatDec = min(OverallProfit)
DecIndex = OverallProfit.index(GreatDec)
DecDate = dates[DecIndex]

DollarAvgChg = "${:.2f}".format(AvgChange)
DollarProfitLoss = "${:.2f}".format(ProfitLoss)
DollarGreatInc = "${:.2f}".format(GreatInc)
DollarGreatDec = "${:.2f}".format(GreatDec)
#prints
print(f"Total Months: {months}")
print(f"Total Profit: {DollarProfitLoss}")
print(f"Average Change: {DollarAvgChg}")
print(f"Greatest Increase in Profits: {IncDate} {DollarGreatInc}")
print(f"Greatest Decrease in Profits: {DecDate} {DollarGreatDec}")

#printing to text file 
with open('analysis1.txt', 'w') as f:
    f.write(f"Financial Analysis\n")
    f.write(f"---------------------------- \n")
    f.write(f"Total months: {months} \n")
    f.write(f"Total Profit: {DollarProfitLoss} \n")
    f.write(f"Average Change: {DollarAvgChg} \n")
    f.write(f"Greatest Increase in Profits: {IncDate} {DollarGreatInc} \n")
    f.write(f"Greatest Decrease in Profits: {DecDate} {DollarGreatDec}")
    #***need to get it to print the actual values