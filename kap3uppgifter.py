# Fråga 1 
for siffra in range(1, 101): # här körs loopen
    if siffra % 3 == 0 and siffra % 5 == 0: # letar först efter om siffra är delbar med både 3 och 
        print("FizzBuzz")
    elif siffra % 3 == 0: # om inte siffra är delbar med båda, leta efter siffror som är delbara med 3
        print("Fizz")
    elif siffra % 5 == 0: # letar efter siffror som är delbara med 5
        print("Buzz")
    else: 
        print(siffra) # om allt ovanstående är False körs denna print ut som bara skriver ut en siffra
