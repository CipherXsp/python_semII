# Python program to perform various operations on lists

    # 1. Create and access list elements

print("1. Creating and accessing list elements:")
my_list = [10, 20, 30, 40, 50]
print(f"Original list: {my_list}")
print(f"First element: {my_list[0]}")
print(f"Last element: {my_list[-1]}")
print(f"Slice [1:4]: {my_list[1:4]}")
print()

    # 2. Add and remove list elements

print("2. Adding and removing list elements:")

    # Add elements

my_list.append(60)
print(f"After append(60): {my_list}")
my_list.insert(2, 25)
print(f"After insert(2, 25): {my_list}")
my_list.extend([70, 80])
print(f"After extend([70, 80]): {my_list}")

    # Remove elements

my_list.pop()
print(f"After pop(): {my_list}")
my_list.remove(25)
print(f"After remove(25): {my_list}")
print()

    # 3. Sort list elements

print("3. Sorting list elements:")
unsorted_list = [50, 20, 80, 10, 40]
print(f"Unsorted list: {unsorted_list}")
unsorted_list.sort()
print(f"After sort(): {unsorted_list}")
print()

    # 4. Reverse list elements
    
print("4. Reversing list elements:")
reversed_list = [1, 2, 3, 4, 5]
print(f"Original list: {reversed_list}")
reversed_list.reverse()

print(f"After reverse(): {reversed_list}")
