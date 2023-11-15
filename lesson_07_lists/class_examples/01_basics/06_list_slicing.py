my_words = ["alex", 'Beni', "Inbal", "Alex", "Dan", "Tal"]

print(my_words[1:3])
print(my_words[::1])
print(my_words[::-1])
print(my_words[-1])

my_new_words = my_words

print(my_new_words)
print(id(my_words))
print(id(my_new_words))
my_different_list = my_words[:]
print(id(my_different_list))
my_words[0] = "ALEXANDER"

print(my_new_words)
print(my_different_list)


