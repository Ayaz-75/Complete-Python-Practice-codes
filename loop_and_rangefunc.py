

#using for loop and range function
sum=0
print("All integers:")
for i in range(1,11):
    sum+=i
    print(i)
print("Sum of all numbers in loop is: ",sum)




#finding the even numbers in loop
print()
sum=0
print("All even number:")
for i in range(1,101):
    if i%2==0:
        sum+=i
        print(i)
print("Sum of all even numbers in rannge is: ",sum)