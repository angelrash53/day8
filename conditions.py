age = 48
print(age)
if age > 40:
    print ("You are eligible for vaccination")
elif age == 40:
    print("Wait for your birthday")
else:
    print("You are too young to be vaccinated")


numbers = [207, 106, 86, 45]
for x in numbers:
    if x % 2 == 0:
        print(str(x) + "is even")
    else:
        print(str(x) + "is odd")
        