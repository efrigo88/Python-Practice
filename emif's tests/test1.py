
def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


value1 = input('please enter Value 1: ')
value2 = input('please enter Value 2: ')

print('Direct concatenation looks like this: ' + value1 + value2)

if isint(value1) is True and isint(value2) is True:
    value1 = int(value1)
    value2 = int(value2)
    print('If you entered integers, I can add them, Total Sum would be: ' + str(value1 + value2))


