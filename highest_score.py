




#highest score in the class
#loop used to find lenght and integer form of string
students_score=input("Enter students score: ").split()
for n in range(0,len(students_score)):
    students_score[n]=int(students_score[n])
print(students_score)

#this loop is used to compare the entire list with one element
highest_score=0
for score in students_score:
    if score>highest_score:
        highest_score=score
print("Highest score in the class is: ",highest_score)