def my_sum(a, b, c):
	return a + b + c

values = [1, 2, 3]

print(my_sum(*values)) # unpackinng before sending it to a function


# ---

values = [1, 2, 3]

v1, v2, v3 = values # implicit *values

#

v1, *v2, v3 = [1, 2, 3, 4, 5, 6, 7]

print(v1, v2, v3)

# ---
# combined list

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = [*list1, " - test - ", *list2]
print(combined)

# ---
# passing  as a parameter

def my_sum_args(*args):
	result = 0
	for param in args:
		result += param
	return result

print(my_sum_args(10, 20, 30, 40, 50, 60))

# ---
# unpacking dictionaries

def my_dict_print(name, age, job):
	print(f'{name} is {age} years old and works as a {job}.')

mydict = {'name': 'Mike', 'age': 35, 'job': 'Programmer'}

my_dict_print(**mydict)

# ---
# combined dictionaries
dict1 = {'name': 'Mike', 'age': 35, 'job': 'Programmer'}
dict2 = {'hight': 185, 'weight': 85}
combined_dict = {**dict1, **dict2}

print(combined_dict)


