# Deadline Calculator

# ------------------------------------------------------------------------------------------------
# Imports

import time
import datetime
import calendar

# ------------------------------------------------------------------------------------------------
# Calculation Functions

def time_today():
    '''
    Calculates hours left on current day at point of program running
    '''

    wknd = False
    current_time = datetime.datetime.now()

    # checking if current day is a weekend
    if calendar.weekday(current_time.year, current_time.month, current_time.day) >= 5:
        wknd = True

    # accounts for rounding current hour
    if current_time.minute >= 30:
        hours_subbed = current_time.hour + 1
    elif current_time.minute < 30:
        hours_subbed = current_time.hour

    # if today is a weekend, give appropriate remaining hours
    if wknd:
        if (24 - hours_subbed) < 10:
            hours = 24 - hours_subbed
        else:
            hours = 10

    # if today is a weekday, give appropriate remaining hours
    if not wknd:
        if (24 - hours_subbed) < 6:
            hours = 24 - hours_subbed
        else:
            hours = 6
    return hours
    
def hours_to_work(hours_today, deadline_y, deadline_m, deadline_d):
    '''
    Calculates total hours left before deadline date
    '''

    free_hours = hours_today
    d0 = datetime.datetime.today()
    d1 = datetime.datetime(deadline_y, deadline_m, deadline_d)
    delta_days = (d1 - d0).days # number of days from today and deadline date

    # check every day before deadline, to see if its a weekend - add appropriate hours
    for i in range(1, delta_days + 1):
        date = d0 + datetime.timedelta(days=i)
        if calendar.weekday(date.year, date.month, date.day) >= 5:
            free_hours += 10
        elif calendar.weekday(date.year, date.month, date.day) <= 4:
            free_hours += 6
    return free_hours

# ------------------------------------------------------------------------------------------------
# Main Function

def main():
    '''
    Main Function - takes user input and outputs text
    '''

    print('Welcome to Deadline Calculator')
    time.sleep(1)
    year = input('Enter the deadline year in yyyy format:  ')
    month = input('Enter the deadline month in mm format:  ')
    date = input('Enter the deadline date in dd format:  ')
    working_hours = hours_to_work(time_today(), int(year), int(month), int(date))   
    print(f'You have {working_hours} hours left to complete your assignment\n')

# ------------------------------------------------------------------------------------------------
# Runs Program

if __name__ == '__main__':
    while True:
        main()
