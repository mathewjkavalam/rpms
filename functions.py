def default_faculty_list( time = "",classs = ""):
    return ['TEACHER1']
def panel_config_satisfied(config="",classs="",defult="",guide="",coordinator="",others=""):
    return ["GUIDE NOT INCLUDED IN PANEL","LESS DISTINCT FACULTY"]
def get_panel_config():
    return {"S8 CSA":{'guide':'yes','coordinator':'yes','distinct':3},"S8 CSB":{'guide':'yes','coordinator':'yes','distinct':3},"S8 CSC":{'guide':'yes','coordinator':'yes','distinct':3}}