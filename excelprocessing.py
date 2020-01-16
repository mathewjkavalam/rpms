from openpyxl import load_workbook
FILENAME = "timetableguide.xlsx"
SHEETNAME = "Faculty _TT "
workbook = load_workbook(filename=FILENAME)
#print("#",workbook.sheetnames)
worksheet = workbook[SHEETNAME]
"""
merged row cells need to take the starting row
to retrieve value;otherwise its none.
"""
COLUMN = 1
ROW = 5
print("#",worksheet.cell(column=COLUMN,row=ROW).value)
