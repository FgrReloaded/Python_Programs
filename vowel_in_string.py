# Count and display vowels in string

word = input("Enter a string: ")
vowel = "aeiou"
count = 0
for i in word:
    if i in vowel:
        count += 1
print("There are total",count,"in string")