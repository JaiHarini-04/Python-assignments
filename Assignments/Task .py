import math

def compute_circle_area(radius):
    area = math.pi * radius ** 2
    return area

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Compute the area of the circle
area = compute_circle_area(radius)

# Print the result
print("The area of the circle is:", area)
