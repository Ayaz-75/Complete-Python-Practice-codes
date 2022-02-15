



#prime number using function


def prime_checker(number):
    is_prime=True


    for i in range(2,number):
        if number%i==0:
            is_prime=False
    if is_prime:
        print(number,"is prime")
    else:
        print(number,"is Not prime")



prime_checker(number=int(input("Enter Number\n")))