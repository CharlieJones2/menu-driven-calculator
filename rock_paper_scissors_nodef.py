print('1. addition')
print('2. subtraction')
print('3. multiplication')
print('4. division')
print('5. quit')

opt_flag = True
while opt_flag:
    try:
        opt = int(input('choose a calculation type (1-5): '))
    except ValueError:
        opt = 0

    if opt == 0 or opt > 5:
        print('error! please enter a number from 1-5')

    if opt == 1:
        one_flag = True
        while one_flag:
            try:
                n1 = float(input('enter the first number: '))
                n2 = float(input('enter the second number: '))
                print(f'{n1} - {n2} = {n1 - n2}')
                one_flag = False
            except ValueError:
                print('error! please enter a valid number')

    elif opt == 2:
        two_flag = True
        while two_flag:
            try:
                n1 = float(input('enter the first number: '))
                n2 = float(input('enter the second number: '))
                print(f'{n1} - {n2} = {n1 - n2}')
                two_flag = False
            except ValueError:
                print('error! please enter a valid number')

    elif opt == 3:
        three_flag = True
        while three_flag:
            try:
                n1 = float(input('enter the first number: '))
                n2 = float(input('enter the second number: '))
                print(f'{n1} * {n2} = {n1 * n2}')
                three_flag = False
            except ValueError:
                print('error! please enter a valid number')

    elif opt == 4:
        four_flag = True
        while four_flag:
            try:
                n1 = float(input('enter the first number: '))
                n2 = float(input('enter the second number: '))
                print(f'{n1} / {n2} = {n1 / n2}')
                four_flag = False
            except ValueError:
                print('error! please enter a valid number')

    elif opt == 5:
        quit_flag = True
        while quit_flag:
            qt = input('would you like to quit? ')
            if qt == 'yes':
                opt_flag = False
                quit_flag = False
            elif qt == 'no':
                print('resuming calculations')
                quitFlag = False
            else:
                print('error! please enter "yes" or "no"')

print('done')
