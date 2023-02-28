# To Check Whether the string is palindrome or not (Using Slicing)

word = input("Enter a string: ")
if word == word[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")