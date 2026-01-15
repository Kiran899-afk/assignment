Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("Area Calculation Program")
... print("1. Area of a Circle")
... print("2. Area of a Square")
... print("3. Area of a Triangle")
... 
... choice = int(input("Enter your choice (1-3): "))
... 
... if choice == 1:
...     pi = 3.14159
...     radius = float(input("Enter the radius of the circle: "))
...     area = pi * radius * radius
...     print("Area of the Circle is:", area)
... 
... elif choice == 2:
...     side = float(input("Enter the side of the square: "))
...     area = side * side
...     print("Area of the Square is:", area)
... 
... elif choice == 3:
...     base = float(input("Enter the base of the triangle: "))
...     height = float(input("Enter the height of the triangle: "))
...     area = 0.5 * base * height
...     print("Area of the Triangle is:", area)
... 
... else:
