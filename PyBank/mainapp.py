
#Dependencies
import os
import csv


#Path to reach out data
csv_path=os.path.join("Resources/budget_data.csv")

# The function reading csv file, which using with os library.
# The function will return data as a dictionary
def ReadReturnCSV(path):
    with open(path) as csv_file:
        csvreader=csv.reader(csv_file,delimiter=',')

        ### Total Number of Month which have been effect to budget

        listMonths=[]
        listBudget=[]

        for row in csvreader:
            listMonths.append(row[0])
            listBudget.append(row[1])
        # the data which is list type are convert into dictionary with zip function
        dictBudget=dict(zip(listMonths,listBudget))

    return dictBudget
# The function returns length for iterable objects
def ReturnLengthIterableItem(it):
    itLenght=len(it)
    return(itLenght)

dictBudget=ReadReturnCSV(csv_path)
totalMonth=ReturnLengthIterableItem(dictBudget)
print("Total Number of Month: "+str(totalMonth))

totalBudget=0
for key,value in dictBudget.items():
    totalBudget=totalBudget+int(value)

print("Total Budget: "+"$"+str(totalBudget))
