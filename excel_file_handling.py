import pandas as pd
import xlrd

file = pd.ExcelFile("C:/Users/user/Desktop/sales.xlsx") # creating excel sheet named sales.xlsx
print(file.sheet_names) # Gives list of all excel sheet names
sheet = file.parse('sales') # stores the content of sales excel sheet in "sheet" variable
print(sheet)
print(sheet.Customer_Name) # Customer_Name is the name of column in  sales excel sheet
print(sheet.Amount.sum()) # Amount is the colmn of sales sheet and sum() will add the values of Amount column
print(sheet.loc[0]) # will print the information of first row
print(sheet.loc[0, "Amount"]) # will give the Amount value of first row
print(sheet.set_index("Customer", inplace = True)) # select the Customer column
print(sheet.loc["MMC Inc."]) # now wil give all the information of customers whose Customer column value is MMC Inc.
sheet = sheet.reset_index()  # it can reset index to search again
print(sheet.loc[sheet['Invoice']==99]) # will give all info of the customer whose Invoice value is 99
print(sheet.loc[sheet['Amount'] > 2000])  # will give all info of customers whose Amount value > 2000
print(sheet.loc[sheet['Amount'].idxmax()])  # will give all info of customers who's having max Amount value

