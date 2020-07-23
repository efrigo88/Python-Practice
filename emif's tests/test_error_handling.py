# Input the values
x = 10
y = 0

# try start
try:
    print(x / y)
except ZeroDivisionError as e:
    print('You cannot divide by zero, please change the value')
    print('Error thrown: ' + str(e))
finally:
    print('This is our cleanup code')


