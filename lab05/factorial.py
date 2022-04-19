def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def main():
    number = float(input("Enter a number: "))
    sign = "S"
    while sign != "q":
        data = input("Enter the next step in the calculation: ").split()
        if len(data) == 1:
            if data[0] == "q" or data[0] == "Q":
                sign = "q"
                break
            else:
                number = add(number, float(data[0]))
        else:
            operator = data[0]
            number2 = float(data[1])
            if operator == "+":
                number = add(number, number2)
            elif operator == "-":
                number = subtract(number, number2)
            elif operator == "*":
                number = multiply(number, number2)
            elif operator == "/":
                number = divide(number, number2)
        print("Subtotal = {}".format(number))
    print("Total = {}".format(number))


if __name__ == "__main__":
    main()
