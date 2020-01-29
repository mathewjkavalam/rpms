from openpyxl import load_workbook
def isProjectPeriod(hr,day):
    projectperiodnamegiveninclasstt = ["PROJECT"]
    ret = False
    if( classtt.cell(column=hr, row=day).value in projectperiodnamegiveninclasstt ):

        ret =  True
        return ret
    if( hr > 3):
            ret = classtt.cell(column=hr - 3, row=day).value in projectperiodnamegiveninclasstt or ret
    if (hr > 2):
         ret = classtt.cell(column = hr - 2, row=day).value in projectperiodnamegiveninclasstt or ret
    if(hr > 1):
         ret = classtt.cell(column = hr - 1, row=day).value in projectperiodnamegiveninclasstt or ret
    return ret
def isFreePeriod(hr,day,guideslno=1):
    # print("#",guidestt.cell(column=hr, row=guideday(day,guideslno) ).value)
    return guidestt.cell(column=hr, row=guideday(day,guideslno) ).value is  None
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

# mon third hour
day = 1
hr = 3

workD = { 1:3,2:5,3:7,4:9,5:12}
classH = {1:3,2:4,3:6,4:7,5:9,6:11,7:12}
CountOfFacultyCalled = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0}
coordname = "Amitha Mathew"
guidename = "Amitha Mathew"
maxpanelcount = 3

"""
check if coord free 
"""
def coordnameSlno(name = "" ):
    return 1
print(  isFreePeriod( classH[hr],workD[day],coordnameSlno(name=coordname) ) )

"""
check if guide free :)
"""
def guideSlno(name = "" ):
    return 1
if( guidename != coordname ):
    print(  isFreePeriod( classH[hr],workD[day],guideSlno(name=guidename) ) )
else:
    print("Guide and Coordinator same")
"""
Order remaining faculties
Priority Criteria:
    should have free on that hour 
    arrange ascendingly count called
    arrange ascendingly count of project hours free for her  
"""
facultyScore = {}
# facultyScore[1] = {"free":False,"calledcount":8,"freecount":3}
# print(facultyScore[1]["freecount"])
MAX_FACULTY_COUNT = 11
for num in range(1,MAX_FACULTY_COUNT+1):
    facultyScore[num]= {"free":isFreePeriod(classH[hr],workD[day],num),"calledcount":0,"freecount":0}
# print(facultyScore)
