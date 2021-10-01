import os 
import csv

#assign path and join in the file 
# path = r'C:\Users\gtmor\Bootcamp\python_challenge\PyBank'
budget_data = os.path.join("budget_data.csv")
analysis1_file = os.path.join("analysis1.txt")

# #create empty output variables 
months = 0
ProfitLoss = 0
num = 0 
change = 0 
dates = []
OverallProfit = []

# #open and read csv
with open(budget_data) as csv_file: 
    pybank_reader = csv.reader(csv_file, delimiter=",")
    #skip the first row because there is a header
    FirstRow = next(pybank_reader)
    #starting to loop through every row 
    for row in pybank_reader: 
        #adding months and profits/losses to get totals 
        months = months + 1
        ProfitLoss = ProfitLoss + int(row[1])

        #keeping track of the dates 
        dates.append(row[0])

#finding the change 
i = 1
for i in range(months): 
    change = int(row[1])-num
    OverallProfit.append(change)
    num = int(row[1])
    AvgChange = round(sum(OverallProfit)/len(OverallProfit), 2)

#finding greatest increase value and date
GreatInc = max(OverallProfit)
IncIndex = OverallProfit.index(GreatInc)
IncDate = dates[IncIndex]

#finding greatest decease value and date 
GreatDec = min(OverallProfit)
DecIndex = OverallProfit.index(GreatDec)
DecDate = dates[DecIndex]

DollarProfitLoss = "${:.2f}".format(ProfitLoss)
#prints
print(f"Total Months: {months}")
print(f"Total Profit: {DollarProfitLoss}")
print(f"Average Change: {AvgChange}")
print(f"Greatest Increase in Profits: {IncDate} {GreatInc}")
print(f"Greatest Decrease in Profits: {DecDate} {GreatDec}")

#printing to text file 
with open('analysis1.txt', 'w') as f
    f.write("Financial Analysis\n")
    f.write("---------------------------- \n")
    f.write("Total months: {months} \n")
    f.write("Total Profit: {ProfitLoss} \n")
    f.write("Average Change: {AvgChange} \n")
    f.write("Greatest Increase in Profits: {IncDate} {GreatInc} \n")
    f.write("Greatest Decrease in Profits: {DecDate} {GreatDec}")
