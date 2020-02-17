from scheduling import min_start_date,team,before,faculty
import datetime

first_day = min_start_date(team)
now_day = first_day
now_hr = 1

cursor = 0
met = 0
cond1 = False
cond2 = False
cond3 = False
cond4 = False
while (met < len(team)):
    alloc = []
    tcs = team[cursor]["start"]
    cond1 = now_day >= datetime.datetime.strptime(tcs, '%d-%m-%Y')
    g = -1
    c = -1
    if cond1:
        guide_required = team[cursor]["panel"]["guide"] == "True"
        coord_required = team[cursor]["panel"]["coordinator"] == "True"
        if guide_required:
            g = guide_of_team(team[cursor]["index"])
            if free(g,now_hr,now_day):
                cond2 = True
                alloc.append( g )
        if coord_required:
            c = coordinator_of_team(team[cursor]["index"])
            if free(c,now_hr,now_day):
                cond3 = True
                alloc.append(c)
        if int( team[cursor]["panel"]["distinct"] ) == len( set(alloc) ):
            cond4 = True
        if cond4 != True and int( team[cursor]["panel"]["distinct"] ) < len( set(alloc) ):
            free_faculty = []
            for fac in  range( len(faculty) ):
                if free(fac,now_hr,now_day):
                    if fac not in [g,c]:
                        #not g or c
                        free_faculty.append(fac)
            minCalled = 10000000000000
            minCalledFac = -1
            for fac in free_faculty:
                if min( int( faculty[fac]["called"]),minCalled ) != minCalled:
                    minCalled = int( faculty[fac]["called"])
                    minCalledFac = fac
            alloc.append(minCalledFac)
        #7 hours per day
        now_hr = (now_hr + 1) % 8
        if now_hr == 0:
            now_hr = 1
            now_day = now_day + datetime.timedelta(days=1)
        cursor = (cursor + 1) % len(team)
