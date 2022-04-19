
'''
Yiming Ge
CS 5001, Fall 2021
Lab09
This is a program to process the IMDB dataset – a benchmark dataset widely
used to develop and evaluate sentiment classifiers.
'''


def read_lines(file_path):
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line)
    return lines


def check_lines_format(path):
    negative_review = []
    positive_review = []
    line_list = read_lines(path)
    for review in line_list:
        number = review.split('\t')
        if int(number[1]) == 0:
            negative_review.append(review)
        if int(number[1]) == 1:
            positive_review.append(review)
    return positive_review, negative_review


def write_reviews(file_path, content):
    lines = content
    with open(file_path, "w") as file:
        for line in lines:
            comment = line.split('\t')
            file.write(comment[0] + '\n')


def main():
    while True:
        try:
            path = input("Enter the path to the IMDB dataset: ")
            positive_list, negative_list = check_lines_format(path)
            print(len(positive_list))
            print(len(negative_list))
            write_reviews('positive.txt', positive_list)
            write_reviews('negative.txt', negative_list)
            break
        except FileNotFoundError:
            print("File not found!")
            continue
        except IndexError:
            print("Error processing the file.")
            continue
    input_commands = input("Enter commands: ")
    while input_commands != 'q':
        try:
            command_list = input_commands.split(" ")
            lines_list = read_lines('negative.txt')
            if command_list[0] == 'p':
                lines_list = read_lines('positive.txt')
            print(lines_list[int(command_list[1])].strip())
        except ValueError:
            print("Doesn’t provide a valid integer")
        except IndexError:
            print("Out of range")
        input_commands = input("Enter commands: ")


if __name__ == "__main__":
    main()
