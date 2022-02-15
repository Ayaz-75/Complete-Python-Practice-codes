

#randomly selected any person by computer from your friends, who is going to buy meal
#without using choice() function

import random
names_string=input("Give me everybody's name seperated by comma: ")
names=names_string.split(",")



names_length=len(names)
random_chosen=random.randint(0,names_length-1)



person_who_will_pay=names[random_chosen]
print(person_who_will_pay,"Will buy meal tonight")