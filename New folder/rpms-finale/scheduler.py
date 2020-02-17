from scheduling import min_start_date,team,before
from datetime import timedelta

first_day = min_start_date(team)
now_day = first_day

while(True):

    print( first_day,next_day )
    now_day = now_day + timedelta(days=1)
    for t in team:
        if before(t["start"],now_day):
            print( t["start"] )