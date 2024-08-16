def add_time(start, duration, day_of_week=None):
    
    dofs = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    time, per = start.split() # Split into components Time: 12:30 and per: PM or AM
    hour, minute = map(int, time.split(':'))

    # Convert time to 24-hour format
    if per == 'PM' and hour != 12: hour += 12
    elif per == 'AM' and hour == 12: hour = 0

    dur_hour, dur_minute = map(int, duration.split(':')) # Split duration into components

    # Add duration to time for final time
    res_hour = hour + dur_hour
    res_minute = minute + dur_minute

    # Adjust final minutes and carry to hours if >60min
    if res_minute >= 60:
        res_hour += res_minute // 60 # Adds to hours
        res_minute = res_minute % 60 # Remaining Minutes 

    # Calculate the number of days later
    later = res_hour // 24
    res_hour = res_hour % 24 # Remaining Hours 

    # Back to 12-hour format
    if res_hour == 0: res_hour = 12 ; per = 'AM'
    elif res_hour < 12: per = 'AM'
    elif res_hour == 12: per = 'PM'
    else: res_hour -= 12 ; per = 'PM'

    new_time = f"{res_hour}:{res_minute:02d} {per}"

    # Calculate the dof
    if day_of_week:
        idx = dofs.index(day_of_week.capitalize())
        new_idx = (idx + later) % 7
        new_day = dofs[new_idx]
        new_time += f", {new_day}"

    # Add number of days later at end
    if later == 1: new_time += " (next day)"
    elif later > 1:
        new_time += f" ({later} days later)"

    return new_time

print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# Returns: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM

print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# Returns: 7:42 AM (9 days later)