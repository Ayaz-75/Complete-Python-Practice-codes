print("----- Welcome to the the pizza Dilevers -----")
print()
'''print('Here are the rates of Pizza, Papperoni and Extra Cheese')
print(f"small pizza=15$ \nmediam pizza=20$ \nlarge pizza=25$ \npapperoni for small pizza=2$ \npapperoni for Large pizza=3$ \nextra cheese for any pizza=1$")
print()'''
size=input("What size would you like to order ? S for Small M for mediam and L for large\n")
add_papproni=input("Do you want to add papperoni Y or N\n")
extra_cheese=input("Do you want extra cheese Y or N\n")

price=0
if size=='S':
    price+=15
    if add_papproni=='Y':
        price+=2
        if extra_cheese=='Y':
            price+=1
        else:
            pass
        print("Your total bill is:",price,"$")
        
elif size=='M':
    price+=20
    if add_papproni=='Y':
        price+=3
        if extra_cheese=='Y':
            price+=1
        else:
            pass
        print("Your total bill is:",price,"$")

elif size=='L':
    price+=25
    if add_papproni=='Y':
        price+=3
        if extra_cheese=='Y':
            price+=1
        else:
            pass
        print("Your total bill is:",price,"$")

else:
    print("Invalid Size")