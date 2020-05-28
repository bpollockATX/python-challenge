import os
import csv

uniqueCandidates = []
VotesCast={}
totalVotesCast = 0
candidateName = '' 
maxVotesCast = 0
winner = ''   

election_data = os.path.join("../PyPoll", "election_data.csv")

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #csvwriter = csv.writer(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    
    
    for row in csvreader:
    
    #Tally up the votes                       
        totalVotesCast += 1  
        candidateName = (row[2])

    #stores unique candidates in list and stores vote count 
        if candidateName not in uniqueCandidates:         
            uniqueCandidates.append(row[2])
            VotesCast[candidateName]=0
        VotesCast[candidateName]+=1
    
    #print results to terminal

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {totalVotesCast}")
    print("-------------------------")

    for i in uniqueCandidates:
        
        percentWon = format((VotesCast[i]/totalVotesCast), ".3%")
     
        if VotesCast[i] > maxVotesCast:
            maxVotesCast = VotesCast[i]
            winner = i     
    
        print(f"{i}: {percentWon} ({VotesCast[i]})")
    
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

#output to csv
candidateResults = zip(i, percentWon, VotesCast)

output_file = os.path.join("output.csv") 

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Total Votes: {totalVotesCast}"])
    writer.writerow(["-------------------------"])

    for i in uniqueCandidates:
        
        percentWon = format((VotesCast[i]/totalVotesCast), ".3%")
     
        if VotesCast[i] > maxVotesCast:
            maxVotesCast = VotesCast[i]
            winner = i     
    
        writer.writerow([f"{i}: {percentWon} ({VotesCast[i]})"])

    writer.writerow(["-------------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["-------------------------"])