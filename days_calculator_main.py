from datetime import datetime
import os, calendar, time
from dateutil import relativedelta

standard_year_days = 365
Leap_year_days = 366

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
                year = int(input("What year? Please 4 digits only as we're using Gregorian calendar system in AD.\n"))
                if year < 0:
                    print("You cannot go below 1!")
                    continue
                else:
                    print(f"You have set the year to {year}")
                    break

            #For user input for the first set of date
            while True:
                month = int(input("What month do you want to set it to? Numerical value please, as in '1' for 'January'\n"))
                if month < 1:
                    print("You cannot go below 1!")
                    continue
                elif month <= 12:
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
                elif day < 1:
                    print("You cannot go below 1!")
                    continue
                else:
                    print("This day is within the range of this month")
                    os.system('cls')
                    break
            counter +=1
    
            if counter == 1: 
                global first_date #necessary for date comparison
                first_date = datetime(year, month, day)
                month_covert_to_string = date_set.int_to_month_conv(month) #Calls int_to_month_conv function within date_set class to convert the int provided by user to string within month dictionary.
                first_date_print = f"Your first date has been set: {day} {month_covert_to_string} {year}"
                print(first_date_print)
            elif counter == 2: 
                global second_date #necessary for date comparison
                second_date = datetime(year, month, day)
                if second_date < first_date:
                    print("Your second date cannot be less than the first date!")
                    counter = 0
                    continue
                else:
                    second_date_print = f"Your second date has been set: {day} {month_covert_to_string} {year}"
                
                time.sleep(2)
                os.system('cls')
                print(first_date_print)
                print(second_date_print)


class date_comparison:
    def compare_dates():
        #pulls in global variable that would be shown in the set_date class.
        date_delta = relativedelta.relativedelta(first_date,second_date)
        day_delta = second_date - first_date

        print(f"The difference between the dates are in {abs(date_delta.years)} years, {abs(date_delta.months)} months, {abs(date_delta.weeks)} weeks, {abs(date_delta.days)} days")
        print(f"In total number of months: {abs(date_delta.years * 12)}") #number of months in year. so 12 x however many years.
        print(f"In total number of weeks: {abs(date_delta.years * 52)}") #number of whole weeks. 
        print(f"In total number of days: {abs(day_delta.days)}") #calculates number of days between two dats.
        print(f"In total number of days, including end date: {abs(day_delta.days + 1)}")

class main_menu:
    def main_menu():
        user_confirmation = input("Would you like to compare dates? y for 'yes', n for 'no' \n")
        while user_confirmation.strip().lower() == 'y':
            date_set.set_date()
            date_comparison.compare_dates()
            user_confirmation_continue = input("Continue? y for yes, n for no only.\n")
            if user_confirmation_continue.strip().lower() == 'y':
                print('Continuing')
                time.sleep(2)
                os.system('cls')
                continue
            elif user_confirmation_continue.strip().lower() == 'n':
                print('exiting')
                exit()
            else: 
                print('No other input allowed. Continuing')
                continue


main_menu.main_menu()