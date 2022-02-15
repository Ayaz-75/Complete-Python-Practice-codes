


import math
#Calculating the area using Function


def calc_area(height,width,coverage):
    area=math.ceil(((height*width)/coverage))
    return area
#math.ceil is used to Round the answer to the nearest greater value than the answer


print(calc_area(height=int(input("Enter Height: ")),width=int(input("Enter Width: ")),
coverage=int(input("Enter Coverage: "))))
