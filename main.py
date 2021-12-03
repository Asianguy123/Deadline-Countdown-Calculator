# Calculations + User handling

import datetime
import math

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
    current_time = datetime.datetime.now()
    minutes = int(current_time.strftime('%M'))
    hours_left_today = 24 - int(current_time.strftime('%H'))
    if minutes >= 30:
        hours_left_today -= 1  
    return hours_left_today

def total_hours():
    pass
