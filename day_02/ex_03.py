# life left

MAX_AGE = 90
MONTHS_IN_YEAR = 12
WEEKS_IN_YEAR = 52
DAYS_IN_YEAR = 365

age = int(input("What is your age?\n>> "))
years_left = MAX_AGE - age
months_left = years_left * MONTHS_IN_YEAR
weeks_left = years_left * WEEKS_IN_YEAR
days_left = years_left * DAYS_IN_YEAR

print(f"You have {years_left} years left; {months_left} months left;"
      f" {weeks_left} weeks left or {days_left} days left to live, approximately.")