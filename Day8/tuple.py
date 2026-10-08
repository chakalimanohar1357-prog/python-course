# Basic operations on tuples in Python

# 1. Creating tuples
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")
mixed = (10, "hello", True)

# 2. Accessing elements
print("First element:", numbers[0])
print("Last element:", fruits[-1])

# 3. Slicing
print("Slice of numbers:", numbers[1:4])
print("Every second element:", numbers[::2])

# 4. Concatenation
print("Concatenated tuple:", numbers + fruits)

# 5. Repetition
print("Repeated tuple:", fruits * 2)

# 6. Length
print("Length of numbers:", len(numbers))

# 7. Membership
print("Is 3 in numbers?", 3 in numbers)
print("Is 'mango' in fruits?", "mango" in fruits)

# 8. Count and index
print("Count of 2 in numbers:", numbers.count(2))
print("Index of 'banana':", fruits.index("banana"))

# 9. Minimum and maximum
print("Minimum of numbers:", min(numbers))
print("Maximum of numbers:", max(numbers))

# 10. Iterating through a tuple
print("Fruits list:")
for fruit in fruits:
    print(fruit)

# 11. Unpacking a tuple
a, b, c = fruits
print("Unpacked values:", a, b, c)

# 12. Converting tuple to list and back
list_from_tuple = list(numbers)
print("List from tuple:", list_from_tuple)
print("Tuple from list:", tuple(list_from_tuple))
