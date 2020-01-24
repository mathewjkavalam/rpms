from openpyxl import load_workbook
def isProjectPeriod(hr,day,projectperiodnamegiveninclasstt = ["PROJECT"]):
    if( worksheet1.cell(column=hr, row=day).value in projectperiodnamegiveninclasstt ):
        return True
    """Correct ordering here"""
    elif (hr > 3):
        return worksheet1.cell(column=hr - 3, row=day).value in projectperiodnamegiveninclasstt
    elif(hr > 2):
        return worksheet1.cell(column=hr - 2, row=day).value in projectperiodnamegiveninclasstt
    elif(hr > 1):
        return worksheet1.cell(column=hr-1, row=day).value in projectperiodnamegiveninclasstt
    return False
def isFreePeriod(hr,day,guideslno=1):
    return worksheet2.cell(column=hr, row=guideday(day,guideslno) ).value is  None
def guideday(day,slno=1):
    #print('##',slno)
    #print('#',(slno-1)*15 + day )
    return (slno-1)*15 + day
FILENAME1 = "_class_tt.xlsx"
SHEETNAME1 = "Sheet1"
FILENAME2 = "_guide_tt.xlsx"
SHEETNAME2 = "Sheet1"

workbook1 = load_workbook(filename=FILENAME1)
workbook2 = load_workbook(filename=FILENAME2)

#print("#",workbook.sheetnames)
worksheet1 = workbook1[SHEETNAME1]
worksheet2 = workbook2[SHEETNAME2]
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

monfri = [3,5,7,9,12]

COLUMN = 1
ROW = 0

classhours = [3,4,6,7,9,11,12]
#for COLUMN in range(4,7+1):
#    print("#",worksheet.cell(column=COLUMN,row=ROW).value)
"""
Sample INPUT:
TT
Sample OUTPUT:
Subject Names 
"""
#print("#",worksheet.cell(column=classhours[5],row=fri).value)
#for day in monfri:
#    for hr in classhours:
#        if( worksheet3.cell(column=hr, row=day).value != None ):
#            print( worksheet3.cell(column=hr, row=day).value )
print("###",isProjectPeriod(12,3),12,3)
for day in monfri:
    for hr in classhours:
        #print('#',worksheet1.cell(column=hr, row=day).value)
        if( isProjectPeriod(hr,day) ):
            guide_row = [1,16,31,46,61,76,91,106,121,136,151]
            print(isFreePeriod(hr,day,2),hr,day)

            #if(worksheet2.cell(column=hr, row=day).value == None and worksheet2.cell(column=hr, row=day).value == None):
            #    print("Possible")
