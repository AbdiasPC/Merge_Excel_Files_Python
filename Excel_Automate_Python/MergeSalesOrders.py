import os
import openpyxl as xl
import pandas as pd

#Getting Working directory
cwd = os.getcwd()
#print(cwd)

#listing files in directory
files = os.listdir(cwd)
print(files)

#working files
files_selected = []
files_other_selected = []

#printing all files in directory 
for file in files:
    if "SampleData" in file:
        files_selected.append(file)
    else: 
        files_other_selected.append(file)

print(files_selected)
#print(files_other_selected)

#merging files
merge = pd.DataFrame()

for file in files_selected:
    df = pd.read_excel(file,sheet_name="SalesOrders",skiprows=1)
    merge = merge.append(df, ignore_index=True)

merge.to_excel("Sales_Merge.xlsx")












