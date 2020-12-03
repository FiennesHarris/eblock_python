foods = ["ice cream", "pizza", "yogurt", "sweets"]
place = 0
more = " "
less = " "
while more != "n":
    add = input(f"\nwhich food items would you like to add to {foods}?: ")
    foods.append(add)
    more = input("would you like to add anymore items?: do (y/n) ").lower()

while less != "n":
    delete = input(f"\nwhich food items would you like to remove from {foods}?: ")
    while delete not in foods:
        print("sorry your request does not appear to be in your food list. Please try again")
        delete = input(f"\nwhich food items would you like to remove from {foods}?: ")
    foods.remove(delete)
    
    less = input("would you like to remove anymore items?: do (y/n) ").lower()
    


for i in foods:
    place += 1
    print(f"\n{i} is comes {place} in the list")