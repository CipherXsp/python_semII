# main.py
# Program to calculate area using shapes module

import shapes

print("Select Shape")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    area = shapes.area_circle(r)
    print("Area of Circle =", area)

elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    area = shapes.area_rectangle(l, w)
    print("Area of Rectangle =", area)

elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = shapes.area_triangle(b, h)
    print("Area of Triangle =", area)

else:
    print("Invalid choice")
