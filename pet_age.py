pet = input("what pet do you have? ")
age = int(input("how old is your pet? "))
human_age = 0
if pet == "cat":
    if age == 1:
        human_age = 15
    elif age == 2:
        human_age = 24
    if age > 2:
        calc_age = age - 2
        for i in range(0,calc_age+1):
            yrs = i * 4
            human_age = 24 + yrs
       
        
if pet == "dog":
    if age == 1:
        human_age = 12
    elif age == 2:
        human_age = 24
    if age > 2:
        calc_age = age - 2
        for i in range(0,calc_age+1):
            yrs = i * 4
            human_age = 24 + yrs
            
print(f"your {pet}'s human age is {human_age}")
    
        
