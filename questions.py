import random

print("Lottery System")
ls = []
while len(ls)<=100:
    ran = random.randint(1000000000, 9999999999)
    if ran not in ls:
        ls.append(ran)

print(ls)

lotter1 = random.choice(ls)
lotter2 = random.choice(ls)
while lotter1 == lotter2:
    lotter2 = random.choice(ls)

print("Lottery #1", lotter1)
print("Lottery #2", lotter2)

print()
print("Numbers divisible by 5 between 10 to 1000")
i = 1
ls2 = []
while i <= 990:
    ans = random.randint(10, 1000)
    if ans not in ls2:
        ls2.append(ans)
        if ans%5==0:
            print(ans, end=" ")
        i+=1
    
