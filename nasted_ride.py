print("-----Welcome to the rollercoaster-----")
height=int(input("Enter your height: "))

if height>=120:
    print("You can ride")
    age=int(input("Enter theyour age: "))
    if age<12:
        print("You have to pay 7$")
    else:
        print("You have to pay 10$")

else:
    print("You can not ride")