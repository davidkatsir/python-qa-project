users = []
print(f"{users = }")

users.append("kevin")
users.append("bob")
users.append("alice")

print(f"{users = }")

del users[1]
print(f"{users = }")

rev_users = list(reversed(users))
print(f"{rev_users = }")

users.insert(1, 'melody')
print(f"{users = }")

users += ['andy', 'wanda', 'jim']
print(f"{users = }")

center_users = users[2:4]
print(f"{center_users = }")

