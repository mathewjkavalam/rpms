import json

def get_dateclass_list():
    return [("21-03-2009","S8 CSA"),("21-02-2020","S8 CSB"),("21-02-2010","S8 CSC")]
def get_class_guideteam_dictionary():
    return {'S8 CSA':[('TEACHER1','S8 CSA1'),('TEACHER1','S8 CSA2'),('TEACHER2','S8  CSA3'),('TEACHER3','S8 CSA4')],'S8 CSB':[('TEACHER4','S8 CSB1'),('TEACHER5','S8 CSB2'),('TEACHER4','S8  CSB3'),('TEACHER3','S8 CSB4')],'S8 CSC':[('TEACHER1','S8 CSC1')]}
def get_class_time_dictionary():
    return {'S8 CSA':20,'S8 CSB':20,'S8 CSC':20}
def get_panel_distinct_dictionary():
    return {'S8 CSA':3,'S8 CSB':3,'S8 CSC':3}
def get_coord_dictionary():
    return {'S8 CSA':'TEACHER1','S8 CSB':'TEACHER2','S8 CSC':'TEACHER3'}
def get_faculty_called_count_dictionary():
    return {'TEACHER1':6,'TEACHER2':5,'TEACHER3':4,"TEACHER4":3,"TEACHER5":2,"TEACHER6":1}
def get_faculty_areaofinterest_dictionary():
    return {'TEACHER1':['1','2'],'TEACHER2':['1','2'],'TEACHER3':['1','2']}
def get_team_areaofinterest_dictionary():
    return { 'S8 CSA1':['1','2'],'S8 CSA2':['1','2'],'S8 CSA3':['1','2'],'S8 CSA4':['1','2'],'S8 CSB1':['1','2'],'S8 CSB2':['1','2'],'S8 CSB3':['1','2'],'S8 CSB4':['1','2'],'S8 CSC1':['1','2']}
def get_class_schedulableperiods_dictionary():
    return {'S8 CSA':['PROJECT'],'S8 CSB':['PROJECT'],'S8 CSC':['PROJECT']}
def get_active_class_list():
    return ['S8 CSA','S8 CSB','S8 CSC']
def get_classtt_list(classs = str()):
    with open('parser.json') as f:
        parserConfig = json.load(f)

    nameofclassttjson = parserConfig["id"] +classs+".xlsx"+ ".json"
    with open(nameofclassttjson) as f:
        classtt = json.load(f)
    return classtt
