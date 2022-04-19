def logarithm(base, number):
    '''
        Function -- logarithm
            calculate the log value with given number and base
        Parameters:
            base -- the given base number
            number -- the number user enters
        Return:
            return the final value of the log
    '''
    count = 0
    while number // base != 0:
        number = number // 2
        count += 1
    return count


def main():
    BASETWO = 2
    number = int(input("Enter a positive power of 2: "))
    count = logarithm(BASETWO, number)
    print("lg({}) = {}".format(number, count))


if __name__ == "__main__":
    main()
