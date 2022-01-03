# Deadline Calculator

import time
import datetime
import calendar

def time_today():
    wknd = False
    current_time = datetime.datetime.now()
    if calendar.weekday(current_time.year, current_time.month, current_time.day) >= 5:
        wknd = True
    if current_time.minute >= 30:
        hours_subbed = current_time.hour + 1
    elif current_time.minute < 30:
        hours_subbed = current_time.hour

    if wknd:
        if (24 - hours_subbed) < 10:
            hours = 24 - hours_subbed
        else:
            hours = 10
    if not wknd:
        if (24 - hours_subbed) < 6:
            hours = 24 - hours_subbed
        else:
            hours = 6
    return hours
    
def hours_to_work(hours_today, deadline_y, deadline_m, deadline_d):
    free_hours = hours_today
    d0 = datetime.datetime.today()
    d1 = datetime.datetime(deadline_y, deadline_m, deadline_d)
    delta_days = (d1 - d0).days
    for i in range(1, delta_days + 1):
        date = d0 + datetime.timedelta(days=i)
        if calendar.weekday(date.year, date.month, date.day) >= 5:
            free_hours += 10
        elif calendar.weekday(date.year, date.month, date.day) <= 4:
            free_hours += 6
    return free_hours

def main():
    print('Welcome to Deadline Calculator')
    time.sleep(1)
    year = input('Enter the deadline year in yyyy format:  ')
    month = input('Enter the deadline month in mm format:  ')
    date = input('Enter the deadline date in dd format:  ')
    working_hours = hours_to_work(time_today(), int(year), int(month), int(date))
    print(f'You have {working_hours} hours left to complete your assignment')
    exit = input('Calculation complete, hit enter to close:  ')

if __name__ == '__main__':
    main()
