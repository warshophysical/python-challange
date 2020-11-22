import os
import csv

location="Resources/election_data.csv"
data_path=os.path.join(location)

with open(data_path) as data_file:
    csvreader = csv.reader(data_file, delimiter=',')
    csv_header = next(csvreader)
    
    print(f"csv Header: {csv_header}")
    
    Voter_ID=[]
    Candidate=[]
    for row in csvreader:
        Voter_ID.append(row[0])
        Candidate.append(row[2])
        
    election_dict=dict(zip(Voter_ID,Candidate))
    
    
    def total_voted(_dict):
        total=len(_dict)     ##### question 1
        print("Total Votes: "+str(total))
    
    def unique_candidate(_candidate):
        unique_candy=[]
        for c in _candidate:
            if c not in unique_candy:
                unique_candy.append(c)
        return unique_candy
    
    def vote_counter(_candidate):
        k,co,l,t=0,0,0,0

        for c in Candidate:
            if c=="Khan":
                k+=1
            elif c=="Correy":
                l+=1
            elif c=="Li":
                co+=1
            elif c=="O'Tooley":
                t+=1    

        vote_numbers=[k,co,l,t]
        return vote_numbers
    
    
    
    
    
    
    def percentage_calculator(_list):
        percentage_list=[]
        _list=vote_counter(Candidate)
        total_vote=sum(_list)
        for i in _list:
            percent=round((i/total_vote)*100,2)
            percent_string=str(percent)+"%"
            percentage_list.append(percent_string)
            percent_string=""
        
        return percentage_list
    
    
    
    def create_election_dict(_list):
        candidate=[]
        percentage=[]
        vote=[]
        candidate=unique_candidate(_list)
        percentage=percentage_calculator(_list)
        vote=vote_counter(_list)
    
        percentage_vote=zip(percentage,vote)  
        created_dict=dict(zip(candidate,percentage_vote))
    
        print(created_dict)
        
        
        
    def winner(_list):
        candidate=unique_candidate(_list)
        vote=vote_counter(_list)
    
        winner_dict=dict(zip(candidate,vote))
    
        Winner = max(winner_dict, key=winner_dict.get) 
        print("Winner: " +Winner) 
        
        
    
    print("######################################")
    print("ELECTION RESULTS")
    print("######################################")
    total_voted(election_dict)
    print("######################################")
    create_election_dict(Candidate)
    print("######################################")
    winner(Candidate)
    print("######################################")


