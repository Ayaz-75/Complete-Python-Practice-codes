


#write a proram that print out the numbers from 1 to 100
#if number is divisible by 3 it shoud print "Fizz" insted of Number
#if number is divisible by 5 it shoud print "buzz" insted of Number
#if number is divisible by both 3 and 5, it shoud print "FizzBuzz" insted of Number



for i in range(1,101):
    if i%3==0 and i%5==0:
        i="FizzBuzz"
    elif i%3==0:
        i="Fizz"
    elif i%5==0:
        i="Buzz"
    else:
        i=i
    print(i)