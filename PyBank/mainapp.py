import os
import csv

csv_path="Resources/budget_data.csv"

def ReadReturnCSV(path):
    with open(path) as csv_file:
        csvreader=csv.reader(csv_file,delimiter=',')
        csv_header = next(csvreader)
        
        listA=[]
        listB=[]
        for row in csvreader:
            listA.append(row[0])
            listB.append(float(row[1]))
        
        dictAB=dict(zip(listA,listB))

    return dictAB
    
# The function returns length for iterable objects
def ReturnLengthIterableItem(it):
    itLenght=len(it)
    return(itLenght)

# Total number of months
dictBudget=ReadReturnCSV(csv_path)
totalNumberMonth=ReturnLengthIterableItem(dictBudget)
print("Total Number of Months: "+str(totalNumberMonth))


# Total budget
def TotalValueDict(dicta):
    total=0
    for key,value in dicta.items():
        total=total+value

    return total

budgetTotal=TotalValueDict(dictBudget)
print("Budget Total: $"+str(budgetTotal))


# Dictionary
# The code makes dictionary divided into dictionary by year

budget2010=[]
budget2011=[]
budget2012=[]
budget2013=[]
budget2014=[]
budget2015=[]
budget2016=[]
budget2017=[]
for key,value in dictBudget.items():
    stringDate=key.split("-")
    if stringDate[1]=="2010":
        date=stringDate[0]
        budget=value
        case = [date,budget]
        budget2010.append(case)

    if stringDate[1]=="2011":
        date=stringDate[0]
        budget=value
        case = [date,budget]
        budget2011.append(case)

    if stringDate[1]=="2012":
        date=stringDate[0]
        budget=value
        case = [date,budget]
        budget2012.append(case)

    if stringDate[1]=="2013":
        date=stringDate[0]
        budget=value
        case = [date,budget]
        budget2013.append(case)

    if stringDate[1]=="2014":
        date=stringDate[0]
        budget=value
        case = [date,budget]
        budget2014.append(case)

    if stringDate[1]=="2015":
        date=stringDate[0]
        budget=value
        case = [date,budget]
        budget2015.append(case)

    if stringDate[1]=="2016":
        date=stringDate[0]
        budget=value
        case = [date,budget]
        budget2016.append(case)

    if stringDate[1]=="2017":
        date=stringDate[0]
        budget=value
        case = [date,budget]
        budget2017.append(case)


dictBudget2010=dict(budget2010)

print(dictBudget2010)




