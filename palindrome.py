n = int(input("Enter a number: "))
x = n
y = n
rev = 0

while y>0:
    rev = rev*10 + y%10
    y //= 10

print("It's a Palindrome") if rev == n else print("It's not a Palindrome")
    
    