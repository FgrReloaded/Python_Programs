r=int(input("Enter rows: "))
c=int(input("Enter Col: "))
ls = []
for i in range(r):
      ls1=[]
      for j in range(c):
          a=int(input())
          ls1.append(a)
      ls.append(ls1)
'''
Main Diagonal
for i in range(r):
    for j in range(c):
        if i==j:
            print(ls[i][j])
        else:
            print(" "*2, end="")
    print()
'''
'''
Upper Triangle
for i in range(r):
    for j in range(c):
        if i+j < r:
            print(ls[i][j], end="")
    print()
'''
'''
Lower Triangle
for i in range(r):
    for j in range(c):
        if i+j >= r-1:
            print(ls[i][j], end="")
        else:
            print(" ", end="")
    print()
'''
'''
Anti Diagonal
for i in range(r):
    for j in range(c):
        if i+j==r-1:
            print(ls[i][j])
        else:
            print(" "*2, end="")
    print()
'''
'''
Zig Zag
for i in range(r):
    if i%2==0:
        for j in range(c):
            print(ls[i][j],end="")
    else:
        for j in range(c-1,-1,-1):
            print(ls[i][j],end="")
    print()
'''
'''
Boundary Of Matrix
for i in range(r):
    for j in range(c):
        if i==0 or j==0 or i == r-1 or j==r-1:
            print(ls[i][j],end="")
        else:
            print(" ", end="")
    print()
'''


