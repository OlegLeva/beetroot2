from datetime import datetime
name = 'Oleg'
week = { 1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday', 5 : 'Friday', 6 : 'Saturday', 7 : 'Sunday' }
day_week_int = datetime.isoweekday(datetime.now())
print('Good day %s! on %s is a perfect day to learn some python.' %(name, week[day_week_int]))
