print("----- Welcome to tip Calculator -----")
total_bill=float(input("What was the total bill ? $"))
percentage_tip=int(input("What percentage tip would you like to give ? 10, 12 or 15"))
people=int(input("How many people to split bill in ?"))

tip_per=(percentage_tip/100)*total_bill
total_tip=(total_bill+tip_per)/7
print("Each person have to pay: ",round(total_tip,2))