# To Reverse a string using loop

word = input("Enter a string: ")
for i in range(0, len(word)):
    print(word[len(word)-1-i], end="")