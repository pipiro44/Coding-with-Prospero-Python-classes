
name = input("Enter a number:")

# convert every single character to int
# check if interger

numerical = []
numerals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# uche
# name.split(): ['u', 'c', 'h'], ["uche"]

for number in  name:
    if number in str(numerals):
        numerical.append(number)
    else:
        pass


if len(numerical) == 0:
    print("There are no numbers in your name")
elif len(numerical) == 1:
    print(f"The number in your name is {numerical}")
else:
    print(f"The numbers in your name are: {numerical}")
   
   

""" 
   
"""
