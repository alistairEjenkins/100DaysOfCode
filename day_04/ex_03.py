# Banker Roulette
from random import choice, randint

diners = input("Can I have the diners names?\n>> ")
diners_lst = diners.split(', ')

paying_diner = choice(diners_lst)
print(f"{paying_diner} will get the bill")

paying_diner = diners_lst[randint(0,len(diners_lst)-1)]
print(f"{paying_diner} will get the bill")
