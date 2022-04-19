'''
Yiming Ge
CS 5001, Fall 2021

This is a program that 
runners can use to calculate statistics about a race time.
'''

def main():
    distance_km = float(input("How many kilometers did you run? ")) #get the distance runners ran in kilometers
    hours = int(input("What was your finish time? Enter hours: ")) #get the hour it took runners
    minutes = int(input("Enter minutes: ")) #get the remaining minutes after entering hours
    
    distance_mile = round(distance_km/1.61, 2) #get the distance the runners run in miles
    
    total_seconds = hours * 3600 + minutes * 60 #get total seconds runners take
    pace_min = int(total_seconds / (distance_km / 1.61) // 60) #get the minute part for pace
    pace_sec = round(total_seconds / (distance_km / 1.61) % 60) #get the second part for pace
    
    mph = round(distance_km / 1.61 / (hours + minutes / 60), 2) #get miles per hour 
    
    print(str(distance_mile) + " miles, " + str(pace_min) + ":" + str(pace_sec) + " pace, " + str(mph) + " MPH")




if __name__ == "__main__":
    main()

#####3 test cases#####
#5km, 0 hours, 30 minutes => 3.11 miles, 9:40 pace, 6.21 MPH
#10km, 1 hours, 30 minutes => 6.21 miles, 14:29 pace, 4.14 MPH
#20km, 3 hours, 0 minutes => 12.42 miles, 14:29 pace, 4.14 MPH
#3km, 0 hours, 20 minutes => 1.86 miles, 10:44 pace, 5.59 MPH
