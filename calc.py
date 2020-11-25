num_1 = float(input("enter your first number: "))
num_2 = float(input("enter your second number: "))

operator = input("which arithmetic operator would you like to use on the numbers? do '/', '+', '-' and '*'")

if operator == '/':
    print(f"{num_1} divided by {num_2} equals {num_1 / num_2}")
    
elif operator == '/':
    print(f"{num_1} divided by {num_2} equals {num_1 / num_2}")
    
elif operator == '*':
    print(f"{num_1} times by {num_2} equals {num_1 * num_2}")
    
elif operator == '+':
    print(f"{num_1} plus {num_2} equals {num_1 + num_2}")
    
elif operator == '-':
    print(f"{num_1} minus {num_2} equals {num_1 - num_2}")