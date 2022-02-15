#write a proram to generate a random password



#Easy Level

import random

letters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
 "s", "t", "u", "v", "w", "x", "z", "y","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R"
 ,"S","T","U","V","W","X","Y","Z"]
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=["!","@","#","$","%","^","&","*","(",")","_","+"]

print("----- Welcome to PyPassword Generator -----")
nr_letters=int(input("How many numbers you want in your password ?"))
nr_symbols=int(input("How many symbols you want in your password ?"))
nr_numbers=int(input("How many numbers you want in your password ?"))


password=""
for char in range(1,nr_letters+1):
    password+=random.choice(letters)
#print(password)
for char in range(1,nr_symbols+1):
    password+=random.choice(symbols)
#print(password)
for char in range(1,nr_numbers+1):
    password+=random.choice(numbers)

print(password)


