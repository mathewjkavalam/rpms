def min_start_date(team):
    from datetime import datetime
    start_dates = []
    for t in team:
        start_dates.append( datetime.strptime(t["start"] , '%d-%m-%Y')  )
    return min( start_dates ).date()

