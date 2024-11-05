# While

# x = 0 
# while x < 5:
#     print(x)
#     x += 1 #While loopen körs när man har en condition bredvid

# x = 0 
# while x < 10:
#     print(x)
#     if x == 5:
#         break
#     x += 1 # viktigt att läga break så inte loopen fortsätter för alltid

# x = 0 
# while x < 10:
#     x += 1
#     if x % 2 == 0:
#         continue
#     print(x) # continue används för att hoppa över ojämna tal osv.

# x = 0 
# while x < 5:
#     print(x)
#     x += 1
# else:
#     print("Loopen avslutades") # else kör bara om det inte finns något break

# user_input = input("Ange ett kommando: ")
# print(user_input) # input är till för att få in vad en användare skriver

# while True: 
#     user_input = input(" ange ett kommando: ")
#     if user_input == "exit":
#         break
#     elif user_input == "5":
#         print("du skrev 5")
#         break
#     else: print("fel input, försök igen") # break för att ta dig ur loopen, input för att fråga användare.
    
## Logiska operatörer

# a = True
# b = False

# print(a and b)# för att få ut ifall båda är sanna
# print(a or b)# få ut om någon är sanna
# print(not a)# för att exkludera 

# x = 5 
# print(1 < x < 10)
# print(1 < x and x < 10)

# age = int(input("ange din ålder: ")) 
# if 18 <= age <= 65: # detta kolla chain för de kan man kolla samtidigt iställer för fler rader
#     print("Du kan jobba")
# else:
#     print("du kan inte jobba")
    
## Files ## 

# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()

# file = open("example.txt", "r")
# line = file.readline()
# while line: 
#     print(line, end='')
#     line = file.readline()
# file.close()

# file = open("example.txt", "r")
# lines = file.readlines()
# for line in lines: 
#     print(line, end='') #istället för end= ' ' så kan man köra /n fast åt andra hållet
# file.close()

# file = open("example.txt", "r")
# lines = file.read().splitlines()
# # print(lines)

# file = open("example.txt", "w")
# file.write("Exempeltext \n")
# file.write("Nästa rad")
# file.close()

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content) # with sats är bäst för man behöver inte stänga filen utan sker auto

with open("example.txt", "w") as file: 
    file.write("Exempeltext \n")
    file.write("Nästa rad")