


def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mult(n1,n2):
    return (n1*n2)

def div(n1,n2):
    return(n1*n2)


opeations={
 "+":add,
 "-":sub,
 "*":mult,
 "/":div  
}


should_continue=True

while should_continue:
    first_number=int(input("Enter the fisrt number: "))

    for symbol in opeations:
        print(symbol)
    operation_symbol=input("Pick any operation given above: ")

    second_number=int(input("Enter the second number: "))

    
    calculation_function=opeations[operation_symbol]
    first_answer=calculation_function(first_number,second_number)

    print(f"{first_number} {operation_symbol} {second_number} ={first_answer}")


    choice=input("Do you want to continue or not yes to continue and not to end")
    if choice=="yes":
        should_continue=True
    else:
        should_continue=False
        print("Goodbye")
    operation_symbol=input("Pick another operation: ")
    num3=int(input("What's the next number"))
    calculation_function=opeations[operation_symbol]
    answer=calculation_function(calculation_function(first_number,second_number),num3)
    print(f"{first_answer} {operation_symbol} {num3}={answer}")