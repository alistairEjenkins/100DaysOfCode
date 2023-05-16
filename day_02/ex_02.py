# BMI Calculator

height = float(input("Enter your height (m):\n>> "))
weight = int(input("Enter your weight (kg):\n>> "))

bmi = int(weight / height ** 2)

print(f"Your BMI is {bmi}")