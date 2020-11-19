import random
num=random.randint(1,10)
attempts=0
guess=""

''' part of this code it missing.
It should ask the user to guess a number
and give them 5 attempts.
If they guess correct, it prints 'correct'
otherwise it prints 'out of attempts'
'''

while num != guess :

    guess=int(input("enter a guess"))
    attempts = attempts +1

if guess == num:
   print("correct")
else:
    print("out of attempts")
