PHI = 3.14

def triangle(base, height):
    area = (base * height) / 2
    return (f"The area of the triangle is: {area}")

def circle(ratio):
    area = ratio*ratio*PHI
    return (f"The area of the circle is: {area}")

def rectangle(base, height):
    area = base * height
    return (f"The area of the rectangle is: {area}")


enter = True

while (enter):
    choice = int(input("Chose the area of: \n" \
    "1) triangle \n" 
    "2) circle \n" 
    "3) rectangle \n"))

    if (choice == 1):
        base = 34
        height = 567
        print(triangle(base, height))
    elif (choice == 2):
        ratio = 5.34
        print(circle(ratio))
    elif (choice == 3):
        base = 3
        height = 67
        print(rectangle(base, height))

    enter = False