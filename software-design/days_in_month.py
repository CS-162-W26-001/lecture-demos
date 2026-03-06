from is_leap_year import is_leap_year


def days_in_month(month: int, year: int) -> int:
    if month == 4 or month == 6 or month == 9 or month == 11: 
        return 30
    if month == 2:
        if is_leap_year(year): 
            return 29
        else:
            return 28
    return 31
