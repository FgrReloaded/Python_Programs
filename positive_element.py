ls = []
size = int(input("Enter size of list: "))
for i in range(size):
    x = int(input("Enter element: "))
    ls.append(x)
print(ls)

ls2=[]
for i in ls:
    if i>0:
        ls2.append(i)
print(ls2)
