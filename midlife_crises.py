print("----- Welcome to Rollercoaster -----")
print()
height=int(input("Enter your Height in cms: "))
bill=0
if height>=120:
    print('Can ride')
    age=int(input('Enter your age: '))
    if age<12:
        bill+=5
        photo=input('Do you want photo ?')
        if photo=='Y':
            bill+=3
        else:
            pass
        print('You have to pay:+$',bill)
    
    elif age>=12 and age<=18:
        bill+=7
        photo=input('Do you want photo ?')
        if photo=='Y':
            bill+=3
        else:
            pass
        print('You have to pay:+$',bill)
    
    elif age>18:
        bill+=12
        photo=input('Do you want photo ?')
        if photo=='Y':
            bill+=3
        else:
            pass
        print('You have to pay:+$',bill)

    elif age>=45 and age<=55:
        bill+=0
        print('You have to pay:+$',bill,'Because you are in Midlife Crises')
    
    else:
        print("an invalid Age according to the Rules")

else:
    print("Can't ride")