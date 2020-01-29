from openpyxl import load_workbook
def isProjectPeriod(hr,day):
    projectperiodnamegiveninclasstt = ["PROJECT"]
    ret = False
    if( worksheet1.cell(column=hr, row=day).value in projectperiodnamegiveninclasstt ):

        ret =  True
        return ret
    if( hr > 3):
            ret = worksheet1.cell(column=hr - 3, row=day).value in projectperiodnamegiveninclasstt or ret
    if (hr > 2):
         ret = worksheet1.cell(column = hr - 2, row=day).value in projectperiodnamegiveninclasstt or ret
    if(hr > 1):
         ret = worksheet1.cell(column = hr - 1, row=day).value in projectperiodnamegiveninclasstt or ret
    return ret
def isFreePeriod(hr,day,guideslno=1):
    return worksheet2.cell(column=hr, row=guideday(day,guideslno) ).value is  None
def guideday(day,slno=1):
    return (slno-1)*15 + day

FILENAME1 = "_class_tt.xlsx"
SHEETNAME1 = "Sheet1"
FILENAME2 = "_guide_tt.xlsx"
SHEETNAME2 = "Sheet1"

workbook1 = load_workbook(filename=FILENAME1)
workbook2 = load_workbook(filename=FILENAME2)


worksheet1 = workbook1[SHEETNAME1]
worksheet2 = workbook2[SHEETNAME2]


monfri = [3,5,7,9,12]

COLUMN = 1
ROW = 0

classhours = [3,4,6,7,9,11,12]
"""
Get Name of Faculty from _guide_tt.xlxs
print( worksheet2.cell(column=1, row= guideday(3, slno) ).value )

"""

"""
INPUT:
    
    FILES:
    class timetable
    faculty time table
    
    VARIABLE:
    day
    hr
    number of times each faculty is called 
    project coordinator name 
    team guide name
    number of total panel members
OUTPUT:
    panel Members Name
"""
