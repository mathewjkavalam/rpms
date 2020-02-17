faculty =[
    { "coordinator":['team1','team2','team3'],"guide":['team1','team2','team3'], "area":["ML","AI","NLP"], "called":"2","exclude":[] },
    { "coordinator":[],"guide":['team1','team2','team3'], "area":["ML","AI","NLP"], "called":"2" ,"exclude":[{"date":"13-2-2020","hour":"3"}]},
    { "coordinator":[],"guide":['team1','team2','team3'], "area":["ML","AI","NLP"], "called":"2" ,"exclude":[{"date":"13-2-2020","hour":"3"}]},
    { "coordinator":[],"guide":['team1','team2','team3'], "area":["ML","AI","NLP"], "called":"2" ,"exclude":[{"date":"13-2-2020","hour":"3"}]},
    { "coordinator":[],"guide":['team1','team2','team3'], "area":["ML","AI","NLP"], "called":"2" ,"exclude":[{"date":"13-2-2020","hour":"3"}]}
]

team =[
    {"index":"1","start":"13-2-2010","panel":{"guide":"True","coordinator":"True","distinct":"2"},"exclude":[{"date":"13-2-2020","hour":"3"}] },
    {"index":"2","start":"13-2-2015","panel":{"guide":"True","coordinator":"True","distinct":"2"},"exclude":[]},
    {"index":"3","start":"13-2-2020","panel":{"guide":"True","coordinator":"True","distinct":"2"},"exclude":[] }
]

def before_date( aDate,bDate ):
    if bDate >= aDate:
        return True
    else:
        return False

def min_start_date(team):
    from datetime import datetime
    start_dates = []
    for t in team:
        start_dates.append( datetime.strptime(t["start"] , '%d-%m-%Y')  )
    return min(start_dates)

def before(t,date):
    from datetime import datetime
    if before_date(datetime.strptime(t, '%d-%m-%Y'), date):
        print( t )
