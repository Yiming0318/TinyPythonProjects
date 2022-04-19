'''
Yiming Ge, Jin Zhang, Shenguo Zhou
CS 5001, Fall 2021
Lab08
This a program to decrypt the given message with
brute force
'''
from encrypt_and_decrypt import decrypt


def deslide(message, slide_amount):
    LENGTH = len(message)
    MIN = 0
    message_list = list(message)
    for index, value in enumerate(message):
        if index - slide_amount < MIN:
            de_index = index + LENGTH - slide_amount
            message_list[de_index] = value
        else:
            de_index = index - slide_amount
            message_list[de_index] = value
    return "".join(message_list)


def brute_force(message, shift_amount, slide_amount):
    return decrypt(deslide(message, slide_amount), shift_amount)


def main():
    # message = "*.glygo rsvvmw'w gshi avmxiw gsqqirxw efsyx *lmq"
    # message = "aqwuvwem, kp cp kphkpkvg nqqr, ykvj"
    message = ".sjajw ywzxy f htruzyjw dtz hfs’y ymwtb tzy f bnsitb.."
    # message = "yko.vjg swguvkqp qh yjgvjgt eqorwvgtu ecp vjkpm ku nkmg vjg swguvkqp qh yjgvjgt uwdoctkpgu ecp u"
    # message = ".ejwem pqttku ytkvgu dqqngcp gzrtguukqpu vjcv ctg dqvj vtwg cpf hcnug"
    for shift_amount in range(1, 6):
        for slide_amount in range(1, 6):
            print(brute_force(message, shift_amount, slide_amount))
    # chuck norris's code writes comments about *him*.
    # stuck, in an infinite loop, withyou
    # never trust a computer you can’t throw out a window...
    # the question of whether computers can think is like the question of whether submarines can swim.
    # chuck norris writes boolean expressions that are both true and false.


if __name__ == "__main__":
    main()