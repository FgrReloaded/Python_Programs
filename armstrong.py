n = int(input("Enter a number: "))
x = n
y = n
size = 0
sum=0

while(x > 0):
    x //= 10
    size += 1

while y>0:
    d = y%10
    sum += d**size
    y //= 10

print("It's an armstrong") if sum == n else print("It's not an armstrong")
    
    