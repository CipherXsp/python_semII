# Python program to perform various operations on sets


    # 1. Create and access set elements

print("1. Creating and accessing set elements:")
my_set = {10, 20, 30, 40, 50}
print(f"Original set: {my_set}")
print("Accessing elements (sets are unordered, so iterate):")
for element in my_set:
 print(f"Element: {element}")
 print()

    # 2. Union of the elements

print("2. Union of sets:")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {union_set}")
print()

    # 3. Intersection of the elements

print("3. Intersection of sets:")
intersection_set = set1.intersection(set2)
print(f"Intersection: {intersection_set}")
print()

    # 4. Difference of the elements

print("4. Difference of sets:")
diff_set1 = set1.difference(set2)
diff_set2 = set2.difference(set1)
print(f"Set1 - Set2: {diff_set1}")
print(f"Set2 - Set1: {diff_set2}")