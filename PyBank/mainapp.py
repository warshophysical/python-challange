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


# MAIN DICTIONARY WHICH WAS CONVERTED FROM CSV
#####
dictBudget=ReadReturnCSV(csv_path)
#####

# Function which gives total value
def TotalValueDict(budgetDictionary):
    total=0
    for key,value in budgetDictionary.items():
        total=total+value

    return total


# The function which gives average change
def AverageValueDict(budgetDictionary):
    dictBudgetValues=list(budgetDictionary.values())
    
    listBudgetChange=[]
    for i in range(len(dictBudgetValues)-1):
        listBudgetChange.append(dictBudgetValues[i+1]-dictBudgetValues[i])

    totalChangeVolume=0
    numberChanged=0
    for i in listBudgetChange:
        totalChangeVolume=totalChangeVolume+i
        numberChanged=numberChanged+1


    averageChange=totalChangeVolume/numberChanged
    averageChange=round(averageChange,2)

    return averageChange



# Function calculates greatest increase of change
def BiggestIncrease(budgetDictionary):
    sortedbudgetDictionary=sorted(budgetDictionary.items(), key=lambda x: x[1])
    return sortedbudgetDictionary[-1]

# Function calculates greatest decrease of change
def BiggestDecrease(budgetDictionary):
    sortedbudgetDictionary=sorted(budgetDictionary.items(), key=lambda x: x[1])
    return sortedbudgetDictionary[1]

totalNumberMonth=len(dictBudget)
budgetTotal=TotalValueDict(dictBudget)
averageChange=AverageValueDict(dictBudget)
budgetBiggestIncrease= BiggestIncrease(dictBudget)
budgetBiggestDecrease= BiggestDecrease(dictBudget)


print("#########################")
print("FINANCIAL ANALYSIS")
print("Total Months: "+str(totalNumberMonth))
print("Budget Total: $"+str(budgetTotal))
print("Average Budget Change: $"+str(averageChange))
print("Biggest Increase: "+str(budgetBiggestIncrease))
print("Biggest Decrease: "+str(budgetBiggestDecrease))


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
dictBudget2011=dict(budget2011)
dictBudget2012=dict(budget2012)
dictBudget2013=dict(budget2013)
dictBudget2014=dict(budget2014)
dictBudget2015=dict(budget2015)
dictBudget2016=dict(budget2016)
dictBudget2017=dict(budget2017)
print("---------------")
budgetBiggestIncrease2010= BiggestIncrease(dictBudget2010)
budgetBiggestDecrease2010= BiggestDecrease(dictBudget2010)
print("Biggest Increase of 2010: "+str(budgetBiggestIncrease2010))
print("Biggest Decrease of 2010: "+str(budgetBiggestDecrease2010))
print("---------------")
budgetBiggestIncrease2011= BiggestIncrease(dictBudget2011)
budgetBiggestDecrease2011= BiggestDecrease(dictBudget2011)
print("Biggest Increase of 2011: "+str(budgetBiggestIncrease2011))
print("Biggest Decrease of 2011: "+str(budgetBiggestDecrease2011))
print("---------------")
budgetBiggestIncrease2012= BiggestIncrease(dictBudget2012)
budgetBiggestDecrease2012= BiggestDecrease(dictBudget2012)
print("Biggest Increase of 2012: "+str(budgetBiggestIncrease2012))
print("Biggest Decrease of 2012: "+str(budgetBiggestDecrease2012))
print("---------------")
budgetBiggestIncrease2013= BiggestIncrease(dictBudget2013)
budgetBiggestDecrease2013= BiggestDecrease(dictBudget2013)
print("Biggest Increase of 2013: "+str(budgetBiggestIncrease2013))
print("Biggest Decrease of 2013: "+str(budgetBiggestDecrease2013))
print("---------------")
budgetBiggestIncrease2014= BiggestIncrease(dictBudget2014)
budgetBiggestDecrease2014= BiggestDecrease(dictBudget2014)
print("Biggest Increase of 2014: "+str(budgetBiggestIncrease2014))
print("Biggest Decrease of 2014: "+str(budgetBiggestDecrease2014))
print("---------------")
budgetBiggestIncrease2015= BiggestIncrease(dictBudget2015)
budgetBiggestDecrease2015= BiggestDecrease(dictBudget2015)
print("Biggest Increase of 2015: "+str(budgetBiggestIncrease2015))
print("Biggest Decrease of 2015: "+str(budgetBiggestDecrease2015))
print("---------------")
budgetBiggestIncrease2016= BiggestIncrease(dictBudget2016)
budgetBiggestDecrease2016= BiggestDecrease(dictBudget2016)
print("Biggest Increase of 2016: "+str(budgetBiggestIncrease2016))
print("Biggest Decrease of 2016: "+str(budgetBiggestDecrease2016))
print("---------------")
budgetBiggestIncrease2017= BiggestIncrease(dictBudget2017)
budgetBiggestDecrease2017= BiggestDecrease(dictBudget2017)
print("Biggest Increase of 2017: "+str(budgetBiggestIncrease2017))
print("Biggest Decrease of 2017: "+str(budgetBiggestDecrease2017))






