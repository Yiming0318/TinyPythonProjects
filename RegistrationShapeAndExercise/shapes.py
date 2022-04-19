'''
Yiming Ge
CS 5001, Fall 2021
HW02 -- Problem 2

This is a program that is able to calculate the area of a shape
based on given information from users.
'''


def main():
    SQUARE = "square"
    TRIANGLE = "triangle"
    RECTANGLE = "rectangle"
    # transform the original information to the all lowercase string
    shape = input("Select a shape(triangle, square, or rectangle): ").lower()
    is_valid = shape == TRIANGLE or shape == SQUARE or shape == RECTANGLE
    if is_valid:  # check the given shape whether is valid
        width = float(input("Enter the width: "))
        if width <= 0:
            print("Invalid width")
        else:
            height = width  # set defalut as square
            if shape != SQUARE:   # ask for the height except the square
                height = float(input("Enter the height: "))
            if height >= 0:
                area = width * height   # square area or rectangle area
                if shape == TRIANGLE:
                    area = area / 2    # triangle area
                print("The area of the {} is {:.2f}".format(shape, area))
            else:
                print("Invalid height")
    else:
        print("Unknown shape")


if __name__ == "__main__":
    main()

# Test cases
# Select a shape(triangle, square, or rectangle): rectangle
# Enter the width: 3
# Enter the height: 4
# The area of the rectangle is 12.00

# Select a shape(triangle, square, or rectangle): triangle
# Enter the width: -35
# Invalid width

# Select a shape(triangle, square, or rectangle): square
# Enter the width: 10
# The area of the square is 100.00

# Select a shape(triangle, square, or rectangle): triangle
# Enter the width: 3.1
# Enter the height: 4.2
# The area of the triangle is 6.51

# Select a shape(triangle, square, or rectangle): rectangle
# Enter the width: 32
# Enter the height: -10
# Invalid height

# Select a shape(triangle, square, or rectangle): diamond
# Unknown shape
