number = int(input("Enter a first number: "))
number_2 = int(input("Enter a second number: "))

if number > number_2:
    print("num_1", number)
else:
    print("num_2", number_2)

print("num_1", number) if number > number_2 else print("num_2", number_2)
