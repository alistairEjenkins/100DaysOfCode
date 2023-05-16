# BMI Calculator v2

height = float(input("Enter your height (m):\n>> "))
weight = int(input("Enter your weight (kg):\n>> "))

bmi = int(weight / height ** 2)
bmi = round(bmi)

print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You are normal weight.")
elif bmi < 30:
    print("You are overweight.")
elif bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese")