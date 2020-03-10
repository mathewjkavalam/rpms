from datetime import datetime,timedelta
import math
import json
import openpyxl
import random

#from external import fetch
def fetch(key = ''):
    data = {'paneldistinctcount':3,'isguidepresent':True,'iscoordinatorpresent':True,'startdate':'2020-02-07','exclusioncount':0}
    ret = data[key]
    return ret

from random import shuffle

def areaweigh(area1 = [],area2 = []):
    return len( set(area1).intersection( set(area2) ) )

class Sort:
    def __init__(self,things = list(),attribute = '',zeroplace = 0):
        self.things = things
        self.attributes = []
        self.zeroplace = zeroplace
        count = len(self.things)
        id = -1
        randids = []
        while len(randids) < count:
            for i in range(count):
                while (id in randids) or (id == -1):
                    id = random.randint(1, count)
                randids.append(id)
        for i in self.things:
            valthing = (i.__getattribute__(attribute),randids.pop(),i)
            self.attributes.append(valthing)

    def th(self,th):
        self.attributes.sort()
        return self.attributes[th-self.zeroplace][2]
    def thvalue(self,place):
        self.attributes.sort()
        return self.attributes[place-self.zeroplace][0]

    def minimum(self):
        self.attributes.sort()
        return self.attributes[0][2]
    def minimumvalue(self):
        self.attributes.sort()
        return self.attributes[0][0]
    def size(self):
        return len(self.attributes)

class Exclusion:
    def __init__(self,count= int()):
        if type(count) is int:
            self.count = count
        else:
            self.count = 0
        self.list = {}
    def add(self,date = '', period = -1,type = '' ,id = -1):
        date = datetime(month=date.month, year=date.year, day=date.day, hour=0, minute=0)
        period = int(period)
        type = str(type)
        #day,period,faculty,team
        id = int(id)
        if date not in self.list.keys():
            self.list[date] = {}
        if period not in self.list[date].keys():
            self.list[date][period] = {}
        if type not in self.list[date][period].keys():
            self.list[date][period][type] = []

        self.list[date][period][type].append(id)
    def isexcluded(self,date='',period=-1,type = '',id = -1):
        date = datetime(month=date.month, year=date.year, day=date.day, hour=0, minute=0)
        period = int(period)
        type = str(type)
        id = int(id)
        if date in self.list.keys():
            if period in self.list[date].keys():
                if type in self.list[date][period].keys():
                    if id in self.list[date][period][type]:
                        return True
        return False


class Date:
    def __init__(self, date = ''):
        year, month, day = 0, 1, 2
        date = date.split('-')
        self.self = datetime(day=int(date[day]), month=int(date[month]), year=int(date[year]))

    def __copy__(self):
        return Date(date=str(self.self.year) + '-' + str(self.self.month) + '-' + str(self.self.day)).self


class Community:
    def __init__(self,id = list(),allocatable = list(),strtdt = Date('1-1-1') ):
        self.startdate = strtdt.self
        with open('parser.json') as f:
            config = dict(json.load(f))
        with open( config["id"] + config["filenameclasstt"][0] + ".json" ) as f:
            self.tt = list( json.load(f) )
        self.id = list(id)
        self.allocatable = allocatable
        self.tt_cursor = self.startdate.weekday() * 7 - 1
        with open('coordinator.json') as f:
            self.coordinator = int( json.load(f) )
    def __copy__(self):
        return Community(id = self.id,allocatable = self.allocatable ,strtdt= Date(date=str(self.startdate.year) + '-' + str(self.startdate.month) + '-' + str(self.startdate.day)))
    def select(self, weekday = -1):
        a = weekday * 7
        return self.tt[ a : a + 7 ]

    def timeofday(self,period=int(),weekday=int()):
        if weekday in range(4) :
            if period == 1:
                return { 'begin':{'hour':8,'minute':30},'end':{'hour':9,'minute':35} }
            elif period == 2:
                return { 'begin':{'hour':9,'minute':35},'end':{'hour':10,'minute':30} }
            elif period == 2.5:
                return { 'begin':{'hour':10,'minute':30},'end':{'hour':10,'minute':45} }
            elif period == 3:
                return { 'begin':{'hour':10,'minute':45},'end':{'hour':11,'minute':40} }
            elif period == 4:
                return { 'begin':{'hour':11,'minute':40},'end':{'hour':12,'minute':35} }
            elif period == 4.5:
                return { 'begin':{'hour':12,'minute':35},'end':{'hour':13,'minute':35} }
            elif period == 5:
                return { 'begin':{'hour':13,'minute':35},'end':{'hour':14,'minute':30} }
            elif period == 5.5:
                return { 'begin':{'hour':14,'minute':30},'end':{'hour':14,'minute':40} }
            elif period == 6:
                return { 'begin':{'hour':14,'minute':40},'end':{'hour':15,'minute':35} }
            elif period == 7:
                return { 'begin':{'hour':15,'minute':35},'end':{'hour':16,'minute':30} }
        else:
            if period == 1:
                return { 'begin':{'hour':8,'minute':30},'end':{'hour':9,'minute':35} }
            elif period == 2:
                return { 'begin':{'hour':9,'minute':35},'end':{'hour':10,'minute':30} }
            elif period == 2.5:
                return { 'begin':{'hour':10,'minute':30},'end':{'hour':10,'minute':45} }
            elif period == 3:
                return { 'begin':{'hour':10,'minute':45},'end':{'hour':11,'minute':40} }
            elif period == 4:
                return { 'begin':{'hour':11,'minute':40},'end':{'hour':12,'minute':35} }
            elif period == 4.5:
                return { 'begin':{'hour':12,'minute':35},'end':{'hour':13,'minute':35} }
            elif period == 5:
                return { 'begin':{'hour':14,'minute':0},'end':{'hour':14,'minute':50} }
            elif period == 6:
                return { 'begin':{'hour':14,'minute':50},'end':{'hour':15,'minute':40} }
            elif period == 7:
                return { 'begin':{'hour':15,'minute':40},'end':{'hour':16,'minute':30} }
    def periodofday(self,weekday = int(),hour=int(),minute =int()):
        if weekday in range(4):
            for p in [1,2,2.5,3,4,4.5,5,5.5,6,7 ]:
                hs,ms = self.timeofday(period=p,weekday=weekday)['begin']['hour'],self.timeofday(period=p,weekday=weekday)['begin']['minute']
                he, me = self.timeofday(period=p, weekday=weekday)['end']['hour'], \
                         self.timeofday(period=p, weekday=weekday)['end']['minute']
                pstart,pend = datetime(year=1,month=1,day=1,hour=hs,minute=ms),datetime(year=1,month=1,day=1,hour=he,minute=me)
                x = datetime(year=1,month=1,day=1,hour=hour,minute=minute)
                if  pstart <= x and x < pend:
                    return p
        else:
            for p in [1,2,2.5,3,4,4.5,5,6,7 ]:
                hs,ms = self.timeofday(period=p,weekday=weekday)['begin']['hour'],self.timeofday(period=p,weekday=weekday)['begin']['minute']
                he, me = self.timeofday(period=p, weekday=weekday)['end']['hour'], \
                         self.timeofday(period=p, weekday=weekday)['end']['minute']
                if (hour in [hs] and minute >= ms) or (hour in [he] and minute < me):
                    return p
        return 8
    def next_schedulable(self,weekdelta = 0):
        if self.tt_cursor + 1 > 7 * 5 - 1:
            weekdelta = weekdelta + 1
            self.tt_cursor = 0
            return self.next_schedulable(weekdelta = weekdelta)

        if self.tt[ self.tt_cursor + 1 ] in self.allocatable:
            self.tt_cursor = self.tt_cursor + 1
            day = int( math.floor( self.tt_cursor / 7) )
            period = self.tt_cursor - day * 7 + 1
            return {'weekday':day,'period':period,'weekdelta':weekdelta}
        else:
            self.tt_cursor = self.tt_cursor + 1
            return self.next_schedulable(weekdelta=weekdelta)

class Faculty:
    def __init__(self,id = int()):
        self.id = id
        with open('faculty.json') as f:
            dic = dict(json.load(f))
            self.area = dic[str(id)]["area"].copy()
            self.name = str(dic[str(id)]["name"])
            self.cost = int(dic[str(id)]["cost"])
        with open('guide.json') as f:
            dic = dict(json.load(f))
            if str(self.id) in dic.keys():
                self.guided_teams = dic[str(self.id)]['team'].copy()
            else:
                self.guided_teams = []
        with open('parser.json') as f:
            config = dict(json.load(f))
        with open( config["id"] + "faculty_tt" + ".json" ) as f:
            self.tt = list( json.load(f) )
    def select(self,weekday = ''):
        a = ( (self.id -1)*35 + weekday * 7)
        return self.tt[ a : a + 7 ]
    def allocated(self):
        self.cost = self.cost + 1

class Team:
    def __init__(self,id = ''):
        self.id = int(id)
        self.isAllocated = False
        self.area = []
        with open('teamarea.json') as f:
            teamarea = dict(json.load(f))
            self.area = teamarea[str(self.id)]['area'].copy()

    def allocated(self):
        self.isAllocated = True

class Panel:
    def __init__(self,distinctcount = -1, isguidepresent = '', iscoordinatorpresent = ''):
        self.distinctcount = int( distinctcount )
        self.isguidepresent = bool( isguidepresent )
        self.iscoordinatorpresent =bool( iscoordinatorpresent )


class Allocate:
    def __init__(self, strtdt = Date('1-1-1') ,panel = Panel() , faculty = [] ,team = [], community = Community(), exclusion = Exclusion(),timeperteam = int()):
        startdate = strtdt.__copy__()
        self.startdate  = startdate
        self.panel = panel
        self.faculty = faculty
        self.community = community
        self.exclusion = exclusion
        self.allocatable = community.allocatable.copy()
        self.team = team
        self.allocation = []
        self.unitTime = timeperteam
        #update start
        self.week = 0
        self.month = int(startdate.month)
        self.year = int(startdate.year)
        self.day = int(startdate.day)
        self.weekday = int(startdate.weekday())
        self.hour = 8
        self.minute = 30
        self.begun = False
        # update end
    def current_time(self):
        return datetime(day=self.day,year=self.year,month=self.month,hour=self.hour,minute=self.minute)

    def allocated(self,pointtime = datetime(year=1,month=1,day=1),panel = list(),team = ''):
        self.allocation.append({'time':pointtime,'panel':panel,'team':team})

    def currentPeriodEnd(self):
        period = self.community.periodofday(hour=self.current_time().hour, minute=self.current_time().minute, \
                                               weekday=self.current_time().weekday())
        beginend_period = self.community.timeofday(period=period, weekday=self.current_time().weekday())
        end = beginend_period['end']
        endhour = end['hour']
        endminute = end['minute']
        now = self.current_time()

        return datetime(month=now.month,year=now.year,day=now.day,hour=endhour,minute=endminute)

    def get_next_slot(self):
        if not self.begun:
            weekday_period_weeksdelta = self.community.next_schedulable()
            dayspassed = weekday_period_weeksdelta['weekdelta'] * 7 + weekday_period_weeksdelta['weekday'] - self.weekday
            slot_day = self.current_time() + timedelta(days=dayspassed)
            begin_end = self.community.timeofday(period=weekday_period_weeksdelta['period'],weekday=weekday_period_weeksdelta['weekday'])
            hour,minute = begin_end['begin']['hour'],begin_end['begin']['minute']
            slot = datetime(month=slot_day.month,year=slot_day.year,day=slot_day.day,hour=hour,minute=minute)
            self.week = self.week + weekday_period_weeksdelta['weekdelta']
            self.begun = True
            self.month,self.year,self.day,self.hour,self.minute,self.weekday = slot.month,slot.year,slot.day,slot.hour,slot.minute,slot.weekday()
            self.community.tt_cursor = slot.weekday()*7 + self.community.periodofday(weekday=slot.weekday(),hour=slot.hour,minute=slot.minute) - 1
            return slot
        else:
            period = self.community.periodofday(hour=self.hour,minute=self.minute,weekday=self.weekday)
            begin_end = self.community.timeofday(period=period,weekday=self.weekday)
            endhour,endminute = begin_end['end']['hour'],begin_end['end']['minute']
            periodend = datetime(month=self.month,year=self.year,day=self.day,hour=endhour,minute=endminute)
            slotend = self.current_time() + timedelta(minutes=2*self.unitTime)
            slotendperiod = self.community.periodofday(weekday=slotend.weekday(),hour=slotend.hour,minute=slotend.minute)
            withinperiod = slotend < periodend
            withinjoinedperiod = False
            if slotendperiod not in [4.5,8]:
                withinjoinedperiod = self.community.select(weekday=slotend.weekday())[int(slotendperiod)-1] in allocatable
            else:
                if slotendperiod in [8]:
                    self.community.tt_cursor = self.community.tt_cursor + 1
                elif slotendperiod in [4.5]:
                    self.community.tt_cursor = self.weekday * 7 + 3
            if withinjoinedperiod or withinperiod:
                if withinperiod:
                    slot = self.current_time() + timedelta(minutes= self.unitTime)
                    self.month, self.year, self.day, self.hour, self.minute,self.weekday = slot.month, slot.year, slot.day, slot.hour, slot.minute,slot.weekday()
                    self.community.tt_cursor = slot.weekday() * 7 + int(self.community.periodofday(weekday=slot.weekday(),hour=slot.hour,minute=slot.minute)) - 1
                    return slot
                elif withinjoinedperiod:
                    slot = self.current_time() + timedelta(minutes=self.unitTime)
                    self.month, self.year, self.day, self.hour, self.minute, self.weekday = slot.month, slot.year, slot.day, slot.hour, slot.minute, slot.weekday()
                    self.community.tt_cursor = slot.weekday() * 7 + int( self.community.periodofday(weekday=slot.weekday(),hour=slot.hour, minute=slot.minute) )- 1
                    return slot
                else:
                    pass
            else:
                weekday_period_weeksdelta = self.community.next_schedulable()
                dayspassed = weekday_period_weeksdelta['weekdelta'] * 7 + weekday_period_weeksdelta['weekday'] - self.weekday
                slot_day = self.current_time() + timedelta(days=dayspassed)
                begin_end = self.community.timeofday(period=weekday_period_weeksdelta['period'],weekday=weekday_period_weeksdelta['weekday'])
                hour, minute = begin_end['begin']['hour'], begin_end['begin']['minute']
                slot = datetime(month=slot_day.month, year=slot_day.year, day=slot_day.day, hour=hour, minute=minute)
                self.week = self.week + weekday_period_weeksdelta['weekdelta']
                self.month, self.year, self.day, self.hour, self.minute, self.weekday = slot.month, slot.year, slot.day, slot.hour, slot.minute, slot.weekday()
                self.community.tt_cursor = slot.weekday() * 7 + int( self.community.periodofday(weekday=slot.weekday(),hour=slot.hour,minute=slot.minute) ) - 1
                return slot
    def run(self,idfortuple):
        # allocation logic
        notYetAllocated = []
        for team in self.team.copy():
            notYetAllocated.append(team.id)
        faculty = self.faculty.copy()
        while notYetAllocated != []:
            sortedfac = Sort(
                things=faculty, attribute='cost'
            )
            slotendperiod = ''
            slotstartperiod = ''
            while True:
                slot = self.get_next_slot()
                slotend = slot + timedelta(minutes= self.unitTime)
                slotstartperiod = self.community.periodofday(weekday=slot.weekday(),hour=slot.hour,minute=slot.minute)
                slotendperiod = self.community.periodofday(weekday=slotend.weekday(),hour=slotend.hour,minute=slotend.minute)
                excludeslot = self.exclusion.isexcluded(date=slot,type='date') or self.exclusion.isexcluded(date=slot,type='period',period=slotstartperiod) or self.exclusion.isexcluded(date=slot,type='period',period=slotendperiod)
                if not excludeslot:
                    break
            panel = []
            team = 'none'
            status = {'c':False,'g':False,'d':False}
            period,weekday = self.community.periodofday(weekday=slot.weekday(),hour=slot.hour,minute=slot.minute),slot.weekday()
            case1coord = faculty[ self.community.coordinator - 1].select(weekday=weekday)[int(period)-1][0] == 'FREE' and faculty[ self.community.coordinator - 1].select(weekday=weekday)[int(slotendperiod)-1][0] == 'FREE'
            case2coord = faculty[ self.community.coordinator - 1].select(weekday=weekday)[int(period)-1][1] in self.community.id and faculty[ self.community.coordinator - 1].select(weekday=weekday)[int(slotendperiod)-1][1] in self.community.id
            exclusioncoord = self.exclusion.isexcluded(date=slot,type='faculty',period=slotstartperiod,id=self.community.coordinator) or self.exclusion.isexcluded(date=slot,type='faculty',period=slotendperiod,id=self.community.coordinator)
            if self.panel.iscoordinatorpresent and self.panel.distinctcount > 0:
                if (case1coord or case2coord) and (not exclusioncoord):
                    panel.append(self.community.coordinator)
                    status['c'] = True
                else:
                    pass
                    #deadend
            if self.panel.isguidepresent and self.panel.distinctcount > 0:
                for person in range(sortedfac.size()):
                    maybeguide = sortedfac.th(th=person)
                    exclusiong = self.exclusion.isexcluded(date=slot,type='faculty',period=slotstartperiod,id=maybeguide.id) or self.exclusion.isexcluded(date=slot,type='faculty',period=slotendperiod,id=maybeguide.id)
                    case1g = maybeguide.select(weekday=weekday)[int(period) - 1][0] == 'FREE' and maybeguide.select(weekday=weekday)[int(slotendperiod) - 1][0] == 'FREE'
                    case2g = maybeguide.select(weekday=weekday)[int(period) - 1][1] in self.community.id and maybeguide.select(weekday=weekday)[int(slotendperiod) - 1][1] in self.community.id
                    if set( maybeguide.guided_teams ).intersection(notYetAllocated) != set() and (case1g or case2g) and (not exclusiong):
                        his_teams_tobe_allocated = set( maybeguide.guided_teams ).intersection(notYetAllocated)
                        his_teams_tobe_allocated = list(his_teams_tobe_allocated)
                        i = 0
                        shuffle(his_teams_tobe_allocated)
                        while True:
                            team = his_teams_tobe_allocated[i]
                            exclusionteam = self.exclusion.isexcluded(date=slot,type='team',period=slotstartperiod,id=team) or self.exclusion.isexcluded(date=slot,type='team',period=slotendperiod,id=team)
                            if not exclusionteam:
                                break
                            if i >= len(his_teams_tobe_allocated)-1:
                                i = 'no team for guide'
                                break
                            i = i + 1
                        if i != 'no team for guide':
                            panel.append(maybeguide.id)
                            status['g'] = True
                            break
                    if team == 'none':
                        pass
                    #deadend
            elif not self.panel.isguidepresent and self.panel.distinctcount > 0:
                teams_yet_to_be_allocated = notYetAllocated.copy()
                shuffle(teams_yet_to_be_allocated)
                i = 0
                while True:
                    team = teams_yet_to_be_allocated[i]
                    exclusionteam = self.exclusion.isexcluded(date=slot, type='team', period=slotstartperiod,id=team) or self.exclusion.isexcluded(date=slot, type='team',period=slotendperiod,id=team)
                    if not exclusionteam:
                        break
                    if i >= len(his_teams_tobe_allocated) - 1:
                        team = 'no team'
                        break
                    i = i + 1
            if self.panel.distinctcount > len( set(panel) ) and team != 'none':
                deficient = self.panel.distinctcount - len( set(panel) )
                areaweight_cost_personid = []
                #priority to area of interest than cost
                for person in range(len(self.faculty)):
                    areaweight_cost_personid.append( ( areaweigh( faculty[person].area,self.team[team].area),-1 * faculty[person].cost,person+1) )
                areaweight_cost_personid.sort(reverse=True)
                areaweighted = []
                for w_cost_id in areaweight_cost_personid:
                    areaweighted.append( w_cost_id[2] )
                for possibleperson in areaweighted:
                    if deficient < 1:
                        status['d'] = True
                        break
                    else:
                        possibleperson = faculty[possibleperson-1]
                        if possibleperson.id not in panel:
                            exclusionp = self.exclusion.isexcluded(date=slot,period=slotstartperiod,type='faculty',id=possibleperson.id) or self.exclusion.isexcluded(date=slot,period=slotendperiod,type='faculty',id=possibleperson.id)
                            case1 = possibleperson.select(weekday=weekday)[int(period)-1][0] == 'FREE' and possibleperson.select(weekday=weekday)[int(slotendperiod)-1][0] == 'FREE'
                            case2 = possibleperson.select(weekday=weekday)[int(period)-1][1] in self.community.id and possibleperson.select(weekday=weekday)[int(slotendperiod)-1][1] in self.community.id
                            if (case1 or case2) and (not exclusionp):
                                panel.append(possibleperson.id)
                                deficient = deficient - 1
            if self.panel.distinctcount == len(set(panel)):
                status['d'] = True
            if self.panel.iscoordinatorpresent == status['c'] and self.panel.isguidepresent == status['g']  and status['d'] and team != 'no team':
                panel = list(set(panel))
                self.allocated(pointtime=slot,panel=panel,team=team)
                for people in faculty:
                    if people.id in panel:
                        people.allocated()
                notYetAllocated.remove(team)
        finalslot = slot
        delta = finalslot - self.startdate
        deltaseconds = delta.total_seconds()
        return (deltaseconds,idfortuple,self.allocation)

    def print_output(self,filename= '', result= []):
        toprint = {}
        for row in range(1, len(result) + 1 + 1 ):
            if row == 1:
                toprint[1] = {'A':'Time','B':'Team','C':'Panel' }
            else:
                panelnames = []
                for person in result[row-2]['panel']:
                    for fac in self.faculty:
                        if fac.id == person:
                            panelnames.append( fac.name )
                            break
                toprint[row] = {'A':result[row-2]['time'],'B':result[row-2]['team'] + 1,'C':panelnames }
        wb = openpyxl.Workbook()
        sheet = wb.active
        print(toprint)
        for row in toprint.keys():
            for col in toprint[row].keys():
                sheet[col+str(row)] = str(toprint[row][col])
        wb.save(filename=filename)

with open('teamcount.json') as f:
    teamcount = int( json.load(f) )

with open('faculty.json') as f:
    facultycount = len(dict(json.load(f)))

with open('timeperteam.json') as f:
    timeperteam = int( json.load(f))

Faculties = []
for i in range(1,facultycount+1):
     Faculties.append( Faculty(id=i) )

with open('allocatable.json') as f:
    allocatable = list( json.load(f)["allocatable"])

community = Community(id=['S8 CSB'],allocatable=allocatable,strtdt =Date(date = fetch("startdate")))

Teams = []
for id in range( teamcount ):
    Teams.append(Team(id = id) )

panel = Panel( distinctcount = fetch("paneldistinctcount") ,isguidepresent = fetch("isguidepresent"),iscoordinatorpresent = fetch("iscoordinatorpresent")   )

exclusion = Exclusion(count = int( fetch("exclusioncount") ))
# for i in range(exclusion.count):
#     exclusion.add( date = Date(fetch("date")), period = fetch("period"),type = fetch("type") ,id = fetch("id") )
# exclusion.add( date = Date('2020-02-10').self, period = 5,type = 'period')

result = []
allocate = ''
for iteration in range(1):
    allocate = Allocate(strtdt=Date(date=fetch("startdate")), panel=panel, faculty=Faculties, team=Teams,
                        community=community.__copy__(), exclusion=exclusion, timeperteam=timeperteam)
    res = allocate.run(iteration)
    result.append(res)
result.sort()
allocate.print_output(result = result[0][2] , filename= "output100.xlsx")

