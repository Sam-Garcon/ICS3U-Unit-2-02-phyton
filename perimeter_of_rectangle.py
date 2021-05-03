#!/usr/bin/env python3

# Created by: Sam. Garcon
# Created on: April 2021
# This program calculates the area and perimeter of a rectangle
# with radius inputted from the user


# Area & Perimeter of Rectangle

# Reading length from user
length = float(input("Enter length of the rectangle: "))

# Reading breadth from user
width = float(input("Enter width of the rectangle: "))

# Calculating area
area = length * width

# Calculating perimeter
perimeter = 2 * (length + width)

# Displaying results
print("Area of rectangle = ", area)
print("Perimeter of rectangle = ", perimeter)