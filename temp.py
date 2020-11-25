temp = float(input("enter the temperature: "))
which = input("do you want to convert this temperature from Fahrenheit to Celsius or from Celsius to Fahrenheit? do 'cel' to convert to celsius and 'fah' to convert to fahrenheit ")

if which == 'cel':
    cel_temp = (temp - 32) / 1.8
    print(f"{temp} fahrenheit equals {cel_temp} celsuis")
    
elif which == 'fah':
    fah_temp = (temp * 9/5) + 32
    print(f"{temp} celsius equals {fah_temp} fahrenheit")
    
