'''
Lab12 Starter Code
CS 5001, Fall 2021
Yiming Ge
This a program that a TA could use to keep track of students waiting to talk
to them during office hours
'''
from queue_impl import Queue
ADD = 'add a name to the queue'
FINISH = 'finish a meeting'
QUIT = 'quit'
MEETING = 'in a meeting'
WAITING = 'waiting'


def main():
    q = Queue()
    quit = 0
    teacher_status = WAITING
    while quit != 3:
        choices = int(input('1 - {}, 2 - {}, 3 - {} '.
                      format(ADD, FINISH, QUIT)))
        if choices == 3:
            quit = 3
        elif choices == 1 and teacher_status == WAITING:
            student_name = input("Enter the student's name: ")
            q.enqueue(student_name)
            teacher_status = MEETING
            print('You are ' + MEETING + ' with ' + student_name)
        elif choices == 1 and teacher_status == MEETING:
            student_name = input("Enter the student's name: ")
            q.enqueue(student_name)
            print(student_name + ' added to the queue')
        elif choices == 2 and q.is_empty() is False:
            q.dequeue()
            if q.is_empty() is True:
                teacher_status == WAITING
                print('No students in the queue.')
            else:
                student_name = q.peek()
                print('You are meeting with ' + student_name)


if __name__ == '__main__':
    main()