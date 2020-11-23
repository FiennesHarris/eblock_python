height = float(input("enter your hieght in meters: "))
weight = float(input("enter your weight in kilos: "))
final_height = height * height
bmi = float(weight / final_height)

if bmi < 18.5:
    health = "under weight"
    advice = "eat more"
    

elif bmi >= 18.5 and bmi <= 24.9:
    health = "a healthy wieght"
    advice = "continue your with your food intake and daily exercise"
    

elif bmi >= 25 and bmi <= 30:
    health = "over weight"
    advice = "eat less and exercise more"
    
elif bmi > 30:
    health = "obese"
    advice = "get help"

print(f"your bmi is {bmi} this means you are {health} you should {advice}")