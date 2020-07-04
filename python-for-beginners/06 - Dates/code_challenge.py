# we have to use the necessary library
from datetime import datetime, timedelta

# print today's date
print(str(datetime.now()))

# print yesterday's date
day = timedelta(days=1)
print(str(datetime.now()-day))

# ask a user to enter a date
users_date = input('Please enter a date (dd/mm/yyyy): ')
users_date_conversion = datetime.strptime(users_date, '%d/%m/%Y')

# print the date one week from the date entered
week = timedelta(weeks=1)
print(str(users_date_conversion + week))









