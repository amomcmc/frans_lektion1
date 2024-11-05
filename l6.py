#*args **kwargs 

#*args

# def function_name(*args):  #syntax för args
#     for arg in args:
#         print(arg)
# function_name(1,1,1,1,1,1,,1,1,1,1,1) 

# def print_info(name, *args):
#     print(f"Name: {name}")
#     for arg in args: 
#         print(arg)
# print_info("Alice", 30, "Stockholm", "Frans", 1, 15) ## args är ett bra sätt för att kunna hantera många argument i en funktion

#**kwargs

# def function_name(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# function_name(name = "Alice", age = 30, city = "Stockholm") #3 **kwargs är bra att använda när man ska hantera många listor

# def print_all(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_all(1, 2, 3, name="Alice", age=30, city="Stockholm") #kan hantera oändliga listor och mata ut exakt vad det står i alla

# def print_all(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key in kwargs.items():
#         print(key)
# print_all([1,2,3], "Alice", 39, (1,1,3))

# def sum_numbers(*args):
#     return sum(args)

# print(sum_numbers(1, 2, 3, 4)) # det här ger summan av alla argument i funktionen

# def build_profile(**kwargs):
#     return kwargs

# profile = build_profile(name="Ali", age=30, job="Stockholm")
# print(profile)

# def display_info(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# display_info(1,2,4, name="Ali", age=37, job="Göteborg")

def calculte(operation, *args, **kwargs):
    if operation == "add":
        return sum(args)
    elif operation == "subtract":
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == "divide":
        result = args[0]
        try:
            for num in args[1:]:
                result /= num
        except ZeroDivisionError:
            return "Cant divide by zero"
        return result
    else:
        return "Unknown operation"
    
print(calculte("add", 1, 2, 3, 4))
print(calculte("subtract", 10, 2, 3))
print(calculte("multiply", 2, 3, 4))
print(calculte("divide", 10, 2, 5))
print(calculte("dicide", 10, 0, 5))



        

