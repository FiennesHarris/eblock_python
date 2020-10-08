# Setup
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
backpack = []
food = 0
# Introduction
name = input("What is your name, adventurer?\n".title())
print("Greetings, " + name + ". Let us go on a quest!".title())
print("You find yourself on the edge of a dark forest.".title())
print("Can you find your way through?\n".title())

# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n".title())
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n".title())
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".".title())
        quit()
    else:
        print("I didn't understand that.\n".title())

# Next part of game
response = ""
while response not in directions:
    print("To your left, you see a bear.\n".title())
    print("To your right, there is more forest.\n".title())
    print("There is a rock wall directly in front of you.\n".title())
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n".title())
    if response == "left":
        print("The bear eats you. Farewell, " + name + ".".title())
        quit()
    elif response == "right":
        print("You head deeper into the forest.\n".title())
    elif response == "forward":
        print("You cannot scale the wall.\n".title())
        response = ""
    elif response == "backward":
        print("You leave the forest. Goodbye, " + name + ".".title())
        quit()
    else:
        print("I didn't understand that.\n".title())
        
# Next part of game 2
response = ""
while response not in directions:
    print("To your right, is a well.\n".title())
    print("To your left, there is even more forest.\n".title())
    print("There is a tent infront of you.\n".title())
    print("Behind you is the forest exit.\n".title())
    response = input("What direction do you move?\nleft/right/forward/backward\n".title())
    if response == "right":
        print("You stare down into the well. Farewell " + name + " you fell down!".title())
        quit()
    elif response == "left":
        print("You head even deeper into the forest.\n".title())
    elif response == "forward":
        print("You venture into the tent. 2 men see you and shoot you!\n".title())
        quit()
    elif response == "backward":
        print("You leave the forest. Goodbye, " + name + ".".title())
        quit()
    else:
        print("I didn't understand that.\n".title())
        
response = ""
while response not in yes_no:
    response = input("As you continue exploring the forest the day comes to an end. but you catch a glimpse of a strange cave do you enter. do \nyes/no\ ".title())
    if response == "yes":
        print("You head into the cave. you fall asleep, safe and warm\n".title())
    elif response == "no":
        print("the night becomes dark and cold. you have no shelter and the coldness eats you up. you die of hypothermia. Goodbye " + name + "!".title())
        quit()
    else:
        print("I didn't understand that.\n".title())
        

response = ""
while response not in yes_no:
    response = input("You wake up, ready to start the day exploring the forest. Outside the cave is some red berries, do you eat them? do \nyes/no\ ".title())
    if response == "yes":
        print("The strawberries made a lovely breakfast\n".title())
        food = food + 1
        print(f"beware your hunger level is {food}. if it reaches 0 you die! ps. you're lucky you had those berries\n".title())
    elif response == "no":
        print("You didnt have breakfast and die of hunger while walking around the path. farewell " + name + "!".title())
        quit()
    else:
        print("I didn't understand that.\n".title())
        
# Next part of game 3
print("Deeper in the cave is a dead body.\n hes holding a bag in his left hand. \n".title())
shake_bag = input("do you search is bag?: yes/no ".title())
if shake_bag == "yes":
    print("his bag has a lock on it. the code = the rgb code to make white")
    lock = int(input("what is the code?:"))
               
    if lock == 225225225:
        print("in his bag you find a hunting knife and put in your backpack \n".title())
        backpack.append("knife")
        print(f" in your backpack you now have a {backpack[0]}.\n".title())
        
                
               
    else:
         print("wrong code, you do not open his bag and you continue your day.\n".title())
           
               
 
    
elif shake_bag == "no":
    print("you walk past the body, ignoring it and continue your day.\n".title())

#next part of game 4

response = ""
while response not in yes_no:
    response = input("As the day closes you see a small stream, which could be contaminated with dead animals. do you take the risk and drink it? do \nyes/no\ ".title())
    if response == "yes":
        print("the water was clean, luckily. You are now not hungry and can survive till the next day!\n".title())
        food = food + 1
        print(f"beware your hunger level is {food}. if it reaches 0 you die!\n".title())
    elif response == "no":
        print("you die over night from hunger!\n".title())
        food = food -1
        print(f"your hunger reached {food} meaning you die! farewell {name}!".title())
        quit()
    else:
        print("I didn't understand that.\n".title())
        
print("good night adventurer see you in the morning.\n".title())
print("wake up wake up! a hungry bear has entered your cave! you must kill him! \n".title())

response = ""
while response not in yes_no:
    response  = input("do you take a chance and stand still hoping the bear doesnt see you? or do you kill him? do yes / no ")
    if response == "yes":
        print(" you look in your backpack for a knife is there one there?\n".title())
        print(f"in your backpack there is a :{backpack}".title())
        if "knife" in backpack:
            print("you kill the bear with the knife. stabbing it into his tough fur. phew!\n".title())
        if "knife" not in backpack:
            print(f"you should have taken the knife from the dead body. the bear savages you! good by {name}!".title())
            quit()
    elif response == "no":
        print(f"the bear sniffs you out. you are dead meat. farewell {name}".title())
        quit()
    else:
        print("i didnt quite get that please input yes or no again.\n".title())
        
response = ""
while response not in yes_no:
    response = input("After killing the bear you are exhausted. you wish you were out of the forest back at home. do you sleep in the cave tonight? or do you keep trying to find your way out? do \nyes for trying to find your way out and /no for sleeping in the cave\ ".title())
    if response == "yes":
        print("you pick up your backpack and go in search of civilisation\n".title())
    elif response == "no":
        print("the night becomes dark and cold. But you sleep tight. TOO TIGHT. a tiger smells you out and eats you alive in your sleep Goodbye " + name + "!".title())
        quit()
    else:
        print("I didn't understand that.\n".title())
        
print("All night you spent trecking your way out of the forest\n")
print("and finally you escape and reach a small village bordering the forest.\n")
print(f"congrats {name} you escaped the forest. GAME OVER!\n")
quit()
    



