# Find a word from a string and print it's index

word = input("Enter a word: ")
srch = input("Enter a word or letter to search: ")

# Method 1 (For Letters and word both)

for i in range(len(word)):
    if word.startswith(srch, i):
        print(i)

# Method 2 (For Letters only)

for i in range(len(word)):
    if word[i] == srch:
        print(i)