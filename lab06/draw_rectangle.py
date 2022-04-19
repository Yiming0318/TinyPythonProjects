'''
Yiming Ge
CS 5001, Fall 2021
Lab06 -- Problem 3
This is a program to draw a rectangle on the command line.
'''


def main():
    width = int(input('enter width: '))
    height = int(input('enter height: '))
    character = input('enter the character: ')
    for i in range(1, height+1):
        for j in range(1, width+1):
            if i == 1 or i == height or j == 1 or j == width:
                print(character, end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    main()
