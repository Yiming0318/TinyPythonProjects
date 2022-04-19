'''
Yiming Ge
CS 5001, Fall 2021
HW02 -- Problem 1 

This is a program that 
is able to help students at a small college register for classes.
'''
def main():
    ori_course = input("Enter a course number: ") # get the course number that the user entered 
    course_number = ori_course.capitalize().replace(" ","") # transform the original course number to the standard format
    
    is_valid_course = course_number == "X101" or course_number == "X102" or course_number == "B500" or course_number == "B525" or course_number == "B701" #valid course numbers at the college
    is_base_course = course_number == "X101" or course_number == "X102" #courses without prerequisites

    if is_valid_course: #check the course number whether is valid
        if is_base_course:
            print("You have successfully registered for", course_number)
        else: #elective courses need prerequisites
            x101_grade = input("What grade did you get for X101? ")
            x102_grade = input("What grade did you get for X102? ")
            if x101_grade.lower() == "a" or x101_grade.lower() == "b" and x102_grade.lower() == "a" or x102_grade.lower() == "b" or x102_grade.lower() ==  "c":
                print("You meet all the prerequisites and have successfully registered for", course_number)
            else: #not meet the prerequisites
                print("You do not meet the prerequisites for", course_number)    
    else:
        print("Invalid course number")


if __name__ == "__main__":
    main()


#####test cases#####
# Enter a course number: b  701
# What grade did you get for X101? F
# What grade did you get for X102? A
# You do not meet the prerequisites for B701

# Enter a course number: 102
# Invalid course number

#Enter a course number: x 1 0 1
#You have successfully registered for X101

# Enter a course number: b 500
# What grade did you get for X101? C
# What grade did you get for X102? C
# You meet all the prerequisites and have successfully registered for B500

# Enter a course number: cs 5001
# Invalid course number