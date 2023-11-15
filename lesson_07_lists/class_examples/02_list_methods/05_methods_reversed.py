my_words = ["alex", 'Beni', "Inbal", "Alex", "Dan", "Tal"]

my_new_list = my_words.reverse()

print(my_words)
print(my_new_list)

my_words = ["alex", 'Beni', "Inbal", "Alex", "Dan", "Tal"]
my_reversed = reversed(my_words)
print(my_reversed)
print(type(my_reversed))

my_reversed_list = tuple(my_reversed)
print(my_reversed_list)
print(list(my_reversed_list))
