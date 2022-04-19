'''
Yiming Ge
CS5001, Fall 2021,lab 03
This is a program to find out
which member you will be in Nogizaka46 (J-pop)
'''


def main():
    # Member Name
    NS = "Nishino Nanase"
    SM = "Shiraishi Mai"
    HS = "Hoshino Minami"
    UM = "Umezawa Minami"
    IE = "Ikuta Erika"
    YY = "Yuki Yoda"
    SA = "Saito Asuka"
    # get the info from user and make them valid
    answer_one = input("Choose your hoobie: A--sports  \
        B--cooking  C--sleeping. ").upper()
    answer_two = input("Choose your height: A--short(under 155cm)  B--average\
        (from 155cm to 175cm) C--high(above 175cm). ").upper()
    answer_three = input("Choose your talent: \
        A--singing  B--dancing C--acting. ").upper()

    is_valid_answer_one = answer_one == "A" or answer_one == "B" \
        or answer_one == "C"
    is_valid_answer_two = answer_two == "A" or answer_two == "B" \
        or answer_two == "C"
    is_valid_answer_three = answer_three == "A" or answer_three == "B" \
        or answer_three == "C"

    if is_valid_answer_one is False:
        answer_one = "A"
    if is_valid_answer_two is False:
        answer_two = "A"
    if is_valid_answer_three is False:
        answer_three = "A"

    member = SA  # default member
    if answer_one == "C":
        member = HS
    elif answer_one == "A" and (answer_two == "A" or answer_two == "B") \
            and answer_three == "A":
        member = IE
    elif answer_one == "B" and answer_two == "B" \
            and (answer_three == "A" or answer_three == "C"):
        member = SM
    elif answer_two == "C":
        member = UM
    elif answer_one == "A" and answer_two == "A" and answer_three == "C":
        member = YY
    elif answer_one == "A" and answer_two == "B" and answer_three == "C":
        member = NS

    print("You are", member)


if __name__ == "__main__":
    main()
