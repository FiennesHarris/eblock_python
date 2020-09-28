import random

a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)
print(f"the 3 numbers are: {a}, {b} and {c}")

if a == b and a == c:
    tatal = a + b + c
    
    
elif a == b:
    total = a + b - c
    
    
elif a == c:
    total = a + c - b
    
    
elif b == c:
    total = b + c - a
    
    
else:
    total = 0
    
print(f"the total is {total}")