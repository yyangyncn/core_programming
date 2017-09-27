# Fibonacci
a, b = 0, 1
while b < 10:
    print(b, end=' ')
    a, b = b, a + b

age = int(input("The age of your dog:"))
print("")
if age < 0:
    print("r u kidding me?")
elif age == 1:
    print("equal to 14")
elif age == 2:
    print("equal to 22")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("equal to ", human)
else:
    print("age is ", age)

input("enter to quit")
