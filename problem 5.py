'''
Complete this program to accept two integer inputs (Score1 and Score2)
If both are added together and the score is greater than 100, print "Invalid Score")
otherwise print "Score Accepted"

Part of the program has been done for you.

'''
Score1 = int(input("enter a number "))
Score2 = int(input("enter a number "))

if Score1 + Score2 > 100:
    print("invalid score")
    
else:
    print("score accepted")
    
