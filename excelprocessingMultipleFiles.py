from openpyxl import load_workbook
FILENAME1 = "timetableguideX.xlsx"
SHEETNAME1 = "Sheet1"
FILENAME2 = "timetableguideY.xlsx"
SHEETNAME2 = "Sheet1"
FILENAME3 = "timetableclass.xlsx"
SHEETNAME3 = "Sheet1"

workbook1 = load_workbook(filename=FILENAME1)
workbook2 = load_workbook(filename=FILENAME2)
workbook3 = load_workbook(filename=FILENAME3)

#print("#",workbook.sheetnames)
worksheet1 = workbook1[SHEETNAME1]
worksheet2 = workbook2[SHEETNAME2]
worksheet3 = workbook3[SHEETNAME3]
"""
merged row cells need to take the starting row
to retrieve value;otherwise its none.
output:
# S1(D3-G3)
# None
# None
# None
"""
#COLUMN = 1
#ROW = 3
#print("#",worksheet.cell(column=COLUMN,row=ROW).value)
name = (1,1)

monfri = [3,5,7,9,11]

COLUMN = 1
ROW = 0

classhours = [0,3,4,6,7,9,11,12]
#for COLUMN in range(4,7+1):
#    print("#",worksheet.cell(column=COLUMN,row=ROW).value)
"""
Sample INPUT:
(fri,5)
Sample OUTPUT:
S7
"""
#print("#",worksheet.cell(column=classhours[5],row=fri).value)
for day in monfri:
    for hr in classhours:
        print day,hr