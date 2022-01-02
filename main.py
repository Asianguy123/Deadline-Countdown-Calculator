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

def time_left(deadline_y, deadline_m, deadline_d):
    current_time = datetime.datetime.now()
    deadline_time = datetime.datetime(deadline_y, deadline_m, deadline_d)
    remaining_days = (deadline_time - current_time).days
    remaining_seconds = (deadline_time - current_time).seconds
    return remaining_days, remaining_seconds

def total_hours():
    pass
