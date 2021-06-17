#Given a sentance provided by the user, 
# print all the vowels from a sentence provided by the users

sentence = input("Enter a sentence")

for vowel in sentence:
    if vowel in "aeiou":
        print(vowel)
