# 1. Basic syntax for a dictionary, accessing values
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
print("Apple quantity:", my_dict["apple"])  # Accessing value

shoes_catalogue = [{"name": "NIKE", "price": "1000"}, {"name": "ASICS", "price": "2000"}]
print("Shoes are: ", shoes_catalogue)


# 2. Create an empty dict and add key
empty_dict = {}
empty_dict["orange"] = 4
print("Empty dict after adding orange:", empty_dict)

# 3. .update() and | operator
another_dict = {"pear": 6, "grape": 10}
my_dict.update(another_dict)  # Using .update()
print("My dict after update:", my_dict)

# Using | operator (Python 3.9+)
combined_dict = my_dict | {"melon": 8}
print("Combined dict with | operator:", combined_dict)

# 4. Write over values
my_dict["banana"] = 7  # Overwriting value
print("My dict after overwriting banana:", my_dict)


# 5. .get()
pear_quantity = my_dict.get("pear")
print("Pear quantity:", pear_quantity)

# Get with default value
kiwi_quantity = my_dict.get("kiwi", 0)
print("Kiwi quantity (with default):", kiwi_quantity)

# 6. .pop()
popped_item = my_dict.pop("cherry")
print("Popped item (cherry):", popped_item)
print("My dict after popping cherry:", my_dict)

# 7. .keys(), .values(), .items() loop through
print("Keys in my_dict:")
for key in my_dict.keys():
    print(key)

print("Values in my_dict:")
for value in my_dict.values():
    print(value)

print("Items in my_dict:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

"""
1. Basic syntax for a dictionary, accessing values
2. Create an empty dict and add key
3. .update() ( | )
4. Write over values
5. .get()
6. .pop()
7. .keys(), .values(), .items() loop through
"""
