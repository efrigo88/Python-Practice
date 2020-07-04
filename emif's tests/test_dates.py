
# import date, to be able to work with them
from datetime import datetime
# to play with time intervals, I can add timedelta
from datetime import timedelta

today = datetime.now()
print('Today is: ' + str(today))

# stored desired amount of days
days = timedelta(days=1)

yesterday = today - days
print('Yesterday was: ' + str(yesterday))

# partition date in: day, month and year
day = str(today.day)
month = str(today.month)
year = str(today.year)

print('We can partition a date in its elements/: DAY: ' + day + ' MONTH: ' + month + ' YEAR: ' + year)

# ask for your birthday date to calculate your age
birthday_date_input = input('Please enter your Birthday Date (dd/mm/yyyy): ')
birthday_date = datetime.strptime(birthday_date_input, '%d/%m/%Y')
get_diff_d = datetime.now() - birthday_date
get_diff_y = (int(get_diff_d.days) / 365).__trunc__()

print('Yor are ' + str(get_diff_y) + ' years old.')






