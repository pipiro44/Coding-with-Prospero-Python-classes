
# mini program to detect digits in names:

"""_summary_:

This simple exercise is to teach you how to handle user
inputs in Python. We also introduce some methods and data structures
which will be covered in future lessons. 

"""

name = input("Enter a number:")
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

digits = {i for i in name if i in str(num)}
#print(list(y))

if len(digits) == 0:
    print("Your name is " + name)
else:
    print("You can't include numbers in your name")



