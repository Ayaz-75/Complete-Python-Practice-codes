



#program to find the average of heights of students
studen_height=input("Input a list of students height: ").split()


for avg in range(0,len(studen_height)):
    studen_height[avg]=int(studen_height[avg])
print(studen_height)

total_heght=sum(studen_height)
total_students=len(studen_height)

print("Average height of students is: ",(total_heght)/total_students)
