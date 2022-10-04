
16

# starting number
# error
#increment
# tolerance
number = int(input())

starting = 0
error_tolerance = 0.001

while number - abs(starting**2) >= error_tolerance:

    error= number - starting**2
    print(f"error ...............{error}")
    learning_rate = number/error
    starting = starting + learning_rate

print(f"the square root of {number} is {starting}")
