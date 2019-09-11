# Python script to use openpyxl module to work with excel spredsheets
# Reference: https://www.youtube.com/watch?v=q6Mc_sAPZ2Y

import openpyxl
import os

os.chdir(r'C:\Users\dhamodv\Documents\Data_Sets')

wb = openpyxl.load_workbook('australian_postcodes.xlsx')
#print(type(wb))
print(wb.sheetnames)