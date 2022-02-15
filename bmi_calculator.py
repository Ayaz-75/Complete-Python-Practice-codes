import math
weight=float(input("Enter weight in kg: "))
height=float(input("Enter height in m: "))

bmi=weight/(height**2)
#print(math.ceil(result))
print(round(bmi,3))