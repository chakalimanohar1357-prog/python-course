# # 1. Creating a dictionary
# student = {"name": "kanna", "age": 20, "age": 21}
# print(student)

# # 2. Accessing values using key
# print(student["name"])

# # 3. Accessing values safely with get()
# print(student.get("name"))
# print(student.get("city"))  # returns None if key does not exist

# # 4. Accessing a missing key directly raises an error
# # print(student["city"])  # Uncomment to see the error

# # 5. Updating values
# student = {"name": "kanna", "age": 20, "age": 21}
# student["age"] = 23
# student["city"] = "Hyderabad"
# print(student)

# # 6. Deleting a key using del
# student = {"name": "kanna", "age": 20, "age": 21}
# student["age"] = 23
# student["city"] = "Hyderabad"
# del student["name"]
# print(student)

# # 7. Deleting a key using pop()
# student = {"name": "kanna", "age": 20, "age": 21}
# student["age"] = 23
# student["city"] = "Hyderabad"
# student.pop("city")
# print(student)

# # 8. Getting all keys
# student = {"name": "kanna", "age": 22}
# print(student.keys())

# # 9. Getting all values
# student = {"name": "kanna", "age": 20}
# print(student.values())

# # 10. Iterating over keys
# student = {"name": "kanna", "age": 20}
# for k in student:
#     print(k)

# # 11. Iterating over keys and values
# student = {"name": "kanna", "age": 20}
# for k, v in student.items():
#     print(k, v)

# # 12. Taking input and storing in a dictionary
# n = int(input("Enter number of students: "))
# m = {}
# for i in range(n):
#     name = input("Enter name: ")
#     age = input("Enter age: ")
#     m[name] = age
# print(m)
