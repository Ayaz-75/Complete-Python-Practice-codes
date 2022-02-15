
weight=float(input("Enter your weight: "))
height=float(input("Enter your height: "))

bmi=(weight)/height**2
print(round(bmi,2))



if bmi<=18.5:
    print("under weight")
elif bmi>18.5 and bmi<=25:
    print("Normal weight")
elif bmi>25 and bmi<30:
    print("overweight")
elif bmi >=30 and bmi<35:
    print("Obese")
else:
    print("Clinikly obesed")