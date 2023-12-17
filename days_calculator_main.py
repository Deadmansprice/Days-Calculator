from datetime import datetime, date
import os, calendar

todays_date = date.today().strftime("%d %B %Y")


standard_year_days = 365
Leap_year_days = 366

print(f"Today's date is {todays_date}")

class date_set():

    def int_to_month_conv(month_conv):
        month = {
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'
        }

        if month_conv in range(1, 13):
            return month[month_conv]
        else: 
            return 'invalid month number'

    def last_day_of_month(year, month):
        _, last_day = calendar.monthrange(year, month)
        return last_day
    
    def set_date():
        counter = 0
        #It will be first year regardless.
        while counter < 2:
            while True:
                year = int(input("What year? Please 4 digits only as we're using Gregorian calendar system\n"))
                if year <= 0:
                    print("You cannot go below 1!")
                    continue
                else:
                    print(f"You have set the year to {year}")
                    break

            #For user input for the first set of date
            while True:
                month = int(input("What month do you want to set it to? Numerical value please, as in '1' for 'January'\n"))
                if month <= 12:
                    print("Within 12 months, moving to next step")
                    break
                else:
                    print("Cannot go past 12 as there are only 12 months in a year\n")
                    continue

        #For day While True loop
            while True:
                day = int(input("What day do you want to set it to?\n"))
                if day > date_set.last_day_of_month(year, month):
                    print("You cannot set the date beyond the last day of this month.")
                    continue
                elif day <= 0:
                    print("You cannot go below 1!")
                    continue
                else:
                    print("This day is within the range of this month")
                    os.system('cls')
                    break
            counter +=1
    
            if counter == 1: 
                first_date = datetime(year, month, day)
                month_covert_to_string = date_set.int_to_month_conv(month) #Calls int_to_month_conv function within date_set class to convert the int provided by user to string within month dictionary.
                first_date_print = f"Your first date has been set: {day} {month_covert_to_string} {year}"
            elif counter == 2: 
                second_date = datetime(year, month, day)
                if second_date < first_date:
                    print("Your second date cannot be less than the first date!")
                    counter = 0
                    continue
                else:
                    second_date_print = f"Your second date has been set: {day} {month_covert_to_string} {year}"
               
                print(first_date_print)
                print(second_date_print)



date_set.set_date()