
'''
Write a program that uses a for loop to counts the number of letters in a word.
Part of the progam has been done for you.

Example Output:

The word is python
There are 6 in it.

'''


word ="python"
letters = 0
print ("The word is", word)
for i in word:
    letters = letters + 1
print(f"in this word there are {letters} letters")   

