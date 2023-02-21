n = int(input("Enter a number: "))
x = n
y = n
rev = 0

while y>0:
    rev = rev*10 + y%10
    y //= 10

print(rev)    
    