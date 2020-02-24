import datetime
from gets import get_class_schedulableperiods_dictionary

period_start_end_nonfriday_dictionary = {
    1: {'start': datetime.datetime(day=day, month=month, year=year, hour=8, minute=30),
        'end': datetime.datetime(day=day, month=month, year=year, hour=9, minute=35)},
    2: {'start': datetime.datetime(day=day, month=month, year=year, hour=9, minute=35),
        'end': datetime.datetime(day=day, month=month, year=year, hour=10, minute=30)},
    3: {'start': datetime.datetime(day=day, month=month, year=year, hour=10, minute=45),
        'end': datetime.datetime(day=day, month=month, year=year, hour=11, minute=40)},
    4: {'start': datetime.datetime(day=day, month=month, year=year, hour=11, minute=40),
        'end': datetime.datetime(day=day, month=month, year=year, hour=12, minute=35)},
    5: {'start': datetime.datetime(day=day, month=month, year=year, hour=13, minute=35),
        'end': datetime.datetime(day=day, month=month, year=year, hour=14, minute=30)},
    6: {'start': datetime.datetime(day=day, month=month, year=year, hour=14, minute=40),
        'end': datetime.datetime(day=day, month=month, year=year, hour=15, minute=35)},
    7: {'start': datetime.datetime(day=day, month=month, year=year, hour=15, minute=35),
        'end': datetime.datetime(day=day, month=month, year=year, hour=16, minute=30)}
}
period_start_end_friday_dictionary = {
    1: {'start': datetime.datetime(day=day, month=month, year=year, hour=8, minute=30),
        'end': datetime.datetime(day=day, month=month, year=year, hour=9, minute=35)},
    2: {'start': datetime.datetime(day=day, month=month, year=year, hour=9, minute=35),
        'end': datetime.datetime(day=day, month=month, year=year, hour=10, minute=30)},
    3: {'start': datetime.datetime(day=day, month=month, year=year, hour=10, minute=45),
        'end': datetime.datetime(day=day, month=month, year=year, hour=11, minute=40)},
    4: {'start': datetime.datetime(day=day, month=month, year=year, hour=11, minute=40),
        'end': datetime.datetime(day=day, month=month, year=year, hour=12, minute=35)},
    5: {'start': datetime.datetime(day=day, month=month, year=year, hour=14, minute=0),
        'end': datetime.datetime(day=day, month=month, year=year, hour=14, minute=50)},
    6: {'start': datetime.datetime(day=day, month=month, year=year, hour=14, minute=50),
        'end': datetime.datetime(day=day, month=month, year=year, hour=15, minute=40)},
    7: {'start': datetime.datetime(day=day, month=month, year=year, hour=15, minute=40),
        'end': datetime.datetime(day=day, month=month, year=year, hour=16, minute=30)}
}

def find_next(mode=str(),current=datetime.datetime(),classs=str(),classtimedic=dict(),classtt=list()):
    nxt = datetime.datetime()
    if mode == 'SLOT':
        nxt = current + datetime.timedelta(minutes=classtimedic[classs])
        #schedulable blockend
        blockend = blockend_datetime(classs=classs,day=current.day,month=current.month,year=current.year,wday=current.weekday(),hr=current.hour,minute=current.minute,classtt=classtt)
        nomorepoint = blockend - datetime.timedelta(minutes=classtimedic[classs])
        if nxt > nomorepoint:
            return "NEXT BLOCK"
        #4:30
        dayend = datetime.datetime(hour=16,minute=30,day=current.day,month=current.month,year=current.year)
        nomorepoint = dayend - datetime.timedelta(minutes=classtimedic[classs])
        if nxt > nomorepoint:
            return "NEXT DAY"

    elif mode == 'PERIOD':
        nxt = next_schedulable_period_datetime(classtt=classtt,classs=classs,day=current.day,month=current.month,year=current.year,wday=current.weekday(),hr=current.hour,minute=current.minute)

    return nxt
def blockend_datetime(classs=str(),day=int(),month=int(),year=int(),wday=int(),hr=int(),minute=int(),classtt = list()):
    #project1 project2 project3 then blockend is project3 final hour

    period = time_to_period(classs=str(),day=int(),month=int(),year=int(),wday=int(),hr=int(),minute=int())
    indx = -1
    periodname = ""
    indx = day * 7 + period - 1
    periodname = classtt[indx]
    blockend_period = ''
    if period < 5:
        if periodname == classtt[day*7 + period+1 -1] and  period+1 <= 4:
            blockend_period = period + 1
        if periodname == classtt[day*7 + period+2 -1] and  period+2 <= 4:
            blockend_period = period + 2
        if periodname == classtt[day*7 + period+3 -1] and  period+3 <= 4:
            blockend_period = period + 3
    elif period < 7:
        if periodname == classtt[day * 7 + period + 1 - 1] and period + 1 <= 7:
            blockend_period = period + 1
        if periodname == classtt[day * 7 + period + 2 - 1] and period + 2 <= 7:
            blockend_period = period + 2
    friday = 4
    if day != friday:
        return period_start_end_nonfriday_dictionary[blockend_period]['end']
    else:
        return period_start_end_friday_dictionary[blockend_period]['end']

def time_to_period(wday=int(),day= int(),month=int(),year=int(),hr=int(),minute=int(),classs=str()):
    #first period is 1
    #last period is 7
    monday,tuesday,wednesday,thursday,friday = 0,1,2,3,4
    timepoint = datetime.datetime(day=day,month=month,year=year,hour=hr,minute=minute)

    if wday in [monday,tuesday,wednesday,thursday]:
        for period in range(1,7+1):
            if period_start_end_nonfriday_dictionary[hr]['start'] <= timepoint and timepoint < period_start_end_nonfriday_dictionary[hr]['end']:
                return period
    if wday in [friday]:
        for period in range(1, 7 + 1):
            if period_start_end_friday_dictionary[hr]['start'] <= timepoint and timepoint < period_start_end_friday_dictionary[hr]['end']:
                return period


def next_schedulable_period_datetime(classtt = list(),classs=str(),day=int(),month=int(),year=int(),wday=int(),hr=int(),minute=int()):
    friday = 4
    period = time_to_period(classs=str(),day=int(),month=int(),year=int(),wday=int(),hr=int(),minute=int())
    schedulabe = ''

    while schedulabe == '':
        if classtt[day * 7 + pnxt - 1] in get_class_schedulableperiods_dictionary()[classs]:
            schedulabe = pnxt
