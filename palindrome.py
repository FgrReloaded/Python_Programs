n = int(input("Enter a number: "))
x = n
y = n
size = 0
rev = 0

while(x > 0):
    x //= 10
    size += 1

while y>0:
    rev = rev*10 + y%10
    y //= 10

print("It's a Palindrome") if rev == n else print("It's not a Palindrome")
    
    