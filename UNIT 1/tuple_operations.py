# Python program to perform various operations on tuples

    # 1. Create and access tuple elements
print("1. Creating and accessing tuple elements:")
my_tuple = (10, 20, 30, 40, 50)
print(f"Original tuple: {my_tuple}")
print(f"First element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")
print(f"Slice [1:4]: {my_tuple[1:4]}")
print()

    # 2. Nested tuple
print("2. Nested tuple:")
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(f"Nested tuple: {nested_tuple}")
print(f"Access nested element: {nested_tuple[0][1]}")
print()

    # 3. Repetition of tuple
print("3. Repetition of tuple:")
repeated_tuple = my_tuple * 2
print(f"Original tuple repeated 2 times: {repeated_tuple}")
print()

    # 4. Concatenation of tuples
print("4. Concatenation of tuples:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(f"Tuple1: {tuple1}")
print(f"Tuple2: {tuple2}")
print(f"Concatenated: {concatenated_tuple}")
