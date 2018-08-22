
"""
Author: Chané van der Berg
Last date modified: 25/03/18

Practical activity testing student's ability to use functions to calculate
averages, outputs based on a circle's radius and the distance between points.

Activity is split into 3 assignments:
1. Calculate the average of 5 numbers that are entered by the user
2. Write a program that accepts a circle's radius request as input and calculates
the following
    The radius (r)
    The diameter (2r)
    The circumference (2πr)
    The area ((πr^2)

3. Write a program that accepts the (x:y) co-ordinates for two points in space
and calculates the Euclidean distance between these points.
"""
import math

print()
print("Assignment 1")
print()
# define variables and convert strings to numbers
val1 = float(input("Enter value 1: "))
val2 = float(input("Enter value 2: "))
val3 = float(input("Enter value 3: "))
val4 = float(input("Enter value 4: "))
val5 = float(input("Enter value 5: "))

# algorithm to average given values
avg = float((val1 + val2 + val3 + val4 + val5) / 5)
print()

# output
print("The average of the values is: ",str(avg))
print()

print("Assignment 2")
print()

# define variable and convert string to number
r = float(input("What is the radius of the circle?: "))
print()

# calculations to be used for outputs
# calculate diameter
diameter = round((2 * r), 2)
# calculate circumference
circumference = round((2 * math.pi * r), 2)
# calculate area
area = round((math.pi * r ** 2), 2)

# print outputs
print("The radius of the circle is: ",str(r))
print("The diameter of the circle is: ",str(diameter))
print("The circumference of the circle is: ",str(circumference))
print("The area of the circle is: ",str(area))
print()
print()

print("Assignment 3")
print()

# define variables and convert strings to numbers
x1 = float(input("Enter the x coordinate for point1: "))
y1 = float(input("Enter the y coordinate for point1: "))
x2 = float(input("Enter the x coordinate for point2: "))
y2 = float(input("Enter the y coordinate for point2: "))

#calculate distance
distance = float(math.sqrt((x1 - y1) ** 2 + (x2 - y2) ** 2))

# output
print("The distance between point1 and point2 is: ",str(distance))
print()
