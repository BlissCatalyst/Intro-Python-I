"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

args = sys.argv
currentdate = datetime.today().timetuple()
year = 0
month = 0

if len(args) == 1:  # Assumes current month/year if no month and year argv's are given
    month = currentdate.tm_mon
    year = currentdate.tm_year
    print("\nIf you would like to specify a different month than the current one:\n - Add a month number (1-12) as the first argument,\n - Add a year number (four digits) as the second.\nIf you only put a month, this program asssumes you mean the current year.")
    print()
elif len(args) == 2:  # If one argument is given, it assumes it is the month and assigns year to current year
    month = int(args[1])
    year = currentdate.tm_year
else:
    month = int(args[1])
    year = int(args[2])

calendar.setfirstweekday(calendar.SUNDAY)

calendar.prmonth(year, month)
