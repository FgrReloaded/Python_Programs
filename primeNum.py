n = int(input("Enter a number: "))

i = 2
while i<n:
    if n%i == 0 and i!= n:
        print("Number is not prime.")
        break        
    i+=1
if i==n:
    print("Number is prime.")