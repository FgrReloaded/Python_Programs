# Find a word from a string and print it's index

word = input("Enter a word: ")
srch = input("Enter a word or letter to search")

for i in range(len(word)):
    if word.startswith(srch, i):
        print(i)
        
