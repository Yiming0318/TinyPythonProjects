'''
Yiming Ge
CS 5001, Fall 2021
Lab06 -- Problem 1
This is a program to compute some statitistics for
a class of students’ scores on an assignment.
'''


def average(listscore):
    if listscore == []:
        return 'empty list'
    sum = 0
    for score in listscore:
        sum += score
    avg_score = sum / len(listscore)
    return avg_score


def median(listscore):
    if listscore == []:
        return 'empty list'
    half = len(listscore) // 2
    listscore.sort()
    if not len(listscore) % 2:
        return (listscore[half - 1] + listscore[half]) / 2.0
    return listscore[half]


def lowest(listscore):
    if listscore == []:
        return 'empty list'
    listscore.sort()
    return listscore[0]


def highest(listscore):
    if listscore == []:
        return 'empty list'
    listscore.sort()
    return listscore[len(listscore) - 1]


def main():
    signal = 'S'
    while signal != 'quit':
        scores = input("Enter the score separated by space,\
            enter quit to quit: ")
        if scores == 'quit':
            signal = 'quit'
        else:
            lst = scores.split()
            for index in range(len(lst)):
                lst[index] = float(lst[index])
            print(lst)
            print(average(lst))
            print(median(lst))
            print(lowest(lst))
            print(highest(lst))


if __name__ == '__main__':
    main()
