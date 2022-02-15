


#computer randomly selects any person from friends grp who is going to buy meal
#using choice() function


import random
names_string=input("Give everbody's name seperated by comma ")
names=names_string.split(",")


randomly_chosen=random.choice(names)
print(randomly_chosen)