name1 = "Alex"
name2 = "Alex"
name3 = "alex"

print(id(name1))
print(id(name2))
print(id(name3))
print(name1 is name2)
print(name1 is name3)
print(name1 is not name3)
print("--------------------")
print(name1.lower() is name3.lower())
print(name1.upper() is name3.upper())

