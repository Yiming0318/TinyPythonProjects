'''
Yiming Ge, Jin Zhang, Shenguo Zhou
CS 5001, Fall 2021
Lab08
This a program to encrypt and decrypt the given message with
shift amount
'''


def encrypt(message, shift_amount):
    SHIFT_MIN = 0
    SHIFT_MAX = 25
    Z = 122
    TOTAL_LETTER = 26
    if shift_amount >= SHIFT_MIN or shift_amount <= SHIFT_MAX:
        shift_amount = shift_amount
    else:
        shift_amount = shift_amount % SHIFT_MAX
    message = message.lower()
    encrypted_list = []
    for string in message:
        if string.isalpha():
            if ord(string) + shift_amount > Z:
                encrypted_string = chr(ord(string) + shift_amount -
                                       TOTAL_LETTER)
                encrypted_list.append(encrypted_string)
            else:
                encrypted_string = chr(ord(string) + shift_amount)
                encrypted_list.append(encrypted_string)
        else:
            encrypted_list.append(string)
    return "".join(encrypted_list)


def decrypt(message, shift_amount):
    SHIFT_MIN = 0
    SHIFT_MAX = 25
    A = 97
    TOTAL_LETTER = 26
    if shift_amount >= SHIFT_MIN or shift_amount <= SHIFT_MAX:
        shift_amount = shift_amount
    else:
        shift_amount = shift_amount % SHIFT_MAX
    message = message.lower()
    decrypted_list = []
    for string in message:
        if string.isalpha():
            if ord(string) - shift_amount < A:
                decrypted_string = chr(ord(string) - shift_amount +
                                       TOTAL_LETTER)
                decrypted_list.append(decrypted_string)
            else:
                decrypted_string = chr(ord(string) - shift_amount)
                decrypted_list.append(decrypted_string)
        else:
            decrypted_list.append(string)
    return "".join(decrypted_list)


def main():
    message = input("Enter a message to encript:\n")
    shift_amount = int(input("Enter a shift amount:\n"))
    encrypt_message = encrypt(message, shift_amount)
    decrypt_message = decrypt(encrypt_message, shift_amount)
    print("Your super secret message is:", encrypt_message)
    print("...decrypting encoded message now...")
    print("It was:", decrypt_message)


if __name__ == "__main__":
    main()
