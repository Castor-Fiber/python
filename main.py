
import student_info as si
import cabinet_info as cab


def option():
    print("\nMonitoring")
    ch = int(input('Input you want to do: \n \
    1: Find student ID by second name \n \
    2: View place info \n \
    3: Exit\n \
    Your choice is: '))

    if ch == 1:
        Surn = str(input("Input second name: "))
        if Surn in si.s_card['Second name']:
            index = si.s_card['Second name'].index(Surn)
        print(f"{si.s_card['ID'][index]}, {si.s_card['First name'][index]},{si.s_card['Second name'][index]}\n,{si.s_card['Date of birth'][index]}, {si.s_card['Perfomance'][index]}")
        print('\nSomething else? Y or N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()

    elif ch == 2:
        c = input('Input student ID: ')
        if c in cab.card['ID']:
            index = cab.card['ID'].index(c)
            print(f" Is present - {cab.card['Subject'][index]}\n\, place number - {cab.card['Place number'][index]}, is {cab.card['Row'][index]}, place - {cab.card['Place type'][index]}, First name: {si.s_card['First name'][index]}, Second name - {si.s_card['Second name'][index]}, perfomane is: {si.s_card['Perfomance'][index]}")
            print('\nSomething else? Y или N: ')
            num = input()
            if num == 'Y' or 'y' or 'У' or 'у':
                option()
            exit()
    else:
        print('Try again...')
    exit()


option()
