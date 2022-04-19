'''
Yiming Ge
CS 5001, Fall 2021

This is a program that 
calculate how many tables that the robot can make with given ingredients.
'''
def main():
    # get the given ingredients data
    tops = int(input("Number of tops: ")) 
    legs = int(input("Number of legs: "))
    screws = int(input("Number of screws: "))
    # calculate the total number of tables that can be made with all the ingredients available 
    total_tables = min(tops // 1 , legs // 4, screws // 8) 
    
    # calculate the amount leftover of each ingredient after the tables are made
    leftover_tops = tops - 1 * total_tables
    leftover_legs = legs - 4 * total_tables
    leftover_screws = screws - 8 * total_tables

    print(total_tables,"tables assembled.","Leftover parts:",leftover_tops,"table tops,",leftover_legs,"legs,",leftover_screws,"screws.")


if __name__ == "__main__":
    main()

#####3 test cases#####
#4 tops, 20 legs, 32 screws => 4 tables assembled. Leftover parts: 0 table tops, 4 legs, 0 screws.
#10 tops, 10 legs, 10 screws => 1 tables assembled. Leftover parts: 9 table tops, 6 legs, 2 screws.
#5 tops, 20 legs, 30 screws => 3 tables assembled. Leftover parts: 2 table tops, 8 legs, 6 screws.
#100 tops, 400 legs, 800 screws => 100 tables assembled. Leftover parts: 0 table tops, 0 legs, 0 screws.