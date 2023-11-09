age = int(input("Enter your age: "))


# if age >= 18:
#     print("You can enter")
# else:
#     print("You're young")

# let answer = 5 > 0 ? "correct" : "incorrect"  JS syntax

print("You can enter") if age >= 18 else print("You're young")

message = "Yes" if age > 18 else ("Maybe" if age == 18 else "No")
print(message)



