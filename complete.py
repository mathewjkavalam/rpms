# sort class according to start date
from gets import get_class_guideteam_dictionary,get_class_time_dictionary,get_panel_distinct_dictionary,get_coord_dictionary,get_faculty_called_count_dictionary,get_dateclass_list,get_faculty_areaofinterest_dictionary,get_team_areaofinterest_dictionary,get_classtt_list,get_active_class_list
from excludes import is_exclude_time,is_exclude_faculty,is_exclude_team
from functions import default_faculty_list,panel_config_satisfied,get_panel_config
from orders import order_guides_ascendingly_called_list,order_faculty_areaofinterest_ascendingly_called_list
from timefunctions import find_next,time_to_period

def sort_class_start_date(date_class_tuples=[]):
    import datetime
    sorted = list()
    for d in date_class_tuples:
        sorted.append((datetime.datetime.strptime(d[0]+"-8:30","%d-%m-%Y-%H:%M"),d[1]))
    sorted.sort()
    return sorted

date_class_tuples = get_dateclass_list()
sorted_date_list = sort_class_start_date( date_class_tuples=date_class_tuples)

# take next from class

# update current
current_time_list = []
import datetime
for cl in range( len(date_class_tuples)):
    current_time_list.append(sorted_date_list[cl])
class_guideteam_remaining_dictionary = get_class_guideteam_dictionary()
class_time_dictionary = get_class_time_dictionary()
panel_distinct_dictionary = get_panel_distinct_dictionary()
coord_dictionary = get_coord_dictionary()
faculty_called_count_dictionary = get_faculty_called_count_dictionary()
faculty_areaofinterest_dictionary = get_faculty_areaofinterest_dictionary()
panel_config_dictionary = get_panel_config()
team_areaofinterest_dictionary = get_team_areaofinterest_dictionary()
active_class_list = get_active_class_list()
faculty_time_allocated_dictionary = {}
class_allocation_dictionary = {}

class_tt_dictionary = {}
for classs in active_class_list:
    class_tt_dictionary[classs] = get_classtt_list(classs=classs)

while(True):
    for key in range( len(sorted_date_list) ):
        classs = sorted_date_list[key][1]
        if is_exclude_time( time = current_time_list[key],classs = classs ):
            #excluding a complete period
            current_time_list[key] = find_next(mode="PERIOD",current=current_time_list[key],classs=classs,classtimedic=dict(),classtt=class_tt_dictionary[classs])
            #allocating next class
            continue
        else:
            #time ok
            default_faculty_actual_list = []
            for faculty in default_faculty_list( time = current_time_list[key],classs = classs ):
                if not is_exclude_faculty(faculty= faculty,time= current_time_list[key],classs=classs):
                    default_faculty_actual_list.append(faculty)
            #found actual defaults

            guide = ""
            cord = ""
            others = []
            team = ""
            current_distict = len(set(default_faculty_actual_list) )
            why_not_satisfied_list = panel_config_satisfied(config=panel_config_dictionary[classs] ,classs=classs,defult=default_faculty_actual_list,guide=guide,coordinator=cord,others=others)

            if "GUIDE NOT INCLUDED IN PANEL" in why_not_satisfied_list:
                #include a guide
                guide_inluded = False
                for guideteam in order_guides_ascendingly_called_list(guidecalledcountdictionary=faculty_called_count_dictionary ,guideteamremaining=class_guideteam_remaining_dictionary,priority=default_faculty_actual_list,classs=classs):
                    g,team = guideteam
                    if is_exclude_team(classs=classs,team=team,time=current_time_list[key]) or is_exclude_faculty(classs=classs,faculty = g,time=current_time_list[key]):
                        continue
                    else:
                        guide = g
                        guide_inluded =True
                        if g not in default_faculty_actual_list:
                            current_distict = current_distict + 1
                        break
            if "LESS DISTINCT FACULTY" in why_not_satisfied_list:
                while current_distict < panel_distinct_dictionary[classs]:
                    #excludes faculty
                    exclude = list()
                    for df in default_faculty_actual_list:
                        exclude.append(df)
                    if guide_inluded:
                        exclude.append(guide)
                    for fac in order_faculty_areaofinterest_ascendingly_called_list(facultycalledcountdictionary=faculty_called_count_dictionary,areaofinterest=faculty_areaofinterest_dictionary,teamarea=team_areaofinterest_dictionary[team],exclude=exclude):
                        if current_distict >= panel_distinct_dictionary[classs]:
                            break
                        else:
                            if is_exclude_faculty(classs=classs,faculty= fac,time= current_time_list[key]):
                                continue
                            else:
                                others.append(fac)
                                current_distict = current_distict + 1
        if classs in class_allocation_dictionary.keys():
            class_allocation_dictionary[classs].append({'time':current_time_list[key] ,'g':guide,'o':others,'d':default_faculty_actual_list})
        else:
            class_allocation_dictionary[classs] = list()
            class_allocation_dictionary[classs].append(
                {'time': current_time_list[key], 'g': guide, 'o': others, 'd': default_faculty_actual_list})
        current_time_list[key] = find_next(mode="SLOT",current=current_time_list[key],classs=classs,classtimedic=class_time_dictionary,classtt=class_time_dictionary[classs])

