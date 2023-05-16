# pizza order

bill = 0

size = input("What size pizza would you like? s/m/l")
if size == 's':
    print("You have ordered a small..")
    bill = 15
elif size == 'm':
    print("You have ordered a medium..")
    bill = 20
else:
    print("You have ordered a large..")
    bill = 25

add_pepperoni = input("Do you want to add pepperoni y/n")

if add_pepperoni == 'y':
    print(".. with pepperoni..")
    if size == 's':
        bill += 2
    else:
        bill += 3

extra_cheese= input("Do you want extra cheese y/n?")
if extra_cheese == 'y':
    print(".. with extra cheese.")
    bill += 1

print(f"Your final bill is £{bill}")