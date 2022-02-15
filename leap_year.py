year=int(input("Enter year to be checked: "))
if year % 4==0:
    print("Leap year")
elif year % 400==0:
    print("Leap year")
else:
    print("Not a leap year")