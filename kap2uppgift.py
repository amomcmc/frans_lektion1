#1
# namn = " aNna kaRlSsOn "
# namn = namn.strip()
# namn = namn.title()
# namn = namn.replace(" ", "-")
# print(namn)
# Resultat: Anna-Karlsson


#2
# order_tuple = ("bröd", "mjölk", "ägg", "smör", "ost", "yoghurt")
# print(order_tuple[0:3]) #tre första
# print(order_tuple[-2:]) #två sista
# print(order_tuple[::2]) #vartannat

#3
# movie_list = ["Inception", "The Matrix", "Interstellar", "The Prestige"]
# movie_list.append("Memento")
# movie_list[1] = "The Lord of the rings"
# movie_list.remove("The Prestige")
# movie_list.insert(1, "The Dark Knight")
# print(movie_list) #MANUELLT

movie_list = ["Inception", "The Matrix", "Interstellar", "The Prestige"]
if "Memento" not in movie_list: #if sats, not in :villkor 
    movie_list.append("Memento")
    
if "The Matrix" in movie_list: #in är villkoret
    index = movie_list.index("The Matrix")
    movie_list[index] = "The Lord of the Rings"
    
if "The Prestige" in movie_list: #villkor
    movie_list.remove("The Prestige")
    
if "The Dark Knight" not in movie_list: # villkor
    movie_list.insert(1, "The Dark Knight")
    
print("Slutgiltig lista: ")
for movie in movie_list:
    print(movie_list)
    break

        
        
    
    

    










