




#sum of all elements of a list



def sum_of_ele():
    a=[8,2,3,0,7]
    sum=0
    for i in range(0,len(a)):
       sum+=a[i]
    return(sum)

print(sum_of_ele())