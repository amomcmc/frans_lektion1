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
        
        
# for i in range(1, 101):    # Loopa från 1 till 100
#     if i % 3 == 0 and i % 5 == 0:    # Om talet är delbart med både 3 och 5
#         print("FizzBuzz")
#     elif i % 3 == 0:    # Om talet är delbart med 3
#         print("Fizz")
#     elif i % 5 == 0:    # Om talet är delbart med 5
#         print("Buzz")
#     else:
#         print(i)    # Om inget av ovanstående gäller, skriv ut talet självt

    
        
