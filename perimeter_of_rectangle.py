#!/usr/bin/env python3

# Created by:Sam. Garcon
# Created on:April 2021
# This program calculates the area and perimeter of a circle
#    with radius inputted from the user

def main():
    # this function calculates area and perimeter

    # input
    length = float(input("Enter length of the rectangle: "))
    width = float(input("Enter width of the rectangle: "))

    # process
    perimeter = 2 * (length + width)
    area = width * length 

    # output
    print("")
    print("Area is {0} mm².".format(area))
    print("Perimeter is {0} mm.".format(perimeter))

if __name__ == "__main__":
    main()
    