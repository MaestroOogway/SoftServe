from math import pi, pow
from areas import rectangle_area, triangle_area, circle_area


print("Choose figure:")
print("1 - Rectangle")
print("2 - Triangle")
print("3 - Circle")

choice = input("Enter option: ")

if choice == "1":
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    print("Area:", rectangle_area(a, b))

elif choice == "2":
    h = float(input("Enter height: "))
    a = float(input("Enter base: "))
    print("Area:", triangle_area(h, a))

elif choice == "3":
    r = float(input("Enter radius: "))
    print("Area:", circle_area(r, pi, pow))

else:
    print("Invalid option")