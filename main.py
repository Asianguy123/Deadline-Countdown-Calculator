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

def total_hours():
    pass
