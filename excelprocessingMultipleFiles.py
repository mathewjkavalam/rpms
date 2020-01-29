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
FILENAME1 = "_class_tt.xlsx"
SHEETNAME1 = "Sheet1"
FILENAME2 = "_guide_tt.xlsx"
SHEETNAME2 = "Sheet1"

workbook1 = load_workbook(filename=FILENAME1)
workbook2 = load_workbook(filename=FILENAME2)


classtt = workbook1[SHEETNAME1]
guidestt = workbook2[SHEETNAME2]

workD = { 1:3,2:5,3:7,4:9,5:12}
classH = {1:3,2:4,3:6,4:7,5:9,6:11,7:12}
CountOfFacultyCalled = {1:0,2:0,3:1,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0}
coordname = "Amitha Mathew"
guidename = "Amitha Mathew"
maxpanelcount = 3
