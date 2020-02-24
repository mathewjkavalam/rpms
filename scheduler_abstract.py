get_team_guide_info()
get_faculty_info()
get_class_info() # dictionary exclude_period

get_class_tts()
get_faculty_tts()

min_allocation = ''
minimum_cost_allocatedfaculty = ''

for run in range(10000):
    allocation  = []
    while(  is_team_remaining() ):
        selected_class = select_class()
        time = get_currenttime(selected= selected_class)
        if time_to_period(time) in exclude_period[selected_class]:
            update_currenttime(selected= selected_class,current=time,period_excluded = True)
        else:
            team,allocatedfaculty = try_to_satisfy_panel_config(time=time,selected=selected_class)
            update_team_faculty_allocation_info(time=time,team=team,faculty=allocatedfaculty)
            update_currenttime(selected=selected_class, current=time,period_excluded = False)

    if is_minimum_cost_allocation(present= allocation, prev=min_allocation):
        minimum_cost_allocatedfaculty = allocatedfaculty

update_faculty_called_count( called = minimum_cost_allocatedfaculty )