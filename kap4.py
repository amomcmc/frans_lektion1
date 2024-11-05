## Programmering för penetrationstestare ##

# [expression for item in iterable] ## syntax för comprehension = korta ner kod

# numbers = [1,2,3,4,5] # list comprehension
# squares = []
# for num in numbers:
#     squares.append(num ** 2)
# print(squares)

# numbers = [1,2,3,4,5]
#  squares = [num ** 2 for num in numbers]
# print(squares) ## smidigare sätt går inte snabbare men sparar plats

# numbers = [1,2,3,4,5,6,7,8,9]
# even_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
# print(even_numbers)

# numbers = [1,2,3,4,5,6,7,8,9] 
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)

# numbers = [1,2,3,4,4,5]
# unique_squares = {num ** 2 for num in numbers} #set comprehenssion
# print(unique_squares)

# fruits = ["apple", "cherry", "grape"] # dictionary comprehenssion
# fruit_lengths = {fruit: len(fruit) for fruit in fruits}
# print(fruit_lengths)

## enumerate ##

# fruits = ["apple", "cherry", "grape"]
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruits}")

# fruits = ("apple", "cherry", "grape")
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")

# matrix =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for i, row in enumerate(matrix):
#     for j, value in enumerate(row): # enumerate används för att få ut index

## zip ##

# name = ["Alice", "Bobbo", "Stefan"]
# age = [24,37,19]
# for name, age in zip(name, age):
#     print(f"Namn: {name}, Ålder: {age}") # zip gör så att man kan få ihop 2 listor samtidigt

# input("Text: ") # syntax för input

# name = input(" ange ditt namn: ")
# print(name)

## funktioner ## 

# def function_name(parametrar):
#     # kod 
#     return # syntax för funktioner

# def greet(name): 
#     return f"Hello, {name}"

# print("Test")
# print(greet("Mcmc"))

# def add(a, b):
#     return a + b

# result = add(10, 25)
# print(result)

# def greet(name="World"):
#     return f"Hello {name}"

# print(greet())
# print(greet("mcmc"))

# def add(a, b):
#     return a + b

# def add_and_square(a, b):
#     sum = add(a, b)
#     return sum * sum 

# print(add_and_square(5, 2))

## logik och funktioner ##

# def categorize_age(age):
#     if age < 13: 
#         return "Child"
#     elif age < 20: 
#         return "Teenager"
#     elif age < 65:
#         return "Adult"
#     else: 
#         return "Retiree"

# print(categorize_age(10))
# print(categorize_age(15))
# print(categorize_age(35))
# print(categorize_age(88))

# def add(a, b):
#     return a + b

# pair = (3, 5)
# result = add(*pair) # * gör så att man kan packa up tuplen
# print(result)

def make_power(exponent):
    def power(x):
        return x ** exponent
    return power

result = make_power(3)

print(result(4))





