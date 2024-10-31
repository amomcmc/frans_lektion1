# x = 10
# if x > 5:
#     print("x is greater than 5")

# if condition1: 
    
# elif condition2: 

# else condition3:
    
# x = 17
# if x > 15:
#     print("x is greater than 15")

# elif x > 5:
#     print("x is greater than 5") # if satsen körs alltid först, om den är true körs inte elif, bara om false

# x = 3 
# if x > 15:
#     print("x is greater than 15")
# elif x > 5:
#     print("x is greater than 5")
# else:
#     print("x is less than 5") # else satsen körs när både if och elif är false

# x = 20
# if x > 10:
#     print("above 10")
# if x > 20:
#     print("and also above 20")
# else: 
#     print("but not above 20.") # här kommer else satsen efter första if satsen när den är true men hoppar över den andra if satsen för den är false

# x = 7
# y = 10
# if x > 5 and y < 15:
#     print("Both conditions are true") # and satsen körs bara när både x och y är true, annars ingenting

# x = 7
# y = 10
# if x > 5 or y < 15:
#     print("both conditions are true") # vid or så körs den satsen om någon av villkoren stämmer, båda behöver inte men båda kan också vara sanna.

# def check_a():
#     print("kontrollerar a")
#     return False 

# def check_b():
#     print("kontrollerar b")
#     return True 

# if check_a() and check_b():
#     print("båda är sanna")
# else:
#     print("minst en är falsk") # funktion som bara återkollar true eller false blandad med sats.

# results = värde_sant if villkor else värde_falskt # gör så att if satsen är mer kompakt istället för flera rader

# x = 5
# parity = "even" if x % 2 == 0 else "odd"
# print(f"Number är {parity}") # exempel på när man sätter ihop fler satser på en rad. 

# a = b = c = 10

# if a == b == c: 
#     print("alla är lika") # fortfarande exempel

# x = -3
# if x > 0:
#     print("x is positive")
# else: 
#     pass # pass är till för att få fram att strunta i den om if satsen är false

# number = input("Type a number:")

# if number.isdigit():
#     number = int(number)
#     print(f"You typed a number {number}")
# else:
#     print("Thats not a number") # frågaar användaren om ett nummer och ger ett svar beroende på vad man skrivit

# x = 5
# y = 10
# z = 15

# if (x < y and y < z) or x == z:
#     print("True") # väldigt svår att förstå så undvik, I och med att and kör inom paranteser körs den först
    
# def max_value(a, b):
#     if a > b:
#         return a
#     else:
#         return b # definerat villkor
    
# biggest = max_value(15, 1)
# print(f"The biggest value is {biggest}") # definerat en variabel 

## LOOPAR

# for variabel in iterable: # " variabel kan heta vad som helst, helst något som visar vad som letas efter

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit) # itererar alla element i listan
    #Resultatet blir:
    #apple
    #banana
    #cherry

# person = ("Alice", 30, "Stockholm")
# name, age, city = person
# print(name)
# print(age)
# print(city)

# people = [("Alice", 30, "Stockholm"), ("Bob", 25, "Götebrog"), ("Charlie", 15, "Linköpig")]
# for name, age, city in people:
#     print(f"Namn: {name}, Age: {age}, Stad: {city}") 

# person = {"name": "Alice", "age": 30, "city": "Stockholm"}
# for key, value in person.items():
#     print(f"{key}: {value}") # tuple unpacking, för att komma åt specifika värden.

# text = "Hello"
# for bokstav in text:
#     print(bokstav) # detta gör så att man får ut "Hello" i en bokstav på varje rad

##For loopen är till för att gå igenom exakt alla element.

# person = {"name": "Alice", "age": 30, "city": "Stockholm"}
# for nyckel in person:
#     print(f"{nyckel}: {person[nyckel]}") 

# person = {"name": "Alice", "age": 30, "city": "Stockholm"}
# for key in person.keys():
#     print(key) # för att bara få ut nyckel

# person = {"name": "Alice", "age": 30, "city": "Stockholm"}
# for value in person.values():
#     print(value) # för att bara få ut värde

# for siffra in range (5):
#     print(siffra)

# for siffra in range(2, 10, 2):
#     print(siffra)

# for i in range(3):
#     for j in range(2):
#         print(f"i: {i}, j: {j}") 

# for i in range(10):
#     if i == 5:
#         break
#     print(i) #break är till för att avbryta loopen vid given plats

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i) # för att se vad som har ett restvärde

# while contidion: # såhär ser syntaxen ut för en while loop

# x = 0 
# while x < 5:
#     print(x)
#     x += 1


# while True:
#     print("This is running forever")
#     break # viktigt att ha en break så inte loopen fortsätter i all oändlighet



    











    



    

