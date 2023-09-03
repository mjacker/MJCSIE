msg = "aaabcc"
letters = sorted(set(msg))
my_dict = {}
for letter in letters:
    my_dict[letter] = msg.count(letter)

print(my_dict)
