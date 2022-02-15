




def my_function():
    result=3*4
    return result

print("Result is:",my_function())



def my_name(first_name,last_name):
    #result=first_name + last_name
    #return result

    formated_name=(first_name.title())
    formated_last_name=(last_name.title())
    return(f"{formated_name} {formated_last_name}")

print(my_name("aAyZ","laKhO")) 