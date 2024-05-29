def convert_time(start):
    time_parts, period = start.split()
    hours, mins = map(int, time_parts.split(':'))  # str -> int

    period = period.upper()

    if period == 'PM' and hours != 12:
        hours += 12  # 24hour format(PM)

    elif period == 'AM' and hours == 12:
        hours = 0  # midnight

    return hours * 60 + mins


def time_format(minutes):
    period = 'AM'
    hours = minutes // 60
    mins = minutes % 60

    if hours >= 24:
        hours -= 24 * (minutes // 1440)

    if hours >= 12:
        period = 'PM'
        if hours > 12:
            hours -= 12


    elif hours == 0:
        hours = 12

    return f'{hours}:{mins:02d} {period}'


def add_time(start, duration, day=None):
    start_mins = convert_time(start)

    d_hours, d_mins = map(int, duration.split(':'))
    duration_mins = d_mins + (d_hours * 60)

    total_mins = start_mins + duration_mins

    new_time = time_format(total_mins)

    total_days = total_mins // 1440

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if day:
        day_index = days.index(day.capitalize())

        days_more = (day_index + total_days) % 7
        new_day = days[days_more]

        if total_days == 0:
            return f'{new_time}, {new_day}'

        elif total_days == 1:
            return f'{new_time}, {new_day} (next day)'
        else:
            return f'{new_time}, {new_day} ({total_days} days later)'

    else:
        if total_days == 0:
            return new_time

        elif total_days == 1:
            return f'{new_time} (next day)'
        else:
            return f'{new_time} ({total_days} days later)'


print(add_time('11:59 PM', '24:05'))



