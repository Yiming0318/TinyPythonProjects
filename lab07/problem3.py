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
    if base > 0:
        if number < base:
            return 0
        else:
            return 1 + logarithm(base, number/base)
    return 0


def bintodeci(binary):
    '''
        Function -- bintodeci
            calculate the decimal of the binary
        Parameters:
            binary == a binary number
        Return:
            return the decimal number
    '''
    n = len(binary)
    if n == 1:
        return int(binary[0])
    if n == 0:
        return []
    return int(binary[0]) * (2 ** (n - 1)) + bintodeci(binary[1:])
