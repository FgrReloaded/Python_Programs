# # Q1.
# print("Question 1")
# f = open("today.txt", "r")
# x = f.read()
# print(x)

# # Q2.
# print("Question 2")
# f.seek(0)
# y = f.readline()
# print(y)
# f.close()

# # Q3
# print("Question 3")
# f = open("today.txt", "a+")
# f.write("I am appending to this file.")
# f.seek(0)
# x = f.read()
# print(x)
# f.close()

# Q4
print("Question 4")
# f = open("today.txt", "r")
# n = int(input())
# y = f.readlines()
# for i in reversed(range(len(y)-n)):
#     print(y[i])





# Q5
# print("Question 5")
# f.seek(0)
# x = f.readlines()
# print(x)
# for i in x:
#     print(i)

# Q6
# print("Question 6")
# f.seek(0)
# x = f.readlines()
# a=""
# for i in x:
#     a+=i
# print(a)

# Q7
# print("Question 7")
# # f.seek(0)
# # x = f.readlines()
# # print(x)
# # for i in x:
# #     print(i)

# # Q8
# print("Question 8")
# f.seek(0)
# x = f.read().split()
# s = len(max(x, key=len))
# for i in x:
#     if len(i) == s:
#         print(i)
#         break

# # Q9
# print("Question 9")
# f.seek(0)
# x = f.readlines()
# print(len(x))
            
            
# # Q10
# print("Question 10")
# f.seek(0)
# x = f.read().split()
# w = input("Enter word to search: ")
# print(x.count(w))

# Q11
# print("Question 11")
# f.seek(0)
# x = f.read().split()
# w = input("Enter word to search: ")
# print(x.count(w))


# Q12
# print("Question 12")
# f = open("today.txt", "w")
# ls = ["Hello", "This", "is", "Nitish"]
# for i in ls:
#     f.write(i)
# f.close()


# Q13
# print("Question 13")
# f = open("new.txt", "r")
# z = open("today.txt", "w")
# x = f.read()
# z.write(x)
# f.close()

# Q14
# print("Question 14")
f = open("new.txt", "r")
z = open("today.txt", "w+")
x = f.readlines()
y = z.readlines()
for i in range(len(x)):
    x[i] += y[i]
    z.write(x[i])


