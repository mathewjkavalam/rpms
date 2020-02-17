from scheduling import min_start_date,team,before
import datetime

first_day = min_start_date(team)
now_day = first_day

now_day = now_day + datetime.timedelta(days=1)
cursor = 0
while (cursor < len(team)):
    if now_day > datetime.datetime.strptime("13-1-2010", '%d-%m-%Y'):
        # Team is allowed to be allocated by date
        print(team[cursor])
    cursor = cursor + 1
