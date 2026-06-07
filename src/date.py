def month_first_day(day,week):
    day %= 7
    if day == 0:
        day=7
    return week - (day - 1)

def leap_year(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    return False

def month_day(y = 2026, m=1):
    if m == 2:
        if leap_year(y):
            return 29
        else:
            return 28
    elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    else:
        return 30     