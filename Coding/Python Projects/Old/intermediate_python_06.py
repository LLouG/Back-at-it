link = "https://www.youtube.com/watch?v=8OKTAedgFYg"

enumerates = "Iterate with enumerate() instead of range(len())"

#data = [1, 2, -4, -3]
#for i in range(len(data)):
#    if data[i] < 0:
#        data[i] = 0
#print(data)

#data = [1, 2, -4, -3]
#for idx, num in enumerate(data):
#    if num < 0:
#        data[idx] = 0
#print(data)


list_comprehension = "Use list comprehension instead of raw for loops"

#squares = []
#for i in range(10):
#    squares.append(i*i)
#print(squares)

#squares = [i*i for i in range(10)]
#print(squares)


sorteds = "Sort complex iterables with sorted()"

#data = [3, 5, 1, 10, 9]
#sorted_data = sorted(data, reverse=True)
#print(sorted_data)

#data = [{"name": "Max", "age": 6},
#        {"name": "Lisa", "age": 20},
#        {"name": "Ben", "age": 9}]
#sorted_data = sorted(data, key=lambda x: x["age"])
#print(sorted_data)


unique_value_sets = "Store unique values with Sets"

#my_list = [1,2,3,4,5,6,7,7,7]
#my_set = set(my_list)
#print(my_set)

#primes = {2,3,5,7,11,17,19}
#print(primes)


generators = "Save memory with Generators"

#import sys
#my_list = [i for i in range(10000)]
#print(sum(my_list))
#print(sys.getsizeof(my_list), "bytes")

#my_gen = (i for i in range(10000))
#print(sum(my_gen))
#print(sys.getsizeof(my_gen), "bytes")


get_and_setdefault = "Define default values in Dictionaries with .get() and .setdefault()"

#my_dict = {"item": "football", "price": 10.00}
#count = my_dict.get("count", 0)
#print(count)

#count = my_dict.setdefault("count", 0)
#print(count)
#print(my_dict)


collections_counter = "Count hashable objects with collections.Counter"

#from collections import Counter
#my_list = [10,10,10,5,5,2,9,9,9,9,9,9]
#counter = Counter(my_list)
#print(counter[10])
#most_common = counter.most_common(1)
#print(most_common)


fstrings = "Format Strings with f-strings (3.6+)"

#name = "Alex"
#my_string = f"Hello {name}"
#print(my_string)

#i = 10
#print(f"{i} squared is {i*i}")


concatenate_strings = "Concatenate Strings with .join()"

#list_of_strings = ["Hello", "my", "friend"]
#my_string = " ".join(list_of_strings)
#print(my_string)


merge_dictionaries = "Merge Dictionaries with {**d1, **d2} (3.5+)"

#d1 = {"name": "Alex", "age": 25}
#d2 = {"name": "Alex", "city": "New York"}
#merged_dict = {**d1, **d2}
#print(merged_dict)

simplify_if_statement = "Simplify if-statement with if x in [a,b,c]"

#colors = ["red", "green", "blue"]
#c = "red"
#if c in colors:
#    print("is main color")