from openpyxl import load_workbook

def isProjectPeriod(hr,day):
    projectperiodnamegiveninclasstt = ["PROJECT"]
    ret = False
    if( classtt.cell(column=classH[hr], row=workD[day]).value in projectperiodnamegiveninclasstt ):
        ret =  True
    if( hr > 2):
            ret = classtt.cell(column=classH[hr - 2], row=workD[day]).value in projectperiodnamegiveninclasstt or ret
    if (hr > 1):
         ret = classtt.cell(column = classH[hr - 1], row=workD[day]).value in projectperiodnamegiveninclasstt or ret
    return ret
def isFreePeriod(hr,day,guideslno=1):
    # print("#",guidestt.cell(column=hr, row=guideday(day,guideslno) ).value)
    return guidestt.cell(column=hr, row=guideday(day,guideslno) ).value is  None
def guideday(day,slno=1):
    return (slno-1)*15 + day

FILENAME1 = "_class_tt_org.xlsx"
SHEETNAME1 = "Sheet1"
FILENAME2 = "_guide_tt_org.xlsx"
SHEETNAME2 = "Sheet1"

workbook1 = load_workbook(filename=FILENAME1)
workbook2 = load_workbook(filename=FILENAME2)


classtt = workbook1[SHEETNAME1]
guidestt = workbook2[SHEETNAME2]

day = 1
hr = 6

workD = { 1:3,2:5,3:7,4:9,5:12}
classH = {1:3,2:4,3:6,4:7,5:9,6:11,7:12}
