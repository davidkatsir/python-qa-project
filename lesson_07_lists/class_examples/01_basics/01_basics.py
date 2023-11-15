my_list = ["a", "b", "c"]
my_list_2 = [5, 10, 15, 20, 20, 20]

print(my_list)
print(id(my_list))
print(my_list_2)
print(type(my_list))

print(my_list_2[0])
print(my_list_2[1])
print(my_list_2[-1])
# print(my_list_2[56])  # IndexError: list index out of range

my_list[1] = "Apple"
print(my_list)
print(id(my_list))
