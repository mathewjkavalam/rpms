from openpyxl import load_workbook
FILENAME = "timetableguide.xlsx"
SHEETNAME = "Sheet1"
workbook = load_workbook(filename=FILENAME)
#print("#",workbook.sheetnames)
worksheet = workbook[SHEETNAME]
"""
merged row cells need to take the starting row
to retrieve value;otherwise its none.
output:
# S1(D3-G3)
# None
# None
# None
"""
COLUMN = 1
ROW = 3
#print("#",worksheet.cell(column=COLUMN,row=ROW).value)
for COLUMN in range(4,7+1):
    print("#",worksheet.cell(column=COLUMN,row=ROW).value)
