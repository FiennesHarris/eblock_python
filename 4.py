
'''

Write a program that uses a while loop.
It will keep asking the user to guess the programming language.
until they type python.

Example output:
what language is this? java
what language is this? c++
what language is this? python
correct

'''

guess = input("what programming language is this")

while guess != "python":
    guess = input("what programming language is this")
    
print("correct this is python")


   

    
