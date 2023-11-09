age = int(input("Enter your age: "))

if age > 67:
    print("pensioner")
elif age >= 18 and age < 30:
    print("You are 18 - 30")
elif age >= 30 and age < 67:
    print("You are 30 - 67")
else:
    print("You're young")
