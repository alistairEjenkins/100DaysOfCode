# days in month calculator

def is_leap(year):
    """determines if a year is a leap year int -> boolean"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):

    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year):
        days[1] = 29
    return days[month - 1]

year = int(input("Which year do you want to check?\n>> "))
month = int(input("Which month do you want to check?\n>> "))
print(days_in_month(year, month))
