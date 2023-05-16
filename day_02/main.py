# tip calculator

print("Welcome to the Tip Calculator")

total_bill = float(input("What is the total bill?\n>> £"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n>> "))
diners = int(input("How many diners were there?\n>> "))

grand_total = total_bill * (100 + tip) / 100
split = grand_total / diners

print(f"Each person should pay: £{round(split, 2):.2f}")
