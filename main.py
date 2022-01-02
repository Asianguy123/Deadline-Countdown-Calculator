# Calculations + User handling

import datetime
import calendar

def user_list():
    pass

def create_user():
    pass

def save_user():
    pass

def login():
    pass

def update_user():
    pass

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

def total_hours():
    pass
