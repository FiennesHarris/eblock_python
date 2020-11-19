'''
Add a for loop that will repeat the number of times
the user enters.
It should print out the word "loop" and the loop number each time.
Example output: (Note, it should not show loop '0')

enter times: 5
loop  1
loop  2
loop  3
loop  4
loop  5

'''

x = int(input("enter times: "))
for i in range (1,x+1):
    print(f"loop {i}")


