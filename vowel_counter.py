vowel_counter = input("input a sentence: ").lower()
vowels = 0
for i in vowel_counter:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i== 'u'):
        vowels = vowels + 1
        
print(vowels)
        