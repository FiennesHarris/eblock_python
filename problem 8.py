
'''
If the person is over 11, they can enter the match.
If they are between 18 and 60, they pay full price
otherwise they pay a discount price.

Complete the IF statement, by putting the following missing phrases
in the correct place.

1. "You pay Discount Price"
2. "You can enter the match."
3. "You pay Full price"
4. "You cannot buy ticket."
5. "Please Enter Age"

'''

age = int (input("enter your age"))
if (age >= 11):
    print ("you can enter the match")
    if (age <= 17 or age >= 60):
        print("your price will have a discount")
    else:
        
        print("you must pay the full price")
else:
    print("you cannot buy ticket")

