# Python script to use openpyxl module to work with excel spredsheets
# Reference: https://www.youtube.com/watch?v=q6Mc_sAPZ2Y

import openpyxl
import os

os.chdir(r'C:\Users\dhamodv\Documents\Data_Sets')

wb = openpyxl.load_workbook('australian_postcodes.xlsx')
#print(type(wb))
#print(wb.sheetnames)
sheet = wb['australian_postcodes']

#Extract the spreadsheet cell values as below
A1_Value = sheet['A1'].value
B1_Value = sheet['B2'].value
print(A1_Value, B1_Value)
