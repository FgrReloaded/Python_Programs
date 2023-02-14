pi = 3.14

r = float(input("Enter radius: "))
print("Area of circle = ", pi*r*r)

# Volume of Sphere

r = float(input("Enter radius: "))

print("Volume of Sphere = ", (4//3)*pi*r**3)

# Area of Triangle
b = float(input("Enter base: "))
h = float(input("Enter height: "))
t = b*h*1/2
print("Area of triange: ", t)

# Celsius to Farenhite
c = float(input("Enter Celsius: "))
f = (c*9/5) + 32
print("Farenhite = ", f)

# Metre to Km
m = float(input("Enter distance: "))
km = m/1000
print(m, "m in km = ", km)

# BMI
w = float(input("Enter weight in kg: "))
h = float(input("Enter height in cm: "))
bmi = w*10000/(h*h)
print("BMI = ", bmi)

# Cricket
over = int(input("Enter overs: "))
totalRun = 33*(over - 1)+ 36
print(totalRun)

# Rabbit and Chicken
head = int(input("Enter heads: "))
legs = int(input("Enter legs: "))
x = (legs - 2*head)/2
y = head - x
print(f"Rabbit = {x} Chicken = {y}")




