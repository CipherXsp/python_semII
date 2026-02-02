# Dictionary Operations in Python

# 1. Create and access dictionary elements
print("1. Create and access dictionary elements:")
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print("Created dictionary:", student)
print("Accessing 'name':", student["name"])
print("Accessing 'age':", student["age"])
print()

# 2. Update dictionary
print("2. Update dictionary:")
student["age"] = 21
student["subject"] = "Math"
print("Updated dictionary:", student)
print()

# 3. Removing elements
print("3. Removing elements:")
removed_grade = student.pop("grade")
print("Removed 'grade':", removed_grade)
print("Dictionary after removal:", student)
del student["subject"]
print("Dictionary after deleting 'subject':", student)
print()

# 4. Merging dictionaries
print("4. Merging dictionaries:")
additional_info = {
    "city": "New York",
    "hobby": "Reading"
}
student.update(additional_info)
print("Merged dictionary:", student)
print()