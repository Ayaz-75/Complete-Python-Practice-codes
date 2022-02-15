



def my_function(f_name,l_name):
    if f_name==" " or l_name==" ":
        return "You did not provided any value"

    formatedf_name=f_name.title()
    formatedl_name=l_name.title()

    return f"{formatedf_name} {formatedl_name}"


print(my_function (input("Enter first name: "),input("Enter last name: ")))