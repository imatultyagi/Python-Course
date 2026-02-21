# area and parameter of circle
import math
def area_of_circle(radius):
    area = math.pi * radius ** 2
    return area 
def perimeter_of_circle(radius):
    perimeter = 2 * math.pi * radius
    return perimeter
radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
perimeter = perimeter_of_circle(radius)
print("The area of the circle is: ", area)
print("The perimeter of the circle is: ", perimeter)



# output:Enter the radius of the circle: 5
# output:The area of the circle is:  78.53981633974483
# output:The perimeter of the circle is:  31.41592653589793
