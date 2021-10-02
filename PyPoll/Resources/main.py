#adding dependencies 
import os 
import csv 

#assign path and join in the file 
poll_data = os.path.join("election_data.csv")
analysis2_file = os.path.join("analysis2.txt")

#create empty variables for counting/collecting data 
votes = 0
candidates = [] #finding the candidates who are running 
votes_per = []  #finding the count per candidate
percentages = ()
all_info_dict = {}

#open and read csv file 
with open(poll_data) as csv_file: 
    pypoll_reader = csv.reader(csv_file, delimiter=",")
    #skip first row because there is a header
    FirstRow = next(pypoll_reader)

    #start looping through the data 
    for row in pypoll_reader: 
        #add votes to find total 
        votes = votes + 1 
        
        #finding a list of candidates and counting their votes 
        if row[2] not in candidates: 
            candidates.append(row[2])
            index = candidates.index(row[2])
            votes_per.append(1)
        else: 
            index = candidates.index(row[2])
            votes_per[index] += 1
    
    #finding percentages of candidates
    import numpy as np 
    percentages = np.divide(votes_per, votes)
    percentages = np.multiply(percentages, 100)

    #finding winner
    MaxVotes = max(votes_per)
    MaxIndex = votes_per.index(MaxVotes)
    winner = candidates[MaxIndex]

    #printing values
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {votes}") 
    print(f"-------------------------")   
    print(f"{candidates[0]}: {percentages[0]} ({votes_per[0]}) ")
    print(f"{candidates[1]}: {percentages[1]} ({votes_per[1]}) ")
    print(f"{candidates[2]}: {percentages[2]} ({votes_per[2]}) ")
    print(f"{candidates[3]}: {percentages[3]} ({votes_per[3]}) ")
    print(f"-------------------------") 
    print(f"Winner: {winner}")
    print(f"-------------------------")

#printing text to file 
with open('analysis2.txt', 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {votes}\n")
    f.write(f"{candidates[0]}: {percentages[0]} ({votes_per[0]}) \n")
    f.write(f"{candidates[1]}: {percentages[1]} ({votes_per[1]}) \n")
    f.write(f"{candidates[2]}: {percentages[2]} ({votes_per[2]}) \n")
    f.write(f"{candidates[3]}: {percentages[3]} ({votes_per[3]}) \n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")
