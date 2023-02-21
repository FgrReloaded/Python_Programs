# Pattern 1
# *
# **
# ***
# ****
print("Pattern #1")
i = 1
while i<=4:
    print("*"*i)
    i += 1

# Pattern 2
# ****
# ***
# **
# *
print("Pattern #2")
i = 4
while i>=1:
    print("*"*i)
    i -= 1

# Pattern 3
#    *
#   **
#  ***
# ****
print("Pattern #3")
i = 1
while i<=4:
    print(" "*(4-i), "*"*i)
    i += 1

# Pattern 4
# ****
#  ***
#   **
#    *
print("Pattern #4")
i = 4
while i>=1:
    print(" "*(4-i), "*"*i)
    i -= 1

# Pattern 5
#    *
#   * *
#  * * *
# * * * *
print("Pattern #5")
i = 1
while i<=4:
    print(" "*(4-i), "* "*i)
    i += 1

# Pattern 6
# * * * *
#  * * *
#   * *
#    *
print("Pattern #6")
i = 4
while i>=1:
    print(" "*(4-i), "* "*i)
    i -= 1


# Pattern 7
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *

print("Pattern #7")
i = 1
while i<=3:
    print(" "*(4-i), "* "*i)
    i += 1

i = 4
while i>=1:
    print(" "*(4-i), "* "*i)
    i -= 1

# Pattern 8
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# **      **
# ***    ***
# ****  ****
# **********

print("Pattern #8")
n = int(input("Enter a number: "))
i = 5
while(i>=1):
    print("*"*i+" "*(n-i)*2+"*"*i)
    i-=1
i=1
while(i<=n):
    print("*"*i+" "*(n-i)*2+"*"*i)
    i+=1