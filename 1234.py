a= ''
a = a.upper()
while a.upper() != 'HELLO':
    a = input('Hello\n')
    if a.upper() == 'HELLO':
        a = input('WHAT`S UP?\n')
        if a.upper() == 'GOOD':
            print('Bye')
            break
        elif a.upper() != 'GOOD':
            a = input("Why?")
            break