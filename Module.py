# Random Module
# Random Module is used to access random values at runtime
import random
# random() - This is used to print the values in between 0 and 1
# print(random.random())
# randint(a,b) - This is used to print the random values between a and b
# print(random.randint(1000, 9999))
# randrange() - Same as randint but will never return endpoint
# print(random.randrange(2, 10))
# uniform() - Used for returning float random values
# print(random.uniform(2.5, 3.4))
# choice() - This is used to extract a character from string or element from a list
# n = "Nitish"
# print(random.choice(n))
# n = [1,2,3,4,5,6,7,8,9]
# print(random.choices(n, k=3))

# ls = [1,2,3,4,5,6,7,8]
# random.shuffle(ls)
# print(ls)

# Q1. Generate a otp of 8 digit
# Q2. Generate a 4 digit password 1 symbols, 1 lowercase, 1 uppercase, 1 digit
# Q3. Store 100 random number in a list unique 10 digit number
# Q4. 10-1000 print random number divisible by 5

# Q1
print(random.randint(10000000, 99999999))

# Q2
print()
print("Password Generator")
al = "abcdefghijklmnopqrstuvwxyz"
sym = "!@#$%^&*?"
password = str(random.randint(1,9)) + random.choice(al)+random.choice(sym)+random.choice(al.upper())
print(password)
