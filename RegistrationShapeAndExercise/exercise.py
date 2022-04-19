'''
Yiming Ge
CS 5001, Fall 2021
HW02 -- Problem 3

This is a program that 
is able to create an exercise plan based on the day of the week and the weather.
'''

def main():
    NORMAL_DURATION = "45"
    MODIFIED_DURATION = "30"
    LOWEST_TEMPERATURE = 35
    HIGHEST_TEMPERATURE = 75
    RUN = "Run"
    SWIM = "Swim"
    HIKE = "Hike"
    #get the info from users and make these info standard
    day =  input("What day is it? ").capitalize()
    holiday = input("Is it a holiday? ").upper()
    rain = input("Is it raining? ").upper()
    temperature = float(input("What is the temperature? "))

    is_valid_day = day == "M" or day == "Tu" or day == "W" or day == "Th" or day == "F" or day == "Sa" or day == "Su"
    is_valid_holiday = holiday == "Y" or holiday == "N"
    is_valid_rain = rain == "Y" or rain == "N"
    is_workout_day = day == "M" or day == "W" or day == "F" or day == "Sa" or holiday == "Y"
    is_raining = rain == "Y"
    is_holiday = holiday == "Y"
    is_cold = temperature < LOWEST_TEMPERATURE
    is_hot = temperature > HIGHEST_TEMPERATURE
    
    if is_valid_day and is_valid_holiday and is_valid_rain: #check the validity of the given info
        if is_workout_day:  
            duration = NORMAL_DURATION  
            if is_raining: 
                exercise =  SWIM
            elif day == "Sa" or is_holiday:
                exercise = HIKE
            else: #days are not raining and not holiday monday or wednesday or friday
                exercise = RUN
                if is_cold or is_hot: #only running will be impacted by the temperature
                    duration = MODIFIED_DURATION
            print(exercise, "for", duration, "minutes")
        else: #rest day
            print("Take a rest day")    
    else:
        print("Swim for 35 minutes")

if __name__ == "__main__":
    main()


######test cases######
# What day is it? m
# Is it a holiday? y
# Is it raining? n
# What is the temperature? 34
# Hike for 45 minutes

# What day is it? TU
# Is it a holiday? N
# Is it raining? Kind of
# What is the temperature? 85
# Swim for 35 minutes

# What day is it? SA
# Is it a holiday? Y
# Is it raining? Y
# What is the temperature? 80
# Swim for 45 minutes

# What day is it? idk
# Is it a holiday? maybe
# Is it raining? I am not sure
# What is the temperature? 60
# Swim for 35 minutes

# What day is it? f
# Is it a holiday? n
# Is it raining? n
# What is the temperature? 20
# Run for 30 minutes

# What day is it? m
# Is it a holiday? n
# Is it raining? n
# What is the temperature? 100
# Run for 30 minutes