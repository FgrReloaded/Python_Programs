# Reverse only word in string

sent = input("Enter a sentence: ").split(" ")

# Method 1
for i in range(0, len(sent)):
    print(sent[len(sent)-1-i], end = " ")

print()

# Method 2
sent = sent[::-1]
newWord = " ".join(sent)
print(newWord)