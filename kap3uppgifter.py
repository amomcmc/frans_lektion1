# Fråga 1 
for siffra in range(1, 101):
    if siffra % 3 == 0 and siffra % 5 == 0:
        print("FizzBuzz")
    elif siffra % 3 == 0:
        print("Fizz")
    elif siffra % 5 == 0:
        print("Buzz")
    else: 
        print(siffra) 
