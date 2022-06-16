import calendar

cal = calendar.TextCalendar()
cal.pryear(2012) 

#Change First weekday
cal.setfirstweekday(calendar.TUESDAY)

#Print birthday month
calendar.prmonth(1999, 9)

#Locale calendar
d = calendar.LocaleTextCalendar(6,"SPANISH")
d.pryear(2012)

#is Leap - Bool operator
print(calendar.isleap(2016))
