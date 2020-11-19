import random

num=random.randint(1,10)
guess=int(input("Guess the number between 1-10"))

# Add the missing code here to allow the user
# to keep guessing until their guess matches the number.
while num != guess:
    if num < guess:
        guess=int(input("Guess to High"))
    elif num > guess:
        guess=int(input("Guess to Low"))
print("correct")
