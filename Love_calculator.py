print('----- Welcome to the Love Calculator -----')
name1 = input("What is your name: \n")
name2 = input("What is their name: \n")
name1.lower()
name2.lower()
combined_name = (name1 + name2)
'''a='true'
b='love'
'''
a = combined_name.count('t')
b = combined_name.count('r')
c = combined_name.count('u')
d = combined_name.count('e')

tru = (a + b + c + d)

a = combined_name.count('l')
b = combined_name.count('o')
c = combined_name.count('v')
d = combined_name.count('e')

love = (a + b + c + d)

print('Your love score is: ', tru, love)
