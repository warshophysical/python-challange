import os
import csv

csv_path=os.path.join("Resources/budget_data.csv")

with open(csv_path) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    Date=[]
    Profit=[]
    for row in csvreader:
        Date.append(row[0])
        Profit.append(float(row[1]))
     
    budget=dict(zip(Date,Profit))   ### the dictionary holds zipped lists of Date and Profit/Losses
    
    def month_counter(_list):           ### the function that gives and print total number of months
        period_counter=len(_list)   
        print("Total Month: "+str(period_counter))
        
    def total_budget(_list):
        t_budget=0                      ### the function that gives and print total profit/losses
        for i in _list:
            t_budget=t_budget+budget[i]
        print("Total: $"+str(t_budget))
    
    
    def difference_list_elements(_list):
        budget_change_list=[]               ### the function that calculate the difference between consecutive numbers
        for i in range(0,len(_list)-1):     ### holds the results as list type
            budget_change_list.append(_list[i+1]-_list[i])
        return budget_change_list
    
    def average_calculator(_list):
        _list=difference_list_elements(Profit)
        number_change=len(_list)
        total_change=sum(_list)
        average_change=round(total_change/number_change,4)
    
        print("Average Change: $"+str(average_change))
        
        
        
    def create_sorted_dict(_date):
        change_month=[]                        ### holds the name of months that the change taken place
        for i in range(1,len(Date)):
            change_month.append(Date[i])
    
        change_budget=difference_list_elements(Profit)
        change_dict=dict(zip(change_month,change_budget)) ### the dictionary that hold months and budget change
        sorted_change_dict=dict(sorted(change_dict.items(),key=lambda x:x[1], reverse=True))
        return sorted_change_dict
    
    def print_greatest_increase(_sorted):
        _sorted=create_sorted_dict(Date)
        for x in list(_sorted)[0:1]:
            print ("Greatest Increase in Profits: {}, ${} ".format(x,  _sorted[x]))
            
            
    def print_greatest_decrease(_sorted):
        _sorted=create_sorted_dict(Date)
        for x in list(_sorted)[-1:]:
            print ("Greatest Decrease in Profits: {}, ${} ".format(x,  _sorted[x]))
            
            
            
            
    for i in range(0,5):
        i
    print("####################################")
print("FINANCIAL ANALYSIS")

month_counter(budget)
total_budget(budget)
average_calculator(Profit)
print_greatest_increase(Date)
print_greatest_decrease(Date)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        